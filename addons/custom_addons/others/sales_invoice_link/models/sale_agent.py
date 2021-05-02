# See LICENSE file for full copyright and licensing details.

from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
 
    commissions = fields.Float(string="Commission" , readOnly = True ,compute="compute_commissions")
    #last_reset = fields.Datetime(string="Last Date" , readOnly = True , required = True , default=datetime.now())
    invoices = fields.One2many(comodel_name='account.invoice', store = True, delegate=True,inverse_name='sale_agent')
    
    def compute_commissions(self) :
        com = 0
        if self.invoices :
            for invoice in self.invoices :
                com += invoice.commission
        if self.x_transfers :
            for transfer in self.x_transfers :
                com += transfer.compute_commission()
        self.commissions = com
        return self.commissions

    #def commissions( self , start , end) :
     #   com = 0 
      #  for invoice in self.invoices :
       #     if invoice.compute_payment_date() >= start and invoice.compute_payment_date() <= end :
        #        com += invoice.compute_commission()
        #return com
        


    


                


    
                    



