# See LICENSE file for full copyright and licensing details.

from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
 
    commissions = fields.Float(string="Commission" , readOnly = True )
    last_reset = fields.Datetime(string="Last Date" , readOnly = True , required = True , default=datetime.now())

    #compute="compute_commissions"
    #@api.multi
    #def compute_commissions(self) : 
     #   self.ensure_one()
      #  for record in self : 
       #     record.commissions = 0
        #    for invoice in record.x_invoices :
         #       record.commissions += invoice.commission
                        
                


    




