from odoo import fields, models, api

class SaleAgentCommissionReport(models.AbstractModel):
    _name = 'report.sale_agent_commission.sale_agent_commission_report'
    
    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': data.get('ids'),
            'doc_model': data.get('model'),
            'commissions': data['form'],
            'start_date': data['start_date'],
            'end_date': data['end_date'],
            'agent' : data['agent'],
            'em_agent' : data['em_agent'],
            'em_driver' : data['em_driver'],
        }


        
