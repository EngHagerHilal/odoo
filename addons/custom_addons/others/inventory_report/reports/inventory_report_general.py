from odoo import fields, models, api

class PurchaseReportVendor(models.AbstractModel):
    _name = 'report.inventory_report.inventory_report_general'

    @api.model
    def _get_report_values(self, docids, data=None):
        return { 
            'doc_ids': data.get('ids'),
            'doc_model': data.get('model'),
            'data': data['form'],
            'start_date': data['start_date'],
            'end_date': data['end_date'],
            'driver' : data['driver'] ,
            'car_number' : data['car_number'] ,
            'source' : data['source_location'] ,
            'dest' : date['dest_location'] ,
            'product' : date['product'] ,
        }
