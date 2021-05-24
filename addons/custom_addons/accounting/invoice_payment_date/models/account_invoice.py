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
            if (record.state == 'paid'):  
                if record.payment_ids :
                        payment = record.payment_ids[0].payment_date
                        for move in record.payment_ids :
                                if  move.payment_date > payment :
                                    payment = move.payment_date
                        record.payment_date = payment
        
