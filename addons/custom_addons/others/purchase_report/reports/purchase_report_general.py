from odoo import fields, models, api

class PurchaseReportVendor(models.AbstractModel):
    _name = 'report.purchase_report.purchase_report_general'

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': data.get('ids'),
            'doc_model': data.get('model'),
            'dat': data['form'],
            'data': data['out'],
            'start_date': data['start_date'],
            'end_date': data['end_date'],
            'driver' : data['driver'] ,
            'car_number' : data['car_number'] ,
        }