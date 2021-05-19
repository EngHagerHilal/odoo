# See LICENSE file for full copyright and licensing details.


from odoo import api, models, _
from odoo.exceptions import UserError
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    number = fields.Char(string='Number')
    
    _sql_constraints = [('uniq_name', 'unique(number)', "The number of the Sale Order must be unique !")]


