from odoo import models, fields, api, _


class PurchaseReportVendor(models.TransientModel):
    _name = 'purchase.report.general'

    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)

    driver = fields.Text(string='Driver')
    car_num = fields.Text(string='Car Number')
    

    def print_vendor_wise_purchase_report(self):
        purchase_order = self.env['purchase.order'].search([])
        filtered_purchase_order = list(filter(lambda x: ( x.x_car_number == self.car_num and (x.x_driver == self.driver or x.x_paid_driver == self.driver) and x.date_order >= self.start_date and x.date_order <= self.end_date)  , purchase_order))

        datas = {
            'ids': self,
            'model': 'purchase.report.general',
            'form': filtered_purchase_order,
            'start_date': self.start_date,
            'end_date': self.end_date ,
            'driver' : self.driver ,
            'car_number' : self.car_num ,
            'vendor' : self.vendor
        }

        print('datas:', datas)
        return self.env.ref('purchase_report.report_general_purchase').report_action([], data=datas)
