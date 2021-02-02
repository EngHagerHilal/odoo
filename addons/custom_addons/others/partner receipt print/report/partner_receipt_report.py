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
    _name = "partner_receipt_report.partner_receipt_pdf"

    def _get_report_values(self,docids,data=None):
        return {
            'doc_ids': self.ids,
            'doc_model': 'partner.receipt',
            'data': data,
        }
