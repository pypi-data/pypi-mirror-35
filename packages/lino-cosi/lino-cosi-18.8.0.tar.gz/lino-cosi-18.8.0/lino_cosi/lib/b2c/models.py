# -*- coding: UTF-8 -*-
# Copyright 2014-2015 Luc Saffre
# License: BSD (see file COPYING for details)


"""
Database models for `lino_cosi.lib.b2c`.

"""

from __future__ import unicode_literals
import logging
import glob
import os
from django.db import models
from django.core.exceptions import MultipleObjectsReturned, ValidationError
from django.utils import translation
from django.utils.encoding import force_text
from lino.api import dd, _, rt
from etgen.html import E
from lino.utils import join_elems

from lino_xl.lib.sepa.fields import IBANField, BICField
from .camt import CamtParser
from .febelfin import code2desc

logger = logging.getLogger(__name__)


class ImportStatements(dd.Action):
    """Import the .xml files found in the directory specified at
    :attr:`import_statements_path
    <lino_cosi.lib.b2c.Plugin.import_statements_path>`.

    End-users invoke this via the menu command :menuselection:`SEPA
    --> Import SEPA`.

    When a file has been successfully imported, Lino deletes it.

    It might happen that an .xml file accidentally gets downloaded a
    second time. Lino does not create these statements again.

    """
    label = _("Import SEPA")
    http_method = 'POST'
    select_rows = False

    def get_view_permission(self, user_type):
        """Make it invisible when :attr:`import_statements_path
        <lino_cosi.lib.b2c.Plugin.import_statements_path>` is empty.

        """
        if not dd.plugins.b2c.import_statements_path:
            return False
        return super(ImportStatements, self).get_view_permission(user_type)

    def run_from_ui(self, ar):
        pth = dd.plugins.b2c.import_statements_path
        if not pth:
            msg = "No import_statements_path configured."
            return ar.error(msg, alert=_("Error"))
        self.new_statements = 0
        self.updated_statements = 0
        self.failed_statements = 0
        self.imported_files = 0
        dd.logger.info("Importing all XML files from %s...", pth)
        wc = os.path.join(pth, '*.[Xx][Mm][Ll]')
        for filename in glob.iglob(wc):
            self.import_file(ar, filename)

        msg = "{0} XML files with {1} new and {2} updated " \
              "statements have been imported."
        msg = msg.format(
            self.imported_files, self.new_statements, self.updated_statements)
        dd.logger.info(msg)
        return ar.success(msg, alert=_("Success"))

    def import_file(self, ar, filename):
        """Import the named file, which must be a CAMT053 XML file."""
        dd.logger.info("Importing file %s ...", filename)
        Account = rt.models.b2c.Account
        parser = CamtParser()
        data_file = open(filename, 'rb').read()
        # imported_statements = 0
        self.imported_files += 1
        failed_statements = 0
        for stmt in parser.parse(data_file):
            iban = stmt.local_account
            if iban is None:
                dd.logger.warning("Statement %s has no IBAN", stmt)
                failed_statements += 1
                continue
            try:
                unique_id = stmt.unique_id
            except Exception as e:
                dd.logger.warning("Statement %s : %s", stmt, e)
                failed_statements += 1
                continue

            # get or create the Account
            key = dict(iban=iban)
            data = dict(
                owner_name=stmt.owner_name,
                account_name=stmt.account_name)
            try:
                account = Account.objects.get(**key)
                for k, v in data.items():
                    if v:
                        setattr(account, k, v)
            except Account.DoesNotExist:
                key.update(data)
                account = Account(**key)
                account.full_clean()
                account.save()
            except MultipleObjectsReturned:
                dd.logger.warning(
                    "Found more than one account with IBAN %s", iban)
                failed_statements += 1
                continue

            # get or create the Statement
            key = dict(account=account, statement_number=unique_id)
            data = dict(
                start_date=stmt.start_date,
                end_date=stmt.end_date,
                balance_end=stmt.end_balance,
                balance_start=stmt.start_balance,
                local_currency=stmt.local_currency)

            try:
                s = Statement.objects.get(**key)
                for k, v in data.items():
                    setattr(s, k, v)
                transactions_to_update = True
                self.updated_statements += 1
            except Statement.DoesNotExist:
                data.update(key)
                s = Statement(**data)
                self.new_statements += 1
                transactions_to_update = False
            try:
                s.full_clean()
                s.save()
            except ValidationError as e:
                dd.logger.warning("Failed to save statement %s : %s", s, e)
                failed_statements += 1
                continue

            last_transaction = ''
            for mvmt in stmt.transactions:
                last_transaction = max(last_transaction, mvmt.value_date)
                key = dict(statement=s, seqno=mvmt.seqno)
                data = dict(
                    value_date=mvmt.value_date,
                    booking_date=mvmt.booking_date,
                    amount=mvmt.transferred_amount,
                    # partner_name=mvmt.remote_owner or '',
                    remote_account=mvmt.remote_account_iban or
                    mvmt.remote_account_other or '',
                    remote_bic=mvmt.remote_bank_bic or '',
                    message=mvmt.message or '',
                    eref=mvmt.eref or '',
                    remote_owner=mvmt.remote_owner or '',
                    remote_owner_city=mvmt.remote_owner_city or '',
                    remote_owner_postalcode=mvmt.remote_owner_postalcode or '',
                    remote_owner_country_code=mvmt.remote_owner_country_code or '',
                    txcd=mvmt.txcd,
                    txcd_issuer=mvmt.txcd_issuer)
                data.update(
                    remote_owner_address=mvmt.remote_owner_address)

                try:
                    m = Transaction.objects.get(**key)
                    if m.statement != s:
                        raise Exception(
                            "Invalid transaction: statement %s != %s" % (
                                m.statement, s))
                    if not transactions_to_update:
                        dd.logger.warning(
                            "Existing transaction in a new statement?! %s",
                            mvmt)

                    for k, v in data.items():
                        setattr(s, k, v)
                except Transaction.DoesNotExist:
                    data.update(key)
                    m = Transaction(**data)

                try:
                    m.full_clean()
                    m.save()
                except ValidationError as e:
                    dd.logger.warning(
                        "Failed to save transaction %s : %s", s, e)
                    break

            if account.last_transaction != last_transaction:
                account.last_transaction = last_transaction
                account.full_clean()
                account.save()

        if failed_statements > 0:
            dd.logger.warning(
                "%d statements were NOT imported from %s",
                failed_statements, filename)
            self.failed_statements += failed_statements
        elif dd.plugins.b2c.delete_imported_xml_files:
            # Delete imported file if there were no errors
            try:
                os.remove(filename)
            except OSError as err:
                dd.logger.warning("Failed to delete %s : %s", filename, err)
            else:
                dd.logger.info("The file %s has been deleted.", filename)
        else:
            dd.logger.info("File %s was imported but NOT deleted.", filename)


