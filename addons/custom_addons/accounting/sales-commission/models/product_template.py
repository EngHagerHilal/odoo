from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    public_price = fields.Float(string="Public Price" , compute="compute_public_price")

    def compute_public_price(self) :
        if self.pricelist_id : 
            for list in self.pricelist_id :
                if list.x_default :
                    for item in list :
                        self.public_price = list.item.price

