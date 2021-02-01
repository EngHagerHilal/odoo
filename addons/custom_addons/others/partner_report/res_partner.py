# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class res_partner(models.Model):
    _inherit = "res.partner"

    @api.multi
    def print_partner(self):
        return self.env.ref('partner_report.cash_reciept_report').report_action(self)

