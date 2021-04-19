# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleRental(models.Model):
    _inherit = 'sale.rental'

    start_date = fields.Datetime(related='start_order_line_id.start_date', readonly=True, store=True)
