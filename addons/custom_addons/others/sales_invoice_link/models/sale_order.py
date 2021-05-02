# See LICENSE file for full copyright and licensing details.
from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta
from datetime import date , time



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    invoice_ids = fields.Many2many(comodel_name='account.invoice',
                            relation='sale_invoice_link',
                            column1='sale_order_id',
                            column2='invoice_id')
    invoices = fields.One2many(comodel_name='sale.order', inverse_name='sale_id' , String = 'Invoices')

                            