from odoo import models, fields, api, _


class SaleAgentCommission(models.TransientModel):
    _name = 'sale.agent.commission'

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)

    agent = fields.Many2one('hr.employee' ,string="Employee" ,domain=[('job_title', 'in', ['مندوب مبيعات','سائق'])], delegate=True)

    def print_sale_agent_commission_report(self):
        #purchase_order = self.env['purchase.order'].search([('x_car_number','=',self.car_num),('x_driver','=',self.driver),('date_order','>=' ,self.start_date), ('date_order', '<=' , self.end_date)])
        #sale_agents = self.env['hr.employee']
        #agent = sale_agents.search([
        #        ('id', '=', self.agent),
        #])
        invoices = self.agent.invoices
        transfers = self.agent.x_transfers
        Em_agent = 0
        Em_driver = 0
        if invoices :
            Em_agent = 1
        if transfers :
            Em_driver = 1 
        #filtered_moves = list(filter(lambda x: x.date_done >= self.start_date and x.date_done <= self.end_date,  orders))
        filtered_invoices = list(filter(lambda x: x.payment_date >= self.start_date and x.payment_date <= self.end_date , invoices))
        filtered_transfers = list(filter(lambda x: x.date_done and x.date_done.date() >= self.start_date and x.date_done.date() <= self.end_date , transfers))

        commissions = []
        if len(filtered_invoices) != 0 :
            for invoice in filtered_invoices :
                commissions.append ({
                    'name' : invoice.number,
                    'customer' : invoice.partner_id.name,
                    'date' : invoice.date_invoice,
                    'payment' : invoice.payment_date,
                    'commission' : invoice.commission ,
                    'product' : invoice.invoice_line_ids[0].product_id.name ,
                    'unit_price' : invoice.invoice_line_ids[0].price_unit ,
                    'quantity' : invoice.invoice_line_ids[0].quantity ,
                    'total' : invoice.amount_total ,
                    'untaxed' : invoice.amount_untaxed ,
                    'taxed' : invoice.amount_tax
                })
        else :
            if len(filtered_transfers) != 0 :
                for invoice in filtered_transfers :
                    commissions.append ({
                        'name' : invoice.name,
                        'customer' : invoice.partner_id.name,
                        'date' : invoice.date_done,
                        'commission' : invoice.compute_commission() ,
                        'location' : invoice.location_id.name ,
                        'product' : invoice.move_lines[0].product_id.name ,
                        'quantity' : invoice.move_lines[0].quantity_done ,
                })
        
        datas = {
            'ids': self,
            'model': 'sale.agent.commission',
            'form': commissions,
            'start_date': self.start_date,
            'end_date': self.end_date ,
            'agent' : self.agent.name ,
            'em_agent' : Em_agent ,
            'em_driver' : Em_driver ,
        }

        print('datas:', datas)
        return self.env.ref('sale_agent_commission.report_agent_commission').report_action([], data=datas)