dd.inject_action('system.SiteConfig', import_b2c=ImportStatements())


@dd.python_2_unicode_compatible
class Account(dd.Model):
    """A bank account related to a given :class:`Partner
    <lino.modlib.models.contacts.Partner>`.

    One partner can have more than one bank account.

    .. attribute:: account_name

        Name of the account, as assigned by the account servicing
        institution, in agreement with the account owner in order to
        provide an additional means of identification of the account.
        Usage: The account name is different from the
        :attr:`owner_name`. The account name is used in certain user
        communities to provide a means of identifying the account, in
        addition to the account owner's identity and the account
        number.

    .. attribute:: owner_name

        Name by which a party is known and which is usually used to
        identify that party.

    """

    class Meta:
        app_label = 'b2c'
        abstract = dd.is_abstract_model(__name__, 'Account')
        verbose_name = _("Imported bank account")
        verbose_name_plural = _("Imported bank accounts")

    iban = IBANField(verbose_name=_("IBAN"), unique=True, blank=False)
    bic = BICField(verbose_name=_("BIC"), blank=True)
    account_name = models.CharField(
        _("Account name"), max_length=70, blank=True)
    owner_name = models.CharField(
        _("Owner name"), max_length=70, blank=True)
    last_transaction = models.DateField(_('Last transaction'), null=True, blank=True)

    def __str__(self):
        return self.iban

    @dd.displayfield(_("Partners"))
    def partners(self, ar):
        if ar is None:
            return ''
        elems = []
        qs = rt.models.sepa.Account.objects.filter(iban=self.iban)
        for obj in qs:
            elems.append(ar.obj2html(obj.partner))
        return E.p(*join_elems(elems, ', '))


