# -*- coding: UTF-8 -*-
# Copyright 2013-2017 Luc Saffre
# License: BSD (see file COPYING for details)


"""See :doc:`/specs/vat`.

.. autosummary::
   :toctree:

    utils

.. fixtures.novat fixtures.euvatrates

"""

from django.utils.translation import ugettext_lazy as _
from lino.api import ad
import six

class Plugin(ad.Plugin):
    """The :class:`Plugin <lino.core.plugin.Plugin>` object for this
    plugin.

    """
    verbose_name = _("VAT")

    needs_plugins = ['lino_xl.lib.countries', 'lino_xl.lib.ledger']

    default_vat_regime = 'normal'
    """The default VAT regime. If this is specified as a string, Lino will
    resolve it at startup into an item of :class:`VatRegimes
    <lino_xl.lib.vat.VatRegimes>`.

    """

    default_vat_class = 'normal'
    """The default VAT class. If this is specified as a string, Lino will
    resolve it at startup into an item of :class:`VatClasses
    <lino_xl.lib.vat.VatClasses>`.

    """

    def get_vat_class(self, tt, item):
        """Return the VAT class to be used for given trade type and given
        invoice item. Return value must be an item of
        :class:`lino_xl.lib.vat.VatClasses`.

        """
        return self.default_vat_class

    def on_site_startup(self, site):
        vat = site.modules.vat
        if isinstance(self.default_vat_regime, six.string_types):
            self.default_vat_regime = vat.VatRegimes.get_by_name(
                self.default_vat_regime)
        if isinstance(self.default_vat_class, six.string_types):
            self.default_vat_class = vat.VatClasses.get_by_name(
                self.default_vat_class)

    def setup_reports_menu(self, site, user_type, m):
        mg = site.plugins.accounts
        # mg = site.plugins.vat
        # mg = self
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('vat.PrintableInvoicesByJournal')
        m.add_action('vat.IntracomPurchases')
        m.add_action('vat.IntracomSales')
        

    def setup_explorer_menu(self, site, user_type, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('vat.VatAreas')
        m.add_action('vat.VatRegimes')
        m.add_action('vat.VatClasses')
        m.add_action('vat.VatColumns')
        m.add_action('vat.Invoices')
        m.add_action('vat.VatRules')
        # m.add_action('vat.InvoiceItems')

