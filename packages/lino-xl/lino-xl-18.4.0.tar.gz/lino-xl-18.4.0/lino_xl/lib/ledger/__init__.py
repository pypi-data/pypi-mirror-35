# -*- coding: UTF-8 -*-
# Copyright 2014-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""This is Lino's standard plugin for General Ledger.
See :doc:`/specs/ledger`.

.. autosummary::
    :toctree:

    roles
    fields
    management.commands.reregister
    fixtures.std
    fixtures.demo
    fixtures.demo_bookings

"""

from __future__ import unicode_literals

import datetime
from django.utils.functional import lazystr

from lino.api import ad, _


class Plugin(ad.Plugin):

    verbose_name = _("Ledger")
    needs_plugins = ['lino_xl.lib.accounts', 'lino.modlib.weasyprint']

    currency_symbol = "€"
    """
    Temporary approach until we add support for multiple
    currencies.
    """
    
    use_pcmn = False
    """
    Whether to use the PCMN notation.

    PCMN stands for "plan compatable minimum normalisé" and is a
    standardized nomenclature for accounts used in France and
    Belgium.

    """
    project_model = None
    """
    Leave this to `None` for normal behaviour.  Set this to a
    string of the form `'<app_label>.<ModelName>'` if you want to
    add an additional field `project` to all models which inherit
    from :class:`lino_xl.lib.ledger.ProjectRelated`.
    """
    
    intrusive_menu = False
    """
    Whether the plugin should integrate into the application's
    main menu in an intrusive way.  Intrusive means that the main
    menu gets one top-level item per journal group.

    The default behaviour is `False`, meaning that these items are
    gathered below a single item "Accounting".
    """
    
    start_year = 2012
    """
    An integer with the calendar year in which this site starts
    working.

    This is used to fill the default list of :class:`FiscalYears`,
    and by certain fixtures for generating demo invoices.
    """
    
    fix_y2k = False
    """
    Whether to use a Y2K compatible representation for fiscal years.
    """
    
    force_cleared_until = None
    """
    Force all movements on vouchers with entry_date until the given
    date to be *cleared*.  This is useful e.g. when you want to keep
    legacy invoices in your database but not their payments.
    """

    def on_site_startup(self, site):
        if site.the_demo_date is not None:
            if self.start_year > site.the_demo_date.year:
                raise Exception(
                    "plugins.ledger.start_year is after the_demo_date")
        FiscalYears = site.modules.ledger.FiscalYears
        today = site.the_demo_date or datetime.date.today()
        for y in range(self.start_year, today.year + 6):
            FiscalYears.add_item(FiscalYears.year2value(y), str(y))

    def setup_main_menu(self, site, user_type, m):
        if not self.intrusive_menu:
            mg = site.plugins.accounts
            m = m.add_menu(mg.app_label, mg.verbose_name)

        Journal = site.models.ledger.Journal
        JournalGroups = site.models.ledger.JournalGroups
        for grp in JournalGroups.objects():
            subm = m.add_menu(grp.name, grp.text)
            for jnl in Journal.objects.filter(
                    journal_group=grp).order_by('seqno'):
                subm.add_action(jnl.voucher_type.table_class,
                                label=lazystr(jnl),
                                params=dict(master_instance=jnl))

    def setup_reports_menu(self, site, user_type, m):
        mg = site.plugins.accounts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        # m.add_action('ledger.Situation')
        # m.add_action('ledger.ActivityReport')
        m.add_action('ledger.AccountingReport')
        # m.add_action('ledger.GeneralAccountBalances')
        # m.add_action('ledger.CustomerAccountBalances')
        # m.add_action('ledger.SupplierAccountBalances')
        m.add_action('ledger.Debtors')
        m.add_action('ledger.Creditors')

    def setup_config_menu(self, site, user_type, m):
        mg = site.plugins.accounts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('ledger.Journals')
        m.add_action('ledger.AccountingPeriods')
        m.add_action('ledger.PaymentTerms')

    def setup_explorer_menu(self, site, user_type, m):
        mg = site.plugins.accounts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('accounts.CommonAccounts')
        m.add_action('ledger.MatchRules')
        m.add_action('ledger.AllVouchers')
        m.add_action('ledger.VoucherTypes')
        m.add_action('ledger.AllMovements')
        m.add_action('ledger.FiscalYears')
        m.add_action('ledger.TradeTypes')
        m.add_action('ledger.JournalGroups')

    def remove_dummy(self, *args):
        lst = list(args)
        if self.project_model is None:
            lst.remove('project')
        return lst

