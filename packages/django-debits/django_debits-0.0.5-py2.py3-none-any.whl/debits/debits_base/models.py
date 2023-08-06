import abc
import hmac
import datetime

import html2text
from django.apps import apps
from django.urls import reverse
from django.db import models
from django.db.models import F
import django.db
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from composite_field import CompositeField
from django.conf import settings

from debits.debits_base.base import logger, Period
from debits.paypal.utils import PayPalUtils


class ModelRef(CompositeField):
    """Reference to a Django model"""

    app_label = models.CharField(_('Django app with the model'), max_length=100)
    """Django app with the model."""

    model = models.CharField(_('Python model class name'), max_length=100)
    """The model class name."""


# The following function does not work as a method, because
# CompositeField is replaced with composite_field.base.CompositeField.Proxy:

def model_from_ref(model_ref):
    """Retrieves a model from `ModelRef`.

    Args:
        model_ref: A `ModelRef` field instance.

    Returns:
        A Django model class.
    """
    return apps.get_model(model_ref.app_label, model_ref.model)


class PaymentProcessor(models.Model):
    """Payment processor (such as PayPal, DalPay, etc.)"""

    name = models.CharField(_('The name of the company'), max_length=255)
    """The name of the payment processing company or service."""

    url = models.URLField(max_length=255)
    """The site of the payment processor."""

    api = ModelRef()
    """The Django model which handles API for payments."""

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('Product name'), max_length=255)
    """Product name."""

    def __str__(self):
        return self.name


# The following function does not work as a method, because
# CompositeField is replaced with composite_field.base.CompositeField.Proxy:

def period_to_string(period):
    """Human readable description of a period.

    Args:
        period: `Period` field.

    Returns:
        A human readable string.

    TODO:
        Move to `base.py`.
    """
    hash = {e[0]: e[1] for e in Period.period_choices}
    return "%d %s" % (period.count, hash[period.unit])


class BaseTransaction(models.Model):
    """A redirect (or other query) to the payment processor.

    It may be paid or (not yet) paid."""

    # class Meta:
    #     abstract = True

    processor = models.ForeignKey(PaymentProcessor, on_delete=models.CASCADE)
    """Payment processor."""

    creation_date = models.DateField(auto_now_add=True)
    """Date of the redirect.
    
    TODO:
        Use time with seconds precision?
    """

    def __repr__(self):
        return "<BaseTransaction: %s>" % (("pk=%d" % self.pk) if self.pk else "no pk")

    @staticmethod
    def custom_from_pk(pk):
        """Secret code of a transaction.

        Secret can be known only to one who created a BaseTransaction.
        This prevents third parties to make fake IPNs from a payment processor.

        Args:
            pk: the serial primary key (of :class:`BaseTransaction`) used to calculate the secret transaction code.

        Returns:
            A secret string."""
        secret = hmac.new(settings.SECRET_KEY.encode(), ('payid ' + str(pk)).encode()).hexdigest()
        return settings.PAYMENTS_REALM + ' ' + str(pk) + ' ' + secret

    @staticmethod
    def pk_from_custom(custom):
        """Restore the :class:`BaseTransaction` primary key from the secret "custom".

        Raises :class:`BaseTransaction.DoesNotExist` if the custom is wrong.

        Args:
            custom: A secret string.

        Returns:
            The primary key for :class:`BaseTransaction`."""
        r = custom.split(' ', 2)
        if len(r) != 3 or r[0] != settings.PAYMENTS_REALM:
            raise BaseTransaction.DoesNotExist
        try:
            pk = int(r[1])
            secret = hmac.new(settings.SECRET_KEY.encode(), ('payid ' + str(pk)).encode()).hexdigest()
            if r[2] != secret:
                raise BaseTransaction.DoesNotExist
            return pk
        except ValueError:
            raise BaseTransaction.DoesNotExist

    @abc.abstractmethod
    def invoice_id(self):
        """Invoice ID.

        Used internally to prevent more than one payment for the same transaction."""
        pass

    def invoiced_item(self):
        """Internal."""
        return self.item.old_subscription.transaction.item \
            if self.item and self.item.old_subscription \
            else self.item

    @abc.abstractmethod
    def subinvoice(self):
        """Subinvoice ID.

        Used internally to prevent more than one payment for the same transaction."""
        pass

