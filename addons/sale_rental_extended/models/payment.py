# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    receiver_id = fields.Many2one('res.partner', string='Receiver')
