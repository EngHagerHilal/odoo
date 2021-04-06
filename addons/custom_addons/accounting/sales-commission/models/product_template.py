
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    commission = fields.Boolean(string="Free of commission",
                                     default=False)
    commission_type = fields.Selection(
        [('default', 'Default'),
         ('extra', 'Extra')], string='Product Commission Status')
