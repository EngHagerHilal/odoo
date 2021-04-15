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
    sale_agent = fields.Many2one(comodel_name='hr.employee', domain=[('job_id.name', '=', 'مندوب مبيعات')],delegate=True)
    deadline = fields.Datetime(string="Deadline" , readOnly = True , compute="compute_deadline")
    payment_date = fields.Date(string="payment date" , readOnly = True , compute="compute_payment_date")
    
    def compute_deadline(self):
        #date = self.date_invoice
        x2 = self.date_invoice
        if (self.date_invoice):
            day = self.date_invoice.day
            month = self.date_invoice.month
            year = self.date_invoice.year
            if( day == 1 or day == 2 or day == 3 or day == 4) :
                x2 = datetime(year, month , 5 , 00,00,00)
            else :
                if month != 12:
                    x2 = datetime(year, month+1 , 5, 00,00,00)
                else :
                    x2 = datetime(year+1, 1 , 5, 00,00,00)
        self.deadline = x2
    
    def compute_payment_date(self):
        if (self.move_id):
            payment = self.date_invoice
            for move in self.move_id :
                if  move.date > payment :
                    self.payment_date = move.date
    
    @api.multi           
    def compute_commission(self) :
        if (self.state == 'paid'):
                if ( self.compute_payment_date() < self.compute_deadline().date()):
                    if (self.compute_payment_date() - self.date_invoice).days <= 1 :
                        if self.invoice_line_ids :
                            count = 0
                            diff = 0
                            for line in self.invoice_line_ids :
                                if line.product_id.categ_id.commission :
                                    count = count + line.quantity
                                if line.product_id.public_price < line.price_unit and line.product_id.public_price != 0  :
                                    diff = line.quantity * line.price_unit - line.quantity * line.product_id.public_price 
                                self.commission = count * line.product_id.categ_id.super_commission_rate + diff / 2
                                #self.sale_agent.commissions += self.commission 
                    else :
                        if self.invoice_line_ids :
                             count = 0
                             for line in self.invoice_line_ids :
                                 if line.product_id.categ_id.commission :
                                    count = count + line.quantity
                                 if line.product_id.public_price < line.price_unit and line.product_id.public_price != 0 :
                                    diff = line.quantity * line.price_unit - line.quantity * line.product.public_price 
                                 self.commission = count * line.product_id.categ_id.default_commission_rate + diff / 2 
                                 #self.sale_agent.commissions += self.commission  
        else :
            self.commission = 0
        return self.commission

    @api.depends('x_sales')
    def get_sale_agent(self) :
        if self.x_sales : 
            self.sale_agent = self.x_sales[0].x_sale_agent




