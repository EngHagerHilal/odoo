# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class res_partner(models.Model):
    _inherit = "res.partner"

class hr_employee(models.Model):
    _inherit = "hr.employee"
