# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_training = fields.Boolean(string='Training ?')
    trainer_ids = fields.Many2many('res.users', 'product_user_rel', 'product_id', 'user_id', string="Trainers")

    is_maintenance = fields.Boolean(string='Maintenance ?')
    maintenance_ids = fields.Many2many('res.users', 'maintenance_user_rel', 'maintenance_id', 'user_id',
                                       string="Maintainers")

