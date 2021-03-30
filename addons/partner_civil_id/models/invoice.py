# See LICENSE file for full copyright and licensing details.

from odoo import api ,fields, models
from openerp.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'account.invoice'

    civil_id = fields.Char(string="Civil ID" , size=12, related='purchase_id.civil_id')
    name = fields.Text(string="Name" , related='purchase_id.name')
    Phone = fields.Char(string="Phone Number" , size=12 , related='purchase_id.phone')

    @api.constrains('civil_id')
    def _check_something(self):
        for record in self:
            if len(record.civil_id) < 12 or len (record.civil_id) > 12:
                raise ValidationError("Civil ID mush be 12 character length!")

