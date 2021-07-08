from odoo import models, fields, api, _
from datetime import datetime, timedelta

from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class InventoryReportVendor(models.TransientModel):
    _name = 'inventory.report.general'

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)

    driver = fields.Text(string='Driver')
    car_num = fields.Text(string='Car Number')
    

    source = fields.Many2one( 'stock.location',string="Source Location")
    dest = fields.Many2one( 'stock.location', string="Destination Location")
    
    product = fields.Many2one('product.product' , string="Product")
    
    

    def print_inventory_report(self):
        #purchase_order = self.env['purchase.order'].search([('x_car_number','=',self.car_num),('x_driver','=',self.driver),('date_order','>=' ,self.start_date), ('date_order', '<=' , self.end_date)])
        orders = self.env['stock.picking']
        
        orders = orders.search([
                ('date_done.date()', '>=', self.start_date),
                ('date_done.date()', '<=', self.end_date),
        ])

        filtered_moves = orders 
        #filtered_moves = list(filter(lambda x: x.date_done >= self.start_date and x.date_done <= self.end_date,  orders))
        if self.driver :
            filtered_moves = list(filter(lambda x: x.x_driver.name == self.driver , filtered_moves))
        if self.car_num : 
            filtered_moves = list(filter(lambda x: x.x_car_number == self.car_num , filtered_moves))
        if self.source : 
            filtered_moves = list(filter(lambda x: x.location_id == self.source , filtered_moves))
        if self.dest : 
            filtered_moves = list(filter(lambda x: x.location_dest_id == self.dest , filtered_moves))


        moves = []
        for order in filtered_moves :
            for move in order.move_lines :
                if ( move.product_id == self.product or not self.product) :
                    moves.append ({
                        'date' : order.date_done,
                        'product' : move.product_id.name,
                        'quantity' : move.product_qty	,
                        'driver' : order.x_driver.name,
                        'unit' : move.product_uom.name ,
                        'car' : order.x_car_number,
                        'picking' : order.name ,
                        'source' : order.location_id.complete_name,
                        'dest' : order.location_dest_id.complete_name ,
                    })
        datas = {
            'ids': self,
            'model': 'inventory.report.general',
            'form': moves,
            'start_date': self.start_date,
            'end_date': self.end_date ,
            'driver' : self.driver ,
            'car_number' : self.car_num ,
            'source_location' : self.source ,
            'dest_location' : self.dest ,
            'product' : self.product ,
        }

        print('datas:', datas)
        return self.env.ref('inventory_report.report_general_inventory').report_action([], data=datas)
