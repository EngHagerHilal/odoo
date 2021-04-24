
{
    'name': 'sale_agent_commission',
    'version': '12.0.0.0.1',
    'summary': 'Generate a detailed report for the sale agent commissions',
    "description": """
        Sale Agent Detailed Commissions        
    """,
    'author': 'Leen',
    'maintainer': 'Leen',
    'Company': 'Leen',
    'website': 'http://leen-eg.com',
    'depends': ['base','contacts','sale'],
    'license': 'LGPL-3',
    'category': 'Sale',
    'data':[
        'wizards/sale_report_general.xml',
        'reports/sale_report_general.xml',
        'reports/sale_reports.xml',
       ],
    'images': ['static/description/banner.png'],
    'price': 0.0,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
    'sequence': 6,
}
