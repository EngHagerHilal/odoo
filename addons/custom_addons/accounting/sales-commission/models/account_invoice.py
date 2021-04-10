# See LICENSE file for full copyright and licensing details.
from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta
from datetime import date



class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    commission = fields.Float(
        string="Commissions",
        compute="compute_commission",
        default=0,
    )
    deadline = fields.Datetime(string="Deadline" , readOnly = True , compute="compute_deadline")
    payment_date = fields.Date(string="payment date" , readOnly = True , compute="compute_payment_date")

    
    def compute_deadline(self):
        date = self.date_invoice
        x2 = self.date_invoice
        if date.day == 1 or date.day == 2 or date.day == 3 or date.day == 4 :
            x2 = datetime(date.year, date.month , 5)
        else :
            if date.month != 12:
                x2 = datetime(date.year, date.month+1 , 5)
            else :
                x2 = datetime(date.year+1, 1 , 5)
        self.deadline = x2
    
    def compute_payment_date(self):
        if (self.move_id):
            self.payment_date = self.date_invoice
            for move in self.move_id :
                if  move.date > self.payment_date :
                    self.payment_date = move.date
                
   
    def compute_commission(self) :
        if (self.state == 'paid'):
                if ( self.payment_date < self.deadline.date()):
                    if (self.payment_date - self.date_invoice).days <= 1 :
                        if self.invoice_line_ids :
                            count = 0
                            diff = 0
                            for line in self.invoice_line_ids :
                                if line.product_id.categ_id.commission :
                                    count = count + line.quantity
                                if line.product_id.public_price < line.price_unit and line.product_id.public_price != 0 :
                                    diff = line.quantity * line.price_unit - line.quantity * line.product_id.public_price 
                                self.commission = count * line.product_id.categ_id.super_commission_rate + diff / 2
                    else :
                        if self.invoice_line_ids :
                             count = 0
                             for line in self.invoice_line_ids :
                                 if line.product_id.categ_id.commission :
                                    count = count + line.quantity
                                 if line.product_id.public_price < line.price_unit and line.product_id.public_price != 0 :
                                    diff = line.quantity * line.price_unit - line.quantity * line.product.public_price 
                                 self.commission = count * line.product_id.categ_id.default_commission_rate + diff / 2
        else :
            self.commission = 0
        self.x_sale_agent.commissions = self.commission    

