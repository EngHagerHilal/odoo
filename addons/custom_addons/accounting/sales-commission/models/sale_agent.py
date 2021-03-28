# See LICENSE file for full copyright and licensing details.

from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta


class SaleAgent(models.Model):
    _inherit = 'hr.employee'

    commisions = fields.Float(string="Commision" , readOnly = True, compute='compute_commision')
    last_reset = fields.DateTime(string="Last Date" , readOnly = True , required = True , default=now())
    def compute_commision(self):
        invoices = self.env['account.invoice']
        comm = 0 
        for record in self:
            for invoice in invoices :
                if invoice.sale_agent ==  record :
                    if invoice.state == 'Paid' :
                        if invoice.__last_update >= self.last_reset :
                            if (invoice.__last_update - invoice.create_date).days == 1 :
                                if invoice.invoice_line_ids :
                                    count = 0 
                                    for line in invoice.invoice_line_ids :
                                        if "بل" in line.product_id.name :
                                            count = count + line.quantity 
                                comm = comm + ( count // 1000 ) * 12
                            else :
                                if (invoice.__last_update - invoice.create_date).days <= 30 :
                                    if invoice.invoice_line_ids :
                                        count = 0 
                                        for line in invoice.invoice_line_ids :
                                            if "بل" in line.product_id.name :
                                                count = count + line.quantity 
                                    comm = comm + ( count // 1000 ) * 10
        self.commisions = comm
    
                                
                            






