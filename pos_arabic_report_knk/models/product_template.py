# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"
    arabic_name = fields.Char(compute='get_product_arabic_name')

    def get_product_arabic_name(self):
        for product in self:
            product.arabic_name = product.with_context(lang='ar_001').display_name
