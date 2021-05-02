# See LICENSE file for full copyright and licensing details.
from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta
from datetime import date , time



class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    sale_ids = fields.Many2many(comodel_name='sale.order',
                            relation='sale_invoice_link',
                            column1='invoice_id',
                            column2='sale_order_id')
    sale_id = fields.Many2one(comodel_name='sale.order', delegate=True)



