from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    public_price = fields.Float(string="Public Price" , compute="compute_public_price")

    def compute_public_price(self) :
        if self.pricelist_item_ids : 
            for list in self.pricelist_item_ids :
                if list.x_default :
                    self.public_price = list.price

