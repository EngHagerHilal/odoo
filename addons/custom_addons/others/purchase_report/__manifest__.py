
{
    'name': 'Purchase Report ',
    'version': '12.0.0.0.1',
    'summary': 'Generate purchase general report',
    "description": """
        Purchase Order Report        
    """,
    'author': 'Leen',
    'maintainer': 'Leen',
    'Company': 'Leen',
    'website': 'http://leen-eg.com',
    'depends': ['base','contacts','purchase'],
    'license': 'LGPL-3',
    'category': 'Purchase',
    'data':[
        'wizards/purchase_report_wizard.xml',
        'reports/purchase_report_vendor.xml',
        'reports/purchase_reports.xml',
       ],
    'images': ['static/description/banner.png'],
    'price': 0.0,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 6,
}
