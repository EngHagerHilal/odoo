# See LICENSE file for full copyright and licensing details.
from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta
from datetime import date , time



class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    sale_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sale Order',
        readonly=True,
        compute = "compute_sale_order"
    )

    @api.depends('origin')
    def compute_sale_order(self):
        for invoice in self:
            if invoice.type in ['in_invoice', 'in_refund']:
                sale = self.env['sale.order'].search([('name' , '=' , invoice.origin)])
                invoice.sale_id = sale[0]