class SimpleTransaction(BaseTransaction):
    """A one-time (non-recurring) transaction."""

    item = models.ForeignKey('SimpleItem', related_name='transactions', null=False, on_delete=models.CASCADE)
    """The stuff sold by this transaction."""

    def subinvoice(self):
        return 1

    def invoice_id(self):
        return settings.PAYMENTS_REALM + ' p-%d' % (self.item.pk,)

    def on_accept_regular_payment(self, email):
        """Handles confirmation of a (non-recurring) payment."""
        payment = SimplePayment.objects.create(transaction=self, email=email)
        self.item.paid = True
        self.item.last_payment = datetime.date.today()
        self.item.upgrade_subscription()
        self.item.save()
        try:
            self.advance_parent(self.item.prolongitem)
        except AttributeError:
            pass
        return payment


    @transaction.atomic
    def advance_parent(self, prolongitem):
        """Advances the parent transaction on receive of a "prolong" payment.

        Args:
            prolongitem: :class:`ProlongItem`.

        `prolongitem.prolong` contains the number of days to advance the parent (:class:`SubscriptionItem`)
        item. The parent transaction is advanced this number of days.
        """
        parent_item = SubscriptionItem.objects.select_for_update().get(
            pk=prolongitem.parent_id)  # must be inside transaction
        # parent.email = transaction.email
        base_date = max(datetime.date.today(), parent_item.due_payment_date)
        parent_item.set_payment_date(PayPalUtils.calculate_date(base_date, prolongitem.prolong))
        parent_item.save()


class SubscriptionTransaction(BaseTransaction):
    """A transaction for a subscription service."""

    item = models.ForeignKey('SubscriptionItem', related_name='transactions', null=False, on_delete=models.CASCADE)
    """The stuff sold by this transaction information."""

    def subinvoice(self):
        return self.invoiced_item().subinvoice

    def invoice_id(self):
        if self.item.old_subscription:
            return settings.PAYMENTS_REALM + ' %d-%d-u' % (self.item.pk, self.subinvoice())
        else:
            return settings.PAYMENTS_REALM + ' %d-%d' % (self.item.pk, self.subinvoice())

    def create_active_subscription(self, ref, email):
        """Internal."""
        self.item.active_subscription = Subscription.objects.create(transaction=self,
                                                                    subscription_reference=ref,
                                                                    email=email)
        self.item.save()
        return self.item.active_subscription

    @django.db.transaction.atomic
    def obtain_active_subscription(self, ref, email):
        """Internal."""
        if self.item.active_subscription and self.item.active_subscription.subscription_reference == ref:
            return self.item.active_subscription
        else:
            return self.create_active_subscription(ref, email)


class Item(models.Model):
    """Anything sold or rent.

    Apps using this package should create their product records manually.
    Then you create an instance of a subclass of this class before allowing
    the user to make a transaction.

    In a future we may provide an interface for registering new products.
    """

    creation_date = models.DateField(auto_now_add=True)
    """Date of item creation.

    TODO:
        Use time with seconds precision?
    """

    product = models.ForeignKey('Product', null=True, on_delete=models.CASCADE)
    """The sold product."""

    product_qty = models.IntegerField(default=1)
    """Quantity of the sold product (often 1)."""

    blocked = models.BooleanField(default=False)
    """A hacker or misbehavior detected."""

    currency = models.CharField(max_length=3, default='USD')
    """The currenct for which this is sold."""

    price = models.DecimalField(max_digits=10, decimal_places=2)
    """Price of the item.
    
    For recurring payment it is the amount of one payment."""

    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    """Price of shipping.
    
    Remain zero if doubt."""

    # code = models.CharField(max_length=255) # TODO

    gratis = models.BooleanField(default=False)
    """Provide a product or service for free."""

    # recurring = models.BooleanField(default=False)

    reminders_sent = models.SmallIntegerField(default=0, db_index=True)
    """Email (or SMS, etc.) payment reminders sent state.
    
    * 0 - no reminder sent
    * 1 - before due payment sent
    * 2 - at due payment sent
    * 3 - day before deadline sent"""

    old_subscription = models.ForeignKey('Subscription', null=True, related_name='new_subscription', on_delete=models.CASCADE)
    """We remove old_subscription (if not `None`) automatically when new subscription is created.
    
    The new payment may be either one-time (:class:`SimpleItem` (usually :class:`ProlongItem`))
    or subscription (:class:`SubscriptionItem`)."""

    def __repr__(self):
        return "<Item pk=%d, %s>" % (self.pk, self.product.name)

    def __str__(self):
        return self.product.name

    @abc.abstractmethod
    def is_subscription(self):
        pass
    """Is this a recurring (or one-time) payment."""

    @transaction.atomic
    def upgrade_subscription(self):
        """Internal.

        It cancels the old subscription (if any).

        It can be called from both subscription IPN and payment IPN, so prepare to handle it two times."""
        if self.old_subscription:
            self.do_upgrade_subscription()

    def do_upgrade_subscription(self):
        """Internal.

        TODO: Remove ALL old subscriptions as in payment_system2."""
        try:
            self.old_subscription.force_cancel(is_upgrade=True)
        except CannotCancelSubscription:
            pass
        # self.on_upgrade_subscription(transaction, item.old_subscription)  # TODO: Needed?
        self.old_subscription = None
        self.save()

    def send_rendered_email(self, template_name, subject, data):
        """Internal."""
        try:
            self.email = self.subscription.email
        except AttributeError:
            return
        if self.email is None:  # hack!
            return
        self.save()
        html = render_to_string(template_name, data, request=None, using=None)
        text = html2text.HTML2Text(html)
        send_mail(subject, text, settings.FROM_EMAIL, [self.email], html_message=html)

