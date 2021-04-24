from odoo import models, fields, api, _


class PurchaseReportVendor(models.TransientModel):
    _name = 'purchase.report.general'

    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)

    driver = fields.Many2one('hr.employee' ,string='Driver' , domain=[('job_title', '=', 'سائق')] )
    car_num = fields.Text(string='Car Number')
    
    
    dest = fields.Many2one( 'stock.picking.type', domain=[('code', '=', 'incoming')] ,  string="Destination Location")
    
    product = fields.Many2one('product.product' , string="Product")

    vendor = fields.Many2one('res.partner' , domain=[('supplier', '=', True)] , string="Vendor")


    def print_purchase_report(self):
        #purchase_order = self.env['purchase.order'].search([('x_car_number','=',self.car_num),('x_driver','=',self.driver),('date_order','>=' ,self.start_date), ('date_order', '<=' , self.end_date)])
        purchase_order = self.env['purchase.order']
        orders = purchase_order.search([
                ('date_order', '>=', self.start_date),
                ('date_order', '<=', self.end_date),
        ])
        filtered_moves = orders 
        #filtered_moves = list(filter(lambda x: x.date_done >= self.start_date and x.date_done <= self.end_date,  orders))
        if self.driver :
            filtered_moves = list(filter(lambda x: x.x_driver == self.driver , filtered_moves))
        if self.car_num : 
            filtered_moves = list(filter(lambda x: x.x_car_number == self.car_num , filtered_moves))
        if self.dest : 
            filtered_moves = list(filter(lambda x: x.picking_type_id == self.dest , filtered_moves))
        if self.vendor : 
            filtered_moves = list(filter(lambda x: x.partner_id == self.vendor , filtered_moves))


        orders = [] 
        for order in filtered_moves :
            if order.x_driver : 
                driver = order.x_driver.name
            else:
                if order.x_paid_driver : 
                    driver = order.x_paid_driver
            for move in order.order_line :
                if ( move.product_id == self.product or not self.product) :
                    orders.append ({
                        'name' : order.name,
                        'date' : order.date_order,
                        'product' : move.product_id.name,
                        'quantity' : move.product_qty	,
                        'received' : move.qty_received ,
                        'unit_price' : move.price_unit ,
                        'price_sub' : move.price_subtotal ,
                        'price_tax' : move.price_tax ,
                        'price_total' : move.price_total ,
                        'driver' : driver,
                        'car' : order.x_car_number,
                        'source' : order.partner_id.name,
                        'dest' : order.picking_type_id.warehouse_id.name ,
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
            'dest_location' : self.dest ,
            'product' : self.product ,
            'vendor' : self.vendor ,
        }

        print('datas:', datas)
        return self.env.ref('purchase_report.report_general_purchase').report_action([], data=datas)
