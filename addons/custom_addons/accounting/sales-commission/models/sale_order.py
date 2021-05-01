# See LICENSE file for full copyright and licensing details.
from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta
from datetime import date , time



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    invoice =  fields.One2many(comodel_name='account.invoice', store = True, delegate=True,inverse_name='sale_order')

    
    