PRIMARY_FIELDS = dd.fields_list(Account, 'iban bic')


@dd.python_2_unicode_compatible
class Statement(dd.Model):
    """A bank statement.

    This data is automaticaly imported by :class:`ImportStatements`.

    .. attribute:: sequence_number

        The legal sequential number of the statement, as assigned by
        the bank.

        See `LegalSequenceNumber
        <https://www.iso20022.org/standardsrepository/public/wqt/Content/mx/camt.053.001.02#mx/camt.053.001.02/Statement/LegalSequenceNumber>`_
        (`<LglSeqNb>`) for details.

    .. attribute:: start_date
    .. attribute:: end_date

        Note that year can differ between start_date and end_date for
        the first statement of every year.

    .. attribute:: unique_id

        A virtual field of the form `YYYY/NNNN` where YYYY is taken
        from the :attr:`end_date` and NNNN is taken from
        :attr:`electronic_sequence_number`.

    .. attribute:: electronic_sequence_number

    """

    class Meta:
        app_label = 'b2c'
        abstract = dd.is_abstract_model(__name__, 'Statement')
        verbose_name = _("Statement")
        verbose_name_plural = _("Statements")

    def __str__(self):
        return self.statement_number

    account = dd.ForeignKey('b2c.Account')
    statement_number = models.CharField(
        _('Statement number'), blank=False, max_length=10,
        help_text=_("Combination of the year and the legal sequential number"
                    " of the paper statement."))

    start_date = models.DateField(_('Start date'), null=True)
    end_date = models.DateField(_('End date'), null=True)
    # date_done = models.DateTimeField(_('Import Date'), null=True)
    balance_start = dd.PriceField(_("Initial amount"), null=True)
    balance_end = dd.PriceField(_("Final amount"), null=True)
    # balance_end_real = dd.PriceField(_("Real end balance"), null=True)
    local_currency = models.CharField(_('Currency'), max_length=3)
    # sequence_number = models.IntegerField(
    #     _('Sequence number'), null=True,
    #     help_text=_("The legal sequential number of the paper statement, "
    #                 "as assigned by the account servicer."))

    # fields like statement_number, date, solde_initial, solde_final


