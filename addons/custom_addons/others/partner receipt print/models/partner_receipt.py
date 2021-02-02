# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015 Dynexcel (<http://dynexcel.com/>).
#
##############################################################################

import time

from odoo import fields,api,models

class PartnerReceipt(models.TransientModel):

    _name = 'partner.receipt'

    partner_id = fields.Many2one('res.partner', string='Partner', required=True, help='Select Partner for movement')
    

    @api.multi
    def print_report(self, data):
        data = {'partner_id': self.partner_id.id }
        return self.env.ref('partner_receipt_report.partner_receipt_pdf').report_action(self, data=data)
