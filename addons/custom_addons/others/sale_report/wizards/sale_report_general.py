from odoo import models, fields, api, _


class PurchaseReportVendor(models.TransientModel):
    _name = 'purchase.report.general'

    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)

    driver = fields.Text(string='Driver')
    car_num = fields.Text(string='Car Number')

    source = fields.Many2one( 'stock.location', string="Destination Location")
    
    product = fields.Many2one('product.product' , string="Product")

    customer = fields.Many2one('res.partner' ,domain=[('customer', '=', True)], string="Vendor")
    agent = fields.Many2one('hr.employee' ,domain=[('job_title', '=', 'مندوب مبيعات')] ,string="Agent")

    def print_purchase_report(self):
        #purchase_order = self.env['purchase.order'].search([('x_car_number','=',self.car_num),('x_driver','=',self.driver),('date_order','>=' ,self.start_date), ('date_order', '<=' , self.end_date)])
        sale_order = self.env['sale.order']
        orders = sale_order.search([
                ('confirmation_date', '>=', self.start_date),
                ('confirmation_date', '<=', self.end_date),
        ])
        filtered_moves = orders 
        #filtered_moves = list(filter(lambda x: x.date_done >= self.start_date and x.date_done <= self.end_date,  orders))
        if self.driver :
            filtered_moves = list(filter(lambda x: x.x_driver.name == self.driver , filtered_moves))
        if self.car_num : 
            filtered_moves = list(filter(lambda x: x.x_car_number == self.car_num , filtered_moves))
        if self.source : 
            filtered_moves = list(filter(lambda x: x.warehouse_id == self.source , filtered_moves))
        if self.customer : 
            filtered_moves = list(filter(lambda x: x.partner_id == self.customer , filtered_moves))
        if self.agent : 
            filtered_moves = list(filter(lambda x: x.x_sale_agent == self.agent , filtered_moves))


        orders = [] 
        for order in filtered_moves :
            for move in order.order_line :
                if ( move.product_id == self.product or not self.product) :
                    orders.append ({
                        'name' : order.name,
                        'date' : order.date_order,
                        'product' : move.product_id.name,
                        'quantity' : move.product_uom_qty	,
                        'received' : move.qty_delivered ,
                        'price_sub' : move.price_subtotal ,
                        'price_tax' : move.price_tax ,
                        'price_total' : move.price_total ,
                        'driver' : order.x_driver.name or order.x_paid_driver,
                        'car' : order.x_car_number,
                        'source' : order.warehouse_id.complete_name,
                        'customer' : order.partner_id.name ,
                        'agent' : order.x_sale_agent.name ,
                        'balance' : order.x_balance ,
                        'total' : order.amount_total ,
                        'untaxed' : order.amount_untaxed ,
                        'taxed' : order.amount_tax
                    })
        
        datas = {
            'ids': self,
            'model': 'inventory.report.general',
            'form': orders,
            'start_date': self.start_date,
            'end_date': self.end_date ,
            'driver' : self.driver ,
            'car_number' : self.car_num ,
            'source_location' : self.source ,
            'product' : self.product ,
            'customer' : self.customer ,
            'agent' : self.agent ,
        }

        print('datas:', datas)
        return self.env.ref('purchase_report.report_general_purchase').report_action([], data=datas)
