# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    branch_id = fields.Many2one('res.branch', string='Branch')

    @api.multi
    @api.constrains('ref')
    def _check_ref(self):
        for partner in self:
            if partner.ref:
                domain = [
                    ('id', '!=', partner.id),
                    ('ref', '=', partner.ref),
                ]
                other = self.search(domain)
                if other and self.env.context.get("active_test", True):
                    raise ValidationError(_("This reference is equal to partner '%s'") % other[0].display_name)

