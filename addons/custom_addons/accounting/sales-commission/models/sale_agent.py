# See LICENSE file for full copyright and licensing details.

from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
 
    commissions = fields.Float(string="Commission" , readOnly = True , compute="compute_commissions")
    last_reset = fields.Datetime(string="Last Date" , readOnly = True , required = True , default=datetime.now())

    def compute_commissions(self) : 
        self.commissions = 0
        self.ensure_one()
        for invoice in self.x_invoices :
            self.commissions += invoice.commission
                        
                


    




