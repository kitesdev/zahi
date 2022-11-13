# -*- coding: utf-8 -*-

from odoo import fields, models


class POSSession(models.Model):
    _inherit = "pos.session"

    def get_closing_control_data(self):
        res = super(POSSession, self).get_closing_control_data()
        res.update({'is_manager': self.user_has_groups("pos_payment_difference_access.group_pos_payment_difference")})
        return res
