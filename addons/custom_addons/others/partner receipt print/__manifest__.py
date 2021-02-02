# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015 Dynexcel (<http://dynexcel.com/>).
#
##############################################################################
{
    'name': 'Partner Receipt Report',
    'version': '1.1',
    'summary': 'This module will Print receit to the partner',
    'description': 'This module provides the movement of individual products with opening and closing stocks',
    'author': 'Leen',
    'maintainer': 'Leen',
    'company': 'Leen',
    'website': 'https://www.leen.com',
    'depends': [
		'base', 'account',
		],
    'category': 'Accounting',
    'demo': [],
    'data': ['views/partner_receipt_views.xml',
             'security/ir.model.access.csv',
             'report/partner_receipt_report.xml',
             'report/partner_receipt_report_template.xml'],
    'installable': True,
    'images': ['static/description/banner.png'],
    'qweb': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    'live_test_url':'https://youtu.be/5OqXXKO6gRA',
}
