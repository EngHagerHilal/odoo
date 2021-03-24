# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp


class bill_quantity(models.Model):
    _name = 'bill.quantity'
    _inherit = ['mail.thread']
    _rec_name = 'project_id'

    @api.one
    @api.depends('quantity_line')
    def _compute_amount(self):
        material_price_subtotal = 0.0
        labor_price_subtotal = 0.0
        subcontract_price_subtotal = 0.0
        equipment_price_subtotal = 0.0
        work_package_price_subtotal = 0.0
        for record in self.quantity_line:
            if record.key == 'material':
                material_price_subtotal = record.price_subtotal + material_price_subtotal
                self.material_cost = material_price_subtotal
            if record.key == 'labor':
                labor_price_subtotal = record.price_subtotal + labor_price_subtotal
                self.labor_cost = labor_price_subtotal
            if record.key == 'subcontract':
                subcontract_price_subtotal = record.price_subtotal + subcontract_price_subtotal
                self.subcontract_cost = subcontract_price_subtotal
            if record.key == 'work_package':
                work_package_price_subtotal = record.price_subtotal + work_package_price_subtotal
                self.work_package_cost = work_package_price_subtotal

    #        self.revision = 0

    project_id = fields.Many2one(
        'project.project', 'Project', track_visibility='always')
    subcontract_cost = fields.Float(
        'Subcontract Cost', compute='_compute_amount', track_visibility='always')
    revision = fields.Integer(
        'Revision', readonly=True,
    )
    material_cost = fields.Float(
        'Material Cost', compute='_compute_amount',
        readonly=True, store=True,
        digits=dp.get_precision('Account'), )
    labor_cost = fields.Float(
        'Labor Cost', compute='_compute_amount',
        readonly=True, store=True,
        digits=dp.get_precision('Account'), )
    work_package_cost = fields.Float(
        'Work Package Cost', compute='_compute_amount',
        readonly=True, store=True,
        digits=dp.get_precision('Account'), )
    quantity_line = fields.One2many(
        'bill.quantity.line', 'bill_quantity_id',
        string='Bill Of Quantity Lines', readonly=False, copy=True)

    @api.multi
    def create_new_revision(self):
        bill_line = []
        for line in self.quantity_line:
            bill_line.append(
                (0, False, {'product_id': line.product_id.id,
                            'type': line.type,
                            'uom_id': line.uom_id.id,
                            'description': line.description,
                            'qty': line.qty,
                            'bill_quantity_id': self.id,
                            'key': line.key,
                            'employee_id': line.employee_id.id,
                            'product_id': line.product_id.id,
                            'partner_id': line.partner_id.id,
                            'work_package_id': line.work_package_id.id,
                            'price_unit': line.price_unit,
                            'price_subtotal': line.price_subtotal,
                            }))
        vals = {'project_id': self.project_id.id,
                'quantity_line': bill_line
                }
        res = self.create(vals)
        res.revision = self.revision + 1


class bill_quantity_line(models.Model):
    _name = 'bill.quantity.line'
    _description = 'Bill Of Quantity Line'

    @api.one
    @api.depends('price_unit', 'qty', 'product_id')
    def _compute_price(self):
        self.price_subtotal = self.qty * self.price_unit

    #
    bill_quantity_id = fields.Many2one(
        'bill.quantity', string='Bill of Quantity Reference',
        ondelete='cascade', index=True)
    key = fields.Selection(
        [
            ('labor', 'Labor'),
            ('material', 'Material'),
            ('subcontract', 'Subcontract'),
            ('work_package', 'Work Package'),
        ], 'Key', default='labor')
    product_id = fields.Many2one(
        'product.product', string='Product',
        ondelete='restrict', index=True)
    employee_id = fields.Many2one(
        'hr.employee', 'Employee', )
    # assest_id = fields.Many2one(
    #     'account.asset.asset',string='Assets',)
    partner_id = fields.Many2one(
        'res.partner', string='Partners', )
    work_package_id = fields.Many2one(
        'work.package', string='Work Package', )
    type = fields.Char('Type', size=64, )
    description = fields.Char(
        'Description', size=64, )
    uom_id = fields.Many2one('uom.uom', 'Unit of Measure', )
    qty = fields.Float("Qty", default=1)
    price_unit = fields.Float(
        "Rate", digits_compute=dp.get_precision('Account'), )
    price_subtotal = fields.Float(
        "Total", compute='_compute_price',
        readonly=True, store=True,
        digits_compute=dp.get_precision('Account'), )
# 

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
