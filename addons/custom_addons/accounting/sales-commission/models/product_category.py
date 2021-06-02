from odoo import fields, models

class ProductCategory(models.Model):
    _inherit = 'product.category'

    commission = fields.Boolean(string="commission",
                                     default=False)
    default_commission_rate = fields.Float(string="default rate of commission" , digits=(10, 5))
    super_commission_rate = fields.Float(string="super commission rate" , digits=(10, 5))

    del_commission = fields.Boolean(string="Delivery Commission", default=False)
    del_standard = fields.Integer(string="Standard")
    del_rate = fields.Float(string="Delivery Commission Rate" , digits=(10, 5))
