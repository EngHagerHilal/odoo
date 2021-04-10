# See LICENSE file for full copyright and licensing details.
from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    commission = fields.Float(
        string="Commissions",
        compute="compute_commission",
        default=0,
    )
    @api.onchange('state')
    def compute_commission(self) :
        if (self.state == 'paid'):
            if self.write_date >= self.x_sale_agent.last_reset :
                if (self.write_date.date() - self.date_invoice).days <= 1 :
                    if self.invoice_line_ids :
                        count = 0
                        diff = 0
                        for line in self.invoice_line_ids :
                            if line.product_id.categ_id.commission :
                                count = count + line.quantity
                            if line.product_id.public_price < line.price_unit and line.product_id.public_price != 0 :
                                diff = line.quantity * line.price_unit - line.quantity * line.product_id.public_price 
                            self.commission += count * line.product_id.categ_id.super_commission_rate + diff / 2
                else :
                        if self.invoice_line_ids :
                             count = 0
                             for line in self.invoice_line_ids :
                                 if line.product_id.categ_id.commission :
                                    count = count + line.quantity
                                 if line.product_id.public_price < line.price_unit and line.product_id.public_price != 0 :
                                    diff = line.quantity * line.price_unit - line.quantity * line.product.public_price 
                                 self.commission += count * line.product_id.categ_id.default_commission_rate + diff / 2       

