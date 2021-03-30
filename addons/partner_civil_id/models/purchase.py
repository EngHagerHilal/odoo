# See LICENSE file for full copyright and licensing details.

from odoo import api ,fields, models
from openerp.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    civil_id = fields.Char(string="Civil ID" , size=12, required=True)
    name = fields.Text(string="Name")
    phone = fields.Char(string="Phone Number" , size=8 , required = True)
 

    @api.constrains('civil_id')
    def _check_something(self):
        for record in self:
            if len(record.civil_id) < 12 or len (record.civil_id) > 12:
                raise ValidationError("Civil ID mush be 12 character length!")

