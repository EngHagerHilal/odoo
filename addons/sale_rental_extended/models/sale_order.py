# -*- coding: utf-8 -*-

import json
from odoo import fields, api, models, _
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    date_payment = fields.Date(string="Payment Date")
    branch_id = fields.Many2one('res.branch', string='Branch', default=lambda self: self.env.user.branch_id.id)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    discount_fixed = fields.Float(string="Discount (Fixed)", digits=dp.get_precision('Product Price'),
                                  help="Fixed amount discount.")
    amount_extra = fields.Float(string="Amount Extra", digits=dp.get_precision('Product Price'))
    amount_deduct = fields.Float(string="Amount Deduct", digits=dp.get_precision('Product Price'))
    amount_commission = fields.Float(string="Trainer Commission", digits=dp.get_precision('Product Price'))
    responsible_id = fields.Many2one('res.users', string="Responsible")
    responsible_domain = fields.Char(compute="_compute_responsible_domain", readonly=True, store=False)
    maintenance_responsible_id = fields.Many2one('res.users', string="Maintenance Responsible")
    maintenance_responsible_domain = fields.Char(compute="_compute_maintenance_responsible_domain",
                                                 readonly=True, store=False)
    is_training = fields.Boolean(string='Training ?', related='product_id.is_training')
    is_maintenance = fields.Boolean(string='Maintenance ?', related='product_id.is_maintenance')
    start_date = fields.Datetime(string='Start Date', readonly=True, states={'draft': [('readonly', False)]})
    end_date = fields.Datetime(string='End Date', readonly=True, states={'draft': [('readonly', False)]})
    number_of_days = fields.Float(compute='_compute_number_of_days',
                                  string='Number of Days', readonly=False, store=True)

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for rec in self:
            if rec.end_date <= rec.start_date:
                raise ValidationError(_("End Date Must Greater Than Start Date !"))

    @api.depends('start_date', 'end_date')
    def _compute_number_of_days(self):
        for line in self:
            days = False
            if line.start_date and line.end_date:
                days = (line.end_date - line.start_date).days
                print ("days", days)
                if days == 0:
                    seconds = (line.end_date - line.start_date).seconds
                    hours = days * 24 + seconds // 3600
                    line.number_of_days = hours / 24
                elif 14 > int(days) >= 7:
                    line.number_of_days = 7
                elif int(days) >= 14:
                    line.number_of_days = 14
                else:
                    line.number_of_days = days
            else:
                line.number_of_days = 0

    @api.onchange('discount')
    def _onchange_discount_percent(self):
        # _onchange_discount method already exists in core,
        # but discount is not in the onchange definition
        if self.discount:
            self.discount_fixed = 0.0

    @api.onchange('discount_fixed')
    def _onchange_discount_fixed(self):
        if self.discount_fixed:
            self.discount = 0.0

    @api.constrains('discount', 'discount_fixed')
    def _check_only_one_discount(self):
        for line in self:
            if line.discount and line.discount_fixed:
                raise ValidationError(
                    _("You can only set one type of discount per line."))

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id',
                 'discount_fixed', 'amount_extra', 'amount_deduct', 'amount_commission')
    def _compute_amount(self):
        vals = {}
        for line in self.filtered(lambda l: l.discount_fixed or l.amount_extra or l.amount_deduct or l.amount_commission):
            real_price = line.price_unit * (1 - (line.discount + line.amount_deduct - line.amount_extra or 0.0) / 100.0
                                            ) - (line.discount_fixed + line.amount_commission or 0.0)
            twicked_price = real_price / (1 - (line.discount or 0.0) / 100.0)
            vals[line] = {
                'price_unit': line.price_unit,
            }
            line.update({
                'price_unit': twicked_price,
            })
        res = super(SaleOrderLine, self)._compute_amount()
        for line in vals.keys():
            line.update(vals[line])
        return res

    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        res.update({
            'discount_fixed': self.discount_fixed,
            'amount_deduct': self.amount_deduct,
            'amount_extra': self.amount_extra,
            'amount_commission': self.amount_commission,
        })
        return res

    @api.multi
    @api.depends('product_id')
    def _compute_maintenance_responsible_domain(self):
        for rec in self:
            domain = []
            if rec.product_id and rec.product_id.is_maintenance:
                domain = json.dumps([('id', 'in', rec.product_id.maintenance_ids.ids)])
            rec.maintenance_responsible_domain = domain

    @api.multi
    @api.depends('product_id')
    def _compute_responsible_domain(self):
        for rec in self:
            domain = []
            if rec.product_id and rec.product_id.is_training:
                domain = json.dumps([('id', 'in', rec.product_id.trainer_ids.ids)])
            rec.responsible_domain = domain

    @api.constrains('price_unit')
    def check_price_unit(self):
        for rec in self:
            if rec.price_unit <= 0:
                raise ValidationError(_('Unit Price Must Be Non Zero !'))

    @api.onchange('product_uom_qty', 'product_uom', 'route_id')
    def _onchange_product_id_check_availability(self):
        if not self.product_id or not self.product_uom_qty or not self.product_uom:
            self.product_packaging = False
            return {}
        if self.product_id.type == 'product':
            precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
            product = self.product_id.with_context(
                warehouse=self.order_id.warehouse_id.id,
                lang=self.order_id.partner_id.lang or self.env.user.lang or 'en_US'
            )
            product_qty = self.product_uom._compute_quantity(self.product_uom_qty, self.product_id.uom_id)
            if float_compare(product.virtual_available, product_qty, precision_digits=precision) == -1:
                is_available = self._check_routing()
                if not is_available:
                    message = _('You plan to sell %s %s of %s but you only have %s %s available in %s warehouse.') % \
                              (self.product_uom_qty, self.product_uom.name, self.product_id.name,
                               product.virtual_available, product.uom_id.name, self.order_id.warehouse_id.name)
                    if float_compare(product.virtual_available, self.product_id.virtual_available,
                                     precision_digits=precision) == -1:
                        for warehouse in self.env['stock.warehouse'].search([]):
                            quantity = self.product_id.with_context(warehouse=warehouse.id).virtual_available
                            if quantity > 0:
                                message += "%s: %s %s\n" % (warehouse.name, quantity, self.product_id.uom_id.name)
                    raise ValidationError(_('Not enough inventory !'))
        return {}

    @api.onchange('end_date')
    def end_date_change(self):
        return

    @api.onchange('start_date')
    def start_date_change(self):
        return

    @api.onchange('product_id')
    def start_end_dates_product_id_change(self):
        return

    @api.onchange('number_of_days')
    def _inverse_number_of_days(self):
        return