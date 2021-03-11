# -*- coding: utf-8 -*-
# Part of Kiran Infosoft. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class ReportProductoutstanding(models.AbstractModel):
    _name = 'report.ki_product_oustanding.product_outstanding_report_tmpl'

    @api.model
    def _compute_product_outstanding(self, data):
        domain = [
            ('date', '>=', data['date_from']),
            ('date', '<=', data['date_to']),
            ('partner_id', 'in', data['partner_ids']),
        ]
#         
        report_ids = self.env['sale.report'].sudo().search(domain, order="partner_id")
        data_dict = {}

        for line in report_ids:

            if line.order_id.partner_id not in data_dict:
                data_dict[line.order_id.partner_id] = {}


            if line.product_id not in data_dict[line.order_id.partner_id]:
                data_dict[line.order_id.partner_id][line.product_id] = {}

            if line.order_id not in data_dict[line.order_id.partner_id][line.product_id]:
                data_dict[line.order_id.partner_id][line.product_id][line.order_id] = {
                    'qty_delivered': line.qty_delivered,
                    'product_uom_qty': line.product_uom_qty
                }
            else:
                data_dict[line.order_id.partner_id][line.product_id][line.order_id]['qty_delivered'] += line.qty_delivered
                data_dict[line.order_id.partner_id][line.product_id][line.order_id]['product_uom_qty'] += line.product_uom_qty
        return data_dict

    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = 'res.partner'
        wiz_rec = self.env[self._context.get('active_model', False)].browse(self._context.get('active_ids', False))
        result = self._compute_product_outstanding(data)
        partner_ids = [r.id for r in result]
        docs = self.env[self.model].browse(partner_ids)

        docargs = {
            'doc_ids': wiz_rec.ids,
            'doc_model': 'product.outstanding.wizard',
            'data': data,
            'docs': wiz_rec,
            'data_dict': result,
        }
        return docargs
