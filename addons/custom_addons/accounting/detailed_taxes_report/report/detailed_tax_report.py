# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015 Dynexcel (<http://dynexcel.com/>).
#
##############################################################################
import pytz
import time

from odoo import models, fields, api
from odoo.exceptions import ValidationError, Warning


class CustomReport(models.AbstractModel):
    _name = 'detailed_taxes_report.detailed_taxes_report'

   @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']

        invoices = self.env['account.invoice']
        start_date = datetime.strptime(date_start, DATE_FORMAT)
        end_date = datetime.strptime(date_end, DATE_FORMAT)
        delta = timedelta(days=1)

        docs = []
        while start_date <= end_date:
            date = start_date
            start_date += delta

            print(date, start_date)
            In = invoices.search([
                ('__last_update', '>=', date.strftime(DATETIME_FORMAT)),
                ('__last_update', '<', start_date.strftime(DATETIME_FORMAT)),
                ('state', 'in', ['paid']),
                ('type' , 'in' , ['in_refund' ,'out_invoice'])
            ])
            Out = invoices.search([
                ('__last_update', '>=', date.strftime(DATETIME_FORMAT)),
                ('__last_update', '<', start_date.strftime(DATETIME_FORMAT)),
                ('state', 'in', ['paid']),
                ('type' , 'in' , ['out_refund' ,'in_invoice'])
            ])
            #total_orders = len(orders)
            #amount_total = sum(order.amount_total for order in orders)

            total_in = len(In)
            amount_total_in = sum(order.amount_tax for order in In)

            total_out = len(Out)
            amount_total_out = sum(order.amount_tax for order in Out)

            docs.append({
                'date': date.strftime("%Y-%m-%d"),
                'total_in': total_in,
                'amount_total_in': amount_total_in,
                'total_out': total_out,
                'amount_total_out': amount_total_out,
                'company': self.env.user.company_id
            })
        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }

