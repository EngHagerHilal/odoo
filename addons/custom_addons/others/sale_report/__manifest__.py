
{
    'name': 'sale_report',
    'version': '12.0.0.0.1',
    'summary': 'Generate Sales general report',
    "description": """
        Sale Order Report        
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
    'application': True,
    'sequence': 6,
}
