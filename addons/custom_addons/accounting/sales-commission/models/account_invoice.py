# See LICENSE file for full copyright and licensing details.

from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    commission = fields.Float(
        string="Commissions",
        compute="compute_commission",
        store=True,
    )
    @api.onchange('state')
    def compute_commission(self) :
        if (self.state == 'paid'):
            comm = 0
            if self.write_date >= self.x_sale_agent.last_reset :
                if (self.write_date - self.date_invoice).days == 1 :
                    if self.invoice_line_ids :
                        count = 0
                        for line in self.invoice_line_ids :
                            if line.product_id.commission :
                                count = count + line.quantity         
                        comm = comm + ( count // 1000 ) * 12
                    else :
                        if self.invoice_line_ids :
                             count = 0
                             for line in self.invoice_line_ids :
                                 if line.product_id.commission :
                                     count = count + line.quantity         
                             comm = comm + ( count // 1000 ) * 10
            self.commission = comm
            self.x_sale_agent.commisions = self.x_sale_agent.commisions + self.commission








