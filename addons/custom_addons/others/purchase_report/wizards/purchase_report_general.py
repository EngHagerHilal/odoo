from odoo import models, fields, api, _


class PurchaseReportVendor(models.TransientModel):
    _name = 'purchase.report.general'

    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)

    driver = fields.Text(string='Driver')
    car_num = fields.Text(string='Car Number')
    

    def print_purchase_report(self):
        #purchase_order = self.env['purchase.order'].search([('x_car_number','=',self.car_num),('x_driver','=',self.driver),('date_order','>=' ,self.start_date), ('date_order', '<=' , self.end_date)])
        purchase_order = self.env['purchase.order'].search([])
        filtered_purchase_order = list(filter(lambda x: ( x.date_order >= self.start_date and x.date_order <= self.end_date)  , purchase_order))

        orders = [] 
        for order in filtered_purchase_order :
            temp_data = []
            temp_data.append(order.name)
            temp_data.append(order.date_order)
            temp_data.append(order.x_balance)
            temp_data.append(order.amount_total)
            temp_data.append(order.partner_id.name)
            temp_data.append(order.amount_tax)
            temp_data.append(order.amount_untaxed)
            temp_data.append(order.x_driver.name)
            temp_data.append(order.x_car_number)
            temp_data.append(order.x_paid_driver)
            lines = []
            for line in order.order_line :
                line_details = []
                line_details.append(line.product_id.name)
                line_details.append(line.product_qty)
                line_details.append(line.qty_received)
                line_details.append(line.price_subtotal)
                line_details.append(line.price_tax)
                line_details.append(line.price_total)
                lines.append(line_details)
            temp_data.append(lines)
            orders.append(temp_data)
        

        datas = {
            'ids': self,
            'model': 'purchase.report.general',
            'out' : orders ,
            'form': filtered_purchase_order,
            'start_date': self.start_date,
            'end_date': self.end_date ,
            'driver' : self.driver ,
            'car_number' : self.car_num ,
        }

        print('datas:', datas)
        return self.env.ref('purchase_report.report_general_purchase').report_action([], data=datas)
