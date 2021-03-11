# -*- coding: utf-8 -*-
###########################################################################
#
#    @author Xpath Solutions <xpathsolution@gmail.com>
#
###########################################################################
from odoo import models, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        if res:
            self.action_invoice_create()
            for invoice in self.invoice_ids:
                invoice.action_invoice_open()
        return res