class Transaction(dd.Model):
    """A transaction within a bank statement.

    This data is automaticaly imported by :class:`ImportStatements`.


    
    .. attribute:: statement

    .. attribute:: seqno

    .. attribute:: booking_date

    .. attribute:: value_date

    .. attribute:: transfer_type

       The actual historic name of the :attr:`txcd`.

    .. attribute:: txcd

        The Bank Transaction Code (`<BkTxCd>`) or "transfer type".
        Actually it is the "proprietary" part of this code.

    .. attribute:: txcd_issuer

        The issuer or the :attr:`txcd`.

    .. attribute:: txcd_text

        Virtual field with the textual translated description of the
        :attr:`txcd`.  Currently this works only for Belgian codes
        where :attr:`txcd_issuer` is `"BBA"` as defined in
        :mod:`lino_cosi.lib.b2c.febelfin`).

    .. attribute:: remote_account
    .. attribute:: remote_bic
    .. attribute:: remote_owner
    .. attribute:: remote_owner_address
    .. attribute:: remote_owner_city
    .. attribute:: remote_owner_postalcode
    .. attribute:: remote_owner_country_code

    """

    class Meta:
        app_label = 'b2c'
        abstract = dd.is_abstract_model(__name__, 'Transaction')
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    statement = dd.ForeignKey('b2c.Statement')
    seqno = models.IntegerField(_('No.'),
        help_text=_("The sequence number of this transaction in the statement."))
    # unique_import_id = models.CharField(_('Unique import ID'), max_length=128)
    # movement_number = models.CharField(_("Ref of Mov"), null=False, max_length=32)
    # movement_date = models.DateField(_('Movement date'), null=True, blank=True)
    amount = dd.PriceField(_('Amount'), null=True, blank=True)
    # partner = dd.ForeignKey('contacts.Partner', related_name='b2c_movement', null=True)
    # partner_name = models.CharField(_('Partner name'), max_length=35, blank=True)
    remote_account = models.CharField(_("IBAN"), blank=True, max_length=64)
    remote_bic = BICField(verbose_name=_("BIC"), blank=True)
    # ref = models.CharField(_('Ref'), max_length=35, blank=True)
    message = models.TextField(_('Message'), blank=True)
    eref = models.CharField(_('End to end reference'), max_length=128, blank=True)
    remote_owner = models.CharField(_('Remote owner'), max_length=128, blank=True)
    remote_owner_address = models.TextField(
        _('Remote owner adress'), blank=True)
    remote_owner_city = models.CharField(_('Remote owner city'), max_length=32, blank=True)
    remote_owner_postalcode = models.CharField(_('Remote owner postal code'), max_length=10, blank=True)
    remote_owner_country_code = models.CharField(_('Remote owner country code'), max_length=4, blank=True)
    txcd = models.CharField(_('Transfer type'), max_length=32, blank=True)
    txcd_issuer = models.CharField(_('TxCd issuer'), max_length=35, blank=True)
    booking_date = models.DateField(_('Execution date'), null=True, blank=True)
    value_date = models.DateField(_('Value date'), null=True, blank=True)

    @dd.displayfield(_("Remote account"))
    def remote_html(self, ar):
        elems = []
        elems += [self.remote_account, " "]
        elems += ["(BIC:", self.remote_bic, ")"]
        elems.append(E.br())
        elems += [E.b(self.remote_owner), ", "]
        elems.append(E.br())
        elems += [" / ".join(self.remote_owner_address.splitlines()), ", "]
        elems += [self.remote_owner_postalcode, " "]
        elems += [self.remote_owner_city, " "]
        elems += [self.remote_owner_country_code]
        return E.div(*elems)

    @dd.displayfield(_("Message"))
    def message_html(self, ar):
        from django.utils.translation import ugettext as _
        elems = []
        # elems += [_("Date"), dd.fds(self.transaction_date), " "]
        # elems += [_("Amount"), ' ', E.b(unicode(self.amount)), " "]
        # self.booking_date
        elems += self.message  # .splitlines()
        elems.append(E.br())
        # elems += [_("ref:"), ': ', self.ref, ' ']
        elems += [_("eref:"), ': ', self.eref]
        elems.append(E.br())
        elems += [E.b(self.txcd_text), ' ']
        elems += [_("Value date"), ': ', E.b(dd.fds(self.value_date)), " "]
        elems += [_("Booking date"), ': ',
                  E.b(dd.fds(self.booking_date)), " "]
        return E.div(*elems)

    @dd.displayfield(_("BkTxCd"))
    def txcd_text(self, ar):
        if self.txcd_issuer == 'BBA':
            # until we get a list of German translations, users in
            # Eupen prefer FR over EN
            with translation.override('fr'):
                return force_text(code2desc(self.txcd[:4]))
        return "{0}:{1}".format(self.txcd_issuer, self.txcd)
        
from .ui import *
