# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    suspense_account_id = fields.Many2one(
        comodel_name='account.account', check_company=True, ondelete='restrict', readonly=False, store=True,
        compute='_compute_suspense_account_id',
        help="Bank statements transactions will be posted on the suspense account until the final reconciliation "
             "allowing finding the right account.", string='Suspense Account',
        domain="[('deprecated', '=', False), ('company_id', '=', company_id), \
                ('account_type', 'not in', ('asset_receivable', 'liability_payable'))]")
