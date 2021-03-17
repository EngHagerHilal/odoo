
{
    'name': 'inventory_report',
    'version': '12.0.0.0.1',
    'summary': 'Generate Inventory general report',
    "description": """
        Inventory Report        
    """,
    'author': 'Leen',
    'maintainer': 'Leen',
    'Company': 'Leen',
    'website': 'http://leen-eg.com',
    'depends': ['base','contacts','stock'],
    'license': 'LGPL-3',
    'category': 'Inventory',
    'data':[
        'wizards/inventory_report_general.xml',
        'reports/inventory_report_general.xml',
        'reports/inventory_reports.xml',
       ],
    'images': ['static/description/banner.png'],
    'price': 0.0,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 6,
}
