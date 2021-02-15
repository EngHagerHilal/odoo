# -*- encoding: utf-8 -*-
{
    'name': 'Purchase Detail',
    'version': '1',
    'author': 'Kinsoft Indonesia, Kikin Kusumah',
    'website': 'https://kinsoft.id',
    'category': 'Purchase',
    'sequence': 1,
    'summary': 'Allow to see the purchase order line',
    'images': [''],
    'depends': ['purchase', 'purchase_open_qty'],
    'description': """
Allow to see the purchase order line
====================================
    """,
    'data': [
        'views/purchase.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/main_screen.png'], 
}
