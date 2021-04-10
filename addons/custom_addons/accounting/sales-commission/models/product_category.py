from odoo import fields, models

class ProductCategory(models.Model):
    _inherit = 'product.category'

    commission = fields.Boolean(string="commission",
                                     default=False)
    default_commission_rate = fields.Float(string="default rate of commission")
    super_commission_rate = fields.Float(string="super commission rate")