import sys
import uuid

from django.db import models, transaction
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import models as base


class PartnerAccount(base.BaseModel):
    partner = models.OneToOneField(base.ResPartner, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=20, unique=True)
    balance = models.FloatField(default=0.0, verbose_name='Current balance')

    class Meta:
        db_table = 'partner_account'

    def __str__(self):
        return self.name

    @classmethod
    def update_balance(cls, asof, user, partner_id=None, amount=0, action_type=None):
        # try:
        partner_account = cls.objects.select_for_update().get(id=partner_id)
        partner_account.write_date = asof
        partner_account.write_user_id = user
        if action_type == AccountLine.ACTION_TYPE_CREDITED:
            partner_account.balance += amount
        elif action_type == AccountLine.ACTION_TYPE_DEBITED:
            partner_account.balance -= amount
        partner_account.save(update_fields=['write_user', 'write_date', 'amount'])
    # asdf
    # except Exception as e:
    # 	print("error in test", e)
    # 	print("line number of error {}".format(sys.exc_info()[-1].tb_lineno))


class Transaction(base.BaseModel):
    PAYMENT_TYPE_BANK_TRANSFER = 'BANK_TRANSFER'
    PAYMENT_TYPE_CHEQUE = 'CHEQUE'
    PAYMENT_TYPE_CASH = 'CASH'
    PAYMENT_TYPE_NONE = 'NONE'
    PAYMENT_TYPE_CHOICES = (
        (PAYMENT_TYPE_BANK_TRANSFER, 'Bank Transfer'),
        (PAYMENT_TYPE_CHEQUE, 'Cheque'),
        (PAYMENT_TYPE_CASH, 'Cash'),
        (PAYMENT_TYPE_NONE, 'None'),
    )

    amount = models.FloatField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, default=PAYMENT_TYPE_NONE)
    number = models.CharField(max_length=30, unique=True, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='Public Identifier')
    reference = models.CharField(max_length=30, null=True, blank=True)
    notes = models.TextField(null=True)

    class Meta:
        db_table = 'payment_transactions'

    def __str__(self):
        return str(self.uuid)

    @classmethod
    def create(cls, user, asof, amount, payment_method, number, uuid, maintenance_ids, reference=None, notes=None):
        from .maintenance import Maintenance
        assert asof is not None

        if reference is None:
            reference = ''
        if notes is None:
            notes = ''
        # vals = {
        # 	'user': user,
        # 	'amount': self.cleaned_data['amount'],
        # 	'asof': timezone.now(),
        # 	'payment_method': self.cleaned_data['payment_method'],
        # 	'number': self.cleaned_data['number'],
        # 	'reference': self.cleaned_data['reference'],
        # 	'notes': self.cleaned_data['notes'],
        # 	'maintenance_ids': maintenance_ids
        #
        # }
        vals = {
            'amount': amount,
            'payment_method': payment_method, 'number': number, 'uuid': uuid,
            'reference': reference, 'notes': notes,
            'create_date': asof, 'write_date': asof, 'create_user_id': user, 'write_user_id': user
        }
        # create account line

        society = Maintenance.objects.filter(id=maintenance_ids[0]).annotate(
            society_id=F('flat__society__partner__partneraccount'),
        ).values('society_id').first()
        society_id = society.get('society_id')
        owner_id = Maintenance.objects.filter(id=maintenance_ids[0]).annotate(
            owner_id=F('flat__flat_owner__partneraccount'),
        ).order_by('id').values('owner_id').first()

        with transaction.atomic():
            transaction_obj = cls.objects.create(**vals)
            PartnerAccount.update_balance(
                asof, user, partner_id=society_id, amount=amount, action_type=AccountLine.ACTION_TYPE_CREDITED
            )
            AccountLine.create(society_id, amount, AccountLine.ACTION_TYPE_CREDITED, transaction_obj.id, asof, user)
            AccountLine.create(owner_id.get('owner_id'), amount, AccountLine.ACTION_TYPE_DEBITED, transaction_obj.id,
                               asof, user)
            maintenance_obj = Maintenance.objects.filter(id__in=maintenance_ids)
            maintenance_obj.update(state=Maintenance.STATE_TYPE_PAID, paid_date=asof.date(),
                                   transaction_id=transaction_obj.id)
            from . import utils
            transaction_obj.number = 'TRM-' + utils.encode(transaction_obj.id)
            transaction_obj.save()
        print("herere return maintenance")
        return HttpResponseRedirect(reverse('admin:hsm_maintenance_changelist'))


class AccountLine(base.BaseModel):
    ACTION_TYPE_CREDITED = 'CREDITED'
    ACTION_TYPE_DEBITED = 'DEBITED'
    ACTION_TYPE_CHOICES = (
        (ACTION_TYPE_CREDITED, 'CREDITED'),
        (ACTION_TYPE_DEBITED, 'DEBITED'),
    )

    account = models.ForeignKey(PartnerAccount, on_delete=models.PROTECT)
    amount = models.FloatField(null=False, blank=False)
    action_type = models.CharField(max_length=20, choices=ACTION_TYPE_CHOICES)
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)

    # create_user = models.ForeignKey(User, on_delete=models.PROTECT)
    # write_user = models.ForeignKey(User, on_delete=models.PROTECT)
    # create_date = models.DateTimeField(Transaction, on_delete=models.PROTECT)
    # write_date = models.DateTimeField(Transaction, on_delete=models.PROTECT)

    @classmethod
    def create(cls, account, amount, action_type, transaction_id, asof, user):
        vals = {
            'account_id': account, 'amount': amount, 'action_type': action_type, 'transaction_id': transaction_id,
            'create_date': asof, 'write_date': asof, 'create_user_id': user, 'write_user_id': user
        }
        cls.objects.create(**vals)

    class Meta:
        db_table = 'account_lines'
