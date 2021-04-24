# See LICENSE file for full copyright and licensing details.
from odoo import api ,fields, models
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta
from datetime import date , time



class StockPicking(models.Model):
    _inherit = 'stock.picking'

    commission = fields.Float( string="Commissions", compute="compute_commission" , default=0)
    
    def compute_commission(self) :
        #for record in self :
        if (self.state == 'done'):
            if self.move_lines :
                count = 0
                for move in self.move_lines :
                    if move.product_id.categ_id.del_commission :
                        count = count + move.quantity_done
                        if count >= move.product_id.categ_id.del_standard :
                            self.commission =  move.product_id.categ_id.del_rate
                        else :
                            self.commission = ( count * move.product_id.categ_id.del_rate ) /1000 
                        #self.sale_agent.commissions += self.commission 
        else :
            self.commission = 0
        return self.commission




