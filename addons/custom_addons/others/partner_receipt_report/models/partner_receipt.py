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
    
    date = fields.Date(string='Date', required=True)
    from_account = fields.Many2one('account.account', string='From Account', required=True)
    to_account = fields.Many2one('account.account', string='To Account', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, help='Select Partner for movement')
    amount = fields.Float(string='Amount', default=0.0)
    
    @api.multi
    def print_report(self, data):
        data = {'partner_id': self.partner_id.id ,'date': self.date , 'amount' : self.amount , 'from' : self.from_account , 'to': self.to_account  }
        return self.env.ref('partner_receipt_report.partner_receipt').report_action(self, data=data)
