# See LICENSE file for full copyright and licensing details.

from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
 
    commissions = fields.Float(string="Commission" , readOnly = True , compute="compute_commissions")
    last_reset = fields.Datetime(string="Last Date" , readOnly = True , required = True , default=datetime.now())
    invoices = fields.One2many(comodel_name='account.invoice', inverse_name='sale_agent')

    
    
    def compute_commissions(self) : 
        com = 0
        for invoice in self.invoices : 
            com += invoice.compute_commission()
        self.commissions = com

                


    
                    