class SimpleItem(Item):
    """Non-subscription item.

    To sell a non-subscription item, create a subclass of this model, describing your sold good."""

    paid = models.BooleanField(default=False)
    """It was paid by the user."""

    def is_subscription(self):
        return False

    def is_paid(self):
        return (self.paid or self.gratis) and not self.blocked
    """If to consider the item paid (or gratis) but not blocked."""


class SubscriptionItem(Item):
    """Subscription (recurring) item.

    To sell a subscription item, create a subclass of this model, describing your sold service."""

    item = models.OneToOneField(Item, related_name='subscriptionitem', parent_link=True, on_delete=models.CASCADE)

    active_subscription = models.OneToOneField('Subscription', null=True, on_delete=models.CASCADE)
    """The :class:`Subscription` currently active for this item
    
    or `None` if the item is not available for the user."""

    due_payment_date = models.DateField(default=datetime.date.today, db_index=True)
    """The reference payment date."""

    payment_deadline = models.DateField(null=True, db_index=True)  # may include "grace period"
    """The dealine payment date.
    
    After it is reached, the item is considered inactive."""

    last_payment = models.DateField(null=True, db_index=True)
    """When the last payment for this item was received.
    
    May be `None` if there were no payments for this item, yet."""

    trial = models.BooleanField(default=False, db_index=True)
    """Now in trial period."""

    grace_period = Period(unit=Period.UNIT_DAYS, count=20)
    """How much :attr:`payment_deadline` is above :attr:`due_payment_data`."""

    payment_period = Period(unit=Period.UNIT_MONTHS, count=1)
    """How often to pay (for automatic recurring payments)."""

    trial_period = Period(unit=Period.UNIT_MONTHS, count=0)
    """Trial period.
    
    It may be zero."""

    # https://bitbucket.org/arcamens/django-payments/wiki/Invoice%20IDs
    subinvoice = models.PositiveIntegerField(default=1)  # no need for index, as it is used only at PayPal side
    """Internal."""

    def is_subscription(self):
        return True

    def is_active(self):
        """Is the item active (paid on time and not blocked).

        Usually you should use quick_is_active() instead because that is faster."""
        prior = self.payment_deadline is not None and \
                datetime.date.today() <= self.payment_deadline
        return (prior or self.gratis) and not self.blocked

    @staticmethod
    def quick_is_active(item_id):
        """Is the item with given PK active (paid on time and not blocked).

        Usually you should use quick_is_active() instead because that is faster."""
        item = SubscriptionItem.objects.filter(pk=item_id).\
            only('payment_deadline', 'gratis', 'blocked').get()
        return item.is_active()

    def set_payment_date(self, date):
        """Sets both :attr:`due_payment_date` and :attr:`payment_deadline`."""
        self.due_payment_date = date
        self.payment_deadline = PayPalUtils.calculate_date(self.due_payment_date, self.grace_period)

    def start_trial(self):
        """Start trial period.

        This should be called after setting non-zero :attr:`trial_period`."""
        if self.trial_period.count != 0:
            self.trial = True
            self.set_payment_date(PayPalUtils.calculate_date(datetime.date.today(), self.trial_period))

    def cancel_subscription(self):
        """Called when we detect that the subscription was canceled."""
        # atomic operation
        SubscriptionItem.objects.filter(pk=self.pk).update(active_subscription=None,
                                                           subinvoice=F('subinvoice') + 1)
        if not self.old_subscription:  # don't send this email on plan upgrade
            self.cancel_subscription_email()

    def cancel_subscription_email(self):
        """Internal.

        Sends cancel subscription email."""
        url = settings.PAYMENTS_HOST + reverse(settings.PROLONG_PAYMENT_VIEW, args=[self.pk])
        days_before = (self.due_payment_date - datetime.date.today()).days
        self.send_rendered_email('debits/email/subscription-canceled.html',
                                 _("Service subscription canceled"),
                                 {'self': self,
                                  'product': self.product.name,
                                  'url': url,
                                  'days_before': days_before})

    @staticmethod
    def send_reminders():
        """Send all email reminders."""
        SubscriptionItem.send_regular_reminders()
        SubscriptionItem.send_trial_reminders()

    @staticmethod
    def send_regular_reminders():
        """Internal."""
        # start with the last
        SubscriptionItem.send_regular_before_due_reminders()
        SubscriptionItem.send_regular_due_reminders()
        SubscriptionItem.send_regular_deadline_reminders()

    @staticmethod
    def send_regular_before_due_reminders():
        """Internal."""
        days_before = settings.PAYMENTS_DAYS_BEFORE_DUE_REMIND
        reminder_date = datetime.date.today() + datetime.timedelta(days=days_before)
        q = SubscriptionItem.objects.filter(reminders_sent__lt=3, due_payment_date__lte=reminder_date, trial=False)
        for transaction in q:
            transaction.reminders_set = 3
            transaction.save()
            url = reverse(settings.PROLONG_PAYMENT_VIEW, args=[transaction.pk])
            transaction.send_rendered_email('debits/email/before-due-remind.html',
                                            _("You need to pay for %s") % transaction.product.name,
                                            {'transaction': transaction,
                                             'product': transaction.product.name,
                                             'url': url,
                                             'days_before': days_before})

    @staticmethod
    def send_regular_due_reminders():
        """Internal."""
        reminder_date = datetime.date.today()
        q = SubscriptionItem.objects.filter(reminders_sent__lt=2, due_payment_date__lte=reminder_date, trial=False)
        for transaction in q:
            transaction.reminders_set = 2
            transaction.save()
            url = reverse(settings.PROLONG_PAYMENT_VIEW, args=[transaction.pk])
            transaction.send_rendered_email('debits/email/due-remind.html',
                                            _("You need to pay for %s") % transaction.product.name,
                                            {'transaction': transaction,
                                             'product': transaction.product.name,
                                             'url': url})

    @staticmethod
    def send_regular_deadline_reminders():
        """Internal."""
        reminder_date = datetime.date.today()
        q = SubscriptionItem.objects.filter(reminders_sent__lt=1, payment_deadline__lte=reminder_date, trial=False)
        for transaction in q:
            transaction.reminders_set = 1
            transaction.save()
            url = reverse(settings.PROLONG_PAYMENT_VIEW, args=[transaction.pk])
            transaction.send_rendered_email('debits/email/deadline-remind.html',
                                            _("You need to pay for %s") % transaction.product.name,
                                            {'transaction': transaction,
                                             'product': transaction.product.name,
                                             'url': url})

    @staticmethod
    def send_trial_reminders():
        """Internal."""
        # start with the last
        SubscriptionItem.send_trial_before_due_reminders()
        SubscriptionItem.send_trial_due_reminders()
        SubscriptionItem.send_trial_deadline_reminders()

    @staticmethod
    def send_trial_before_due_reminders():
        """Internal."""
        days_before = settings.PAYMENTS_DAYS_BEFORE_TRIAL_END_REMIND
        reminder_date = datetime.date.today() + datetime.timedelta(days=days_before)
        q = SubscriptionItem.objects.filter(reminders_sent__lt=3, due_payment_date__lte=reminder_date, trial=True)
        for transaction in q:
            transaction.reminders_set = 3
            transaction.save()
            url = reverse(settings.PROLONG_PAYMENT_VIEW, args=[transaction.pk])
            transaction.send_rendered_email('debits/email/before-due-remind.html',
                                            _("You need to pay for %s") % transaction.product.name,
                                            {'transaction': transaction,
                                             'product': transaction.product.name,
                                             'url': url,
                                             'days_before': days_before})

    @staticmethod
    def send_trial_due_reminders():
        """Internal."""
        reminder_date = datetime.date.today()
        q = SubscriptionItem.objects.filter(reminders_sent__lt=2, due_payment_date__lte=reminder_date, trial=True)
        for transaction in q:
            transaction.reminders_set = 2
            transaction.save()
            url = reverse(settings.PROLONG_PAYMENT_VIEW, args=[transaction.pk])
            transaction.send_rendered_email('debits/email/due-remind.html',
                                            _("You need to pay for %s") % transaction.product.name,
                                            {'transaction': transaction,
                                             'product': transaction.product.name,
                                             'url': url})

    @staticmethod
    def send_trial_deadline_reminders():
        """Internal."""
        reminder_date = datetime.date.today()
        q = SubscriptionItem.objects.filter(reminders_sent__lt=1, payment_deadline__lte=reminder_date, trial=True)
        for transaction in q:
            transaction.reminders_set = 1
            transaction.save()
            url = reverse(settings.PROLONG_PAYMENT_VIEW, args=[transaction.pk])
            transaction.send_rendered_email('debits/email/deadline-remind.html',
                                            _("You need to pay for %s") % transaction.product.name,
                                            {'transaction': transaction,
                                             'product': transaction.product.name,
                                             'url': url})

    # TODO
    # def get_email(self):
    #     try:
    #         # We get the first email, as normally we have no more than one non-canceled transaction
    #         t = self.transactions.filter(subscription__canceled=False)[0]
    #         payment = AutomaticPayment.objects.filter(transaction=t).order_by('-id')[0]
    #         return payment.email
    #     except IndexError:  # no object
    #         return None


