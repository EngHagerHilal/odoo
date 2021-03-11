# -*- coding: utf-8 -*-
# Part of Kiran Infosoft. See LICENSE file for full copyright and licensing details.

{
    'name': 'Outstanding Product Report By Customer',
    'summary': 'Outstanding Product Report By Customer',
    'description': """
Outstanding Product Report By Customer
""",
    'author': "Kiran Infosoft",
    "website": "http://www.kiraninfosoft.com",
    'category': 'Sales',
    'version': '1.0',
    'license': 'Other proprietary',
    'price': 0.0,
    'currency': 'EUR',
    'images': ['static/description/logo.png'],
    'depends': [
        'sale',
    ],
    'data': [
        'wizard/product_outstanding_wizard_view.xml',
        'report/report_product_outstanding_view.xml',
        'views/report_action.xml',
    ],
    'installable': True,
}
