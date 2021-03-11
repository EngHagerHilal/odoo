# -*- coding: utf-8 -*-

import time
from datetime import datetime
from dateutil import relativedelta
from odoo import api, models, fields, _


class ProductOutstandingWizard(models.TransientModel):
    _name = "product.outstanding.wizard"

    partner_ids = fields.Many2many(
        'res.partner',
        string='Partner',
        required=False
    )
    date_from = fields.Date(
        string='Start Date',
        required=True,
        default=lambda *a: time.strftime('%Y-%m-01'),
    )
    date_to = fields.Date(
        string='End Date',
        required=True,
        default=lambda *a: str(
            datetime.now() + relativedelta.relativedelta(
                months=+1, day=1, days=-1
            )
        )[:10],
    )

    @api.multi
    def action_print_report(self):
        partners = self.partner_ids
        data = {
            'date_from': self.date_from,
            'date_to': self.date_to,
            'partner_ids': self.partner_ids.ids
        }
        return self.env.ref(
            'ki_product_oustanding.action_product_outstanding_report'
        ).report_action(self, data=data)

