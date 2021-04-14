# See LICENSE file for full copyright and licensing details.

from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
 
    commissions = fields.Float(string="Commission" , readOnly = True )
    last_reset = fields.Datetime(string="Last Date" , readOnly = True , required = True , default=datetime.now())
    invoices = fields.One2many(comodel_name='account.invoice', inverse_name='sale_agent')

    
    
    #def compute_commissions(self) : 
     #   invoices = self.env['account.invoice'].search([('x_sale_agent.id' , '=' , self.id)])
      #  com = 0 
       # for invoice in invoices : 
        #    com += invoice.commission
        #self.commissions = com
                    
                


    




