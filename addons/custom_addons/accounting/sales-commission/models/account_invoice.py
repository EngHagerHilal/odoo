# See LICENSE file for full copyright and licensing details.
from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta
from datetime import date , time



class AccountInvoice(models.Model):
    _inherit = 'account.invoice'


    commission = fields.Float( string="Commissions", compute="compute_commission" , store=True, default=0)
    payment_commission = fields.Float( string="Payment Commissions", compute="compute_commission" , store=True, default=0)
    price_commission = fields.Float( string="Price Commissions", compute="compute_commission" , store=True, default=0)
     
    sale_agent = fields.Many2one(comodel_name='hr.employee', related='sale_id.x_sale_agent', readonly=False, states={'paid': [('readonly', True)]} , domain=[('job_id.name', '=', 'مندوب مبيعات')],delegate=True)
    deadline = fields.Datetime(string="Deadline" , readOnly = True , store = True , compute="compute_deadline")
    
    #payment_date = fields.Date(string="payment date" , readOnly = True , store = True , compute="compute_payment_date")
    
    

    @api.depends('date_invoice' )
    def compute_deadline(self):
        for invoice in self :
            if (invoice.date_invoice and invoice.type == 'out_invoice'):
                day = invoice.date_invoice.day
                month = invoice.date_invoice.month
                year = invoice.date_invoice.year
                if( day == 1 or day == 2 or day == 3 or day == 4) :
                    x2 = datetime(year, month , 5 , 00,00,00)
                else :
                    if month != 12:
                        x2 = datetime(year, month+1 , 5, 00,00,00)
                    else :
                        x2 = datetime(year+1, 1 , 5, 00,00,00)
                invoice.deadline = x2
        #return self.deadline
    
    #@api.depends('state' , 'type')
    #def compute_payment_date(self):
     #   for record in self : 
      #      if (record.state == 'paid' and record.type == 'out_invoice'):
       #         payment = record.move_id[0].date
        #        for move in record.move_id :
         #           if  move.date > payment :
          #              payment = move.date
           #     record.payment_date = payment
    @api.multi   
    @api.depends('state' , 'type')
    def compute_commission(self) :
        for record in self :
            if (record.state == 'paid' and record.type == 'out_invoice'):
                payment = record.payment_date
                if ( payment < record.deadline.date()):
                    if (payment - record.date_invoice).days <= 1 :
                        if record.invoice_line_ids :
                            count = 0
                            diff = 0
                            for line in record.invoice_line_ids :
                                if line.product_id.categ_id.commission :
                                    count = count + line.quantity
                                if line.product_id.compute_public_price() < line.price_unit and line.product_id.compute_public_price() != 0  :
                                    diff = line.quantity * line.price_unit - line.quantity * line.product_id.compute_public_price()
                                record.commission = count * line.product_id.categ_id.super_commission_rate + diff / 2
                                record.payment_commission = count * line.product_id.categ_id.super_commission_rate
                                record.price_commission = diff / 2
                            #self.sale_agent.commissions += self.commission 
                    else :
                        if record.invoice_line_ids :
                            count = 0
                            for line in record.invoice_line_ids :
                                if line.product_id.categ_id.commission :
                                    count = count + line.quantity
                                if line.product_id.compute_public_price() < line.price_unit and line.product_id.compute_public_price() != 0 :
                                    diff = line.quantity * line.price_unit - line.quantity * line.product.compute_public_price() 
                                record.commission = count * line.product_id.categ_id.default_commission_rate + diff / 2
                                record.payment_commission = count * line.product_id.categ_id.default_commission_rate
                                record.price_commission = diff / 2 
                            #self.sale_agent.commissions += self.commission  
            else :
                record.commission = 0
                record.payment_commission = 0
                record.price_commission = 0 

    #@api.depends('x_sales')
    #def get_sale_agent(self) :
     #   if self.x_sales : 
      #      self.sale_agent = self.x_sales[0].x_sale_agent




