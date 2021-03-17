from odoo import models, fields, api, _


class InventoryReportVendor(models.TransientModel):
    _name = 'inventory.report.general'

    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)

    driver = fields.Text(string='Driver')
    car_num = fields.Text(string='Car Number')
    
    source = fields.Many2One( 'stock.location',string="Source Location")
    dest = fields.Many2One( 'stock.location	', string="Destination Location")
    
    product = fields.Many2One(string="Product")
    

    def print_inventory_report(self):
        #purchase_order = self.env['purchase.order'].search([('x_car_number','=',self.car_num),('x_driver','=',self.driver),('date_order','>=' ,self.start_date), ('date_order', '<=' , self.end_date)])
        moves = self.env['stock.picking'].search([
                ('date_done', '>=', self.start_date),
                ('date_done', '<', self.end_date),
                ('x_driver.name', 'in', self.driver) ,
                ('x_car_number' , '==' , self.car_num) ,
                ('location_id' , '==' , self.source ),
                ('location_dest_id' , '==' , self.dest) ,
        ])

        #filtered_moves = list(filter(lambda x: x.date_order >= self.start_date and x.date_order <= self.end_date,  purchase_order))
        moves = []
        for order in moves :
            for move in order.move_lines :
                if ( move.product_id == self.product) :
                    moves.append ({
                        date : order.date_done
                        product : move.product_id.name
                        quantity : move.product_qty	
                        driver : order.x_driver.name
                        car : order.x_car_number
                        picking : order.name
                        source : order.location_id.name
                        dest : order.location_dest_id.name
                    })
        

        datas = {
            'doc_ids': data['ids'],
            'model': 'inventory.report.general',
            'form': moves,
            'start_date': self.start_date,
            'end_date': self.end_date ,
            'driver' : self.driver ,
            'car_number' : self.car_num ,
            'source_location' : self.source ,
            'dest_location' : self.dest ,
            'product' : self.product
        }

        print('datas:', datas)
        return self.env.ref('inventory_report.report_general_inventory').report_action([], data=datas)