class ProlongItem(SimpleItem):
    """Prolong :attr:`parent` item.

    This is meant to be a one-time payment which prolongs a manual subscription item."""

    # item = models.OneToOneField('SimpleItem', related_name='prolongitem', parent_link=True)
    parent = models.ForeignKey('SubscriptionItem', related_name='child', parent_link=False, on_delete=models.CASCADE)
    """Which subscription item to prolong."""

    prolong = Period(unit=Period.UNIT_MONTHS, count=0)
    """The amount of days (or weeks, months, etc.) how much to prolong.
    
    TODO: rename."""

    def refund_payment(self):
        """Handle payment refund.

        For :class:`ProlongItem` we subtract the prolong days back from the :attr:`parent` item."""
        prolong2 = self.prolong
        prolong2.count *= -1
        self.parent.set_payment_date(PayPalUtils.calculate_date(self.parent.due_payment_date, prolong2))
        self.parent.save()


class Subscription(models.Model):
    """Created when the user subscribes for automatic payment.

    This is created by an IPN."""

    transaction = models.OneToOneField('SubscriptionTransaction', on_delete=models.CASCADE)
    """The transaction we accepted."""

    subscription_reference = models.CharField(max_length=255, null=True)  #
    """As `recurring_payment_id` in PayPal.
    
    Avangate has it for every product, but PayPal for transaction as a whole.
    So have it both in :class:`AutomaticPayment` and :class:`Subscription`.
    """

    email = models.EmailField(null=True)
    """User's email.
    
    Duplicates email in :class:`Payment`.
    
    DalPay requires to notify the customer 10 days before every payment."""

    # TODO: The same as in do_upgrade_subscription()
    #@shared_task  # PayPal tormoz, so run in a separate thread # TODO: celery (with `TypeError: force_cancel() missing 1 required positional argument: 'self'`)
    def force_cancel(self, is_upgrade=False):
        """Cancels the :attr:`transaction`."""
        if self.subscription_reference:
            klass = model_from_ref(self.transaction.processor.api)
            api = klass()
            try:
                api.cancel_agreement(self.subscription_reference, is_upgrade=is_upgrade)  # may raise an exception
            except CannotCancelSubscription:
                # fallback
                Subscription.objects.filter(pk=self.pk).update(subscription_reference=None)
                logger.warn("Cannot cancel subscription " + self.subscription_reference)
            # transaction.cancel_subscription()  # runs in the callback


class Payment(models.Model):
    """Base class describing a particular payment.

    It generated by our IPN handler."""

    email = models.EmailField(null=True)
    """User's email.

    Duplicates email in :class:`Subscription`.

    DalPay requires to notify the customer 10 days before every payment."""

    def refund_payment(self):
        """Handles payment refund."""
        try:
            self.transaction.item.prolongitem.refund_payment()
        except ObjectDoesNotExist:
            pass


class SimplePayment(Payment):
    """Non-recurring payment."""

    transaction = models.OneToOneField('SimpleTransaction', on_delete=models.CASCADE)
    """The transaction in response to which the payment happened."""


class AutomaticPayment(Payment):
    """Automatic (recurring) payment."""

    transaction = models.ForeignKey('SubscriptionTransaction', on_delete=models.CASCADE)
    """The transaction in response to which the payment happened."""

    # subscription = models.ForeignKey('Subscription')

    # curr = models.CharField(max_length=3, default='USD')

    # A transaction should have a code that identifies it.
    # code = models.CharField(max_length=255)


class CannotCancelSubscription(Exception):
    """Canceling subscription failed."""
    pass

class CannotRefundSubscription(Exception):
    """Refunding subscription failed."""
    pass
