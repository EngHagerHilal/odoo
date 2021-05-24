# See LICENSE file for full copyright and licensing details.
from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta
from datetime import date , time



class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    payment_date = fields.Date(string="payment date" , readOnly = True , store = True , compute="compute_payment_date")
        

    @api.depends('state' , 'type')
    def compute_payment_date(self):
        for record in self : 
            if (record.state == 'paid' and record.type == 'out_invoice'):                
                payment = record.reverse_entry_id.move_id[0].date
                for move in record.reverse_entry_id.move_id :
                    if  move.date > payment :
                        payment = move.date
                record.payment_date = payment
        
