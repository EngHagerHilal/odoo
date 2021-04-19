# -*- coding: utf-8 -*-

from odoo import fields, api, models


class ResBranch(models.Model):
    _name = "res.branch"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist')
    analytic_tag_id = fields.Many2one('account.analytic.tag', string='Analytic Tags')


