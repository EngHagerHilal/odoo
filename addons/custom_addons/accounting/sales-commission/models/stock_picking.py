# See LICENSE file for full copyright and licensing details.
from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta
from datetime import date , time



class StockPicking(models.Model):
    _inherit = 'stock.picking'

    commission = fields.Float( string="Commissions", compute="compute_commission" , store=True, default=0)
    
    @api.depends('state')
    def compute_commission(self) :
        for record in self :
            if (record.state == 'done'):
                if record.move_lines :
                    count = 0
                    for move in record.move_lines :
                        if move.product_id.categ_id.del_commission :
                            count = count + move.quantity_done
                            if count >= move.product_id.categ_id.del_standard :
                                record.commission =  move.product_id.categ_id.del_rate
                            else :
                                record.commission = ( count * move.product_id.categ_id.del_rate ) /1000 
                            #self.sale_agent.commissions += self.commission 
            else :
                record.commission = 0
        #return self.commission




