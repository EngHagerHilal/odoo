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


class CustomReport(models.TransientModel):
    _name = "report.partner_receipt_report.partner_receipt_pdf"

    def _get_report_values(self,docids,data=None): 
        dat = data  
        data['date'] = data['date']
        data['partner'] = data['partner_id']
        data['amount'] = data['amount']
        data['from'] = data['from']
        data['to'] = data['to']
        return {
            'doc_ids': self.ids,
             docs : docids ,
            'doc_model': 'partner.receipt',
            'data': data,
            'date' : data['date'],
            'date' = data['date'],
            'partner' = data['partner_id'],
            'amount' = data['amount'],
            'from' = data['from'],
            'to' = data['to'],
            'dat' : data
        }
