# -*- coding: UTF-8 -*-
# Copyright 2008-2016 Luc Saffre
# License: BSD (see file COPYING for details)


"""
Database models for `lino_xl.lib.products`.

"""


from django.db import models
from django.utils.translation import ugettext_lazy as _

from lino.api import dd
from lino import mixins

from .choicelists import DeliveryUnit
from .roles import ProductsUser, ProductsStaff

vat = dd.resolve_app('vat')


class ProductCat(mixins.BabelNamed):
    """A **product category** is a way to group products."""

    class Meta:
        app_label = 'products'
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")
        abstract = dd.is_abstract_model(__name__, 'ProductCat')

    description = models.TextField(blank=True)


class ProductCats(dd.Table):
    model = 'products.ProductCat'
    required_roles = dd.login_required(ProductsStaff)
    order_by = ["id"]
    detail_layout = """
    id name
    description
    ProductsByCategory
    """


class Product(mixins.BabelNamed):
    """A product is something you can sell or buy.

    .. attribute:: description
    .. attribute:: cat
    .. attribute:: delivery_unit

    

    """

    class Meta:
        app_label = 'products'
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        abstract = dd.is_abstract_model(__name__, 'Product')

    description = dd.BabelTextField(
        verbose_name=_("Long description"),
        blank=True, null=True)
    cat = dd.ForeignKey(
        ProductCat, verbose_name=_("Category"),
        blank=True, null=True)

    delivery_unit = DeliveryUnit.field(
        default=DeliveryUnit.as_callable('piece'))

    if vat:
        vat_class = vat.VatClasses.field(blank=True)
    else:
        vat_class = dd.DummyField()


class Products(dd.Table):
    required_roles = dd.login_required(ProductsUser)
    model = 'products.Product'
    order_by = ["id"]
    column_names = "id name cat vat_class *"

    insert_layout = """
    cat
    name
    """

    detail_layout = """
    id cat #sales_price vat_class delivery_unit
    name
    description
    """

# note: a Site without sales will have to adapt the detail_layout and
# column_names of Products


class ProductsByCategory(Products):
    master_key = 'cat'


