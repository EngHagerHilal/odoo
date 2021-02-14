# See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    number = fields.Char(string='Number')
    
    _sql_constraints = [('uniq_name', 'unique(number)', "The number of the Purchase Order must be unique !")]

