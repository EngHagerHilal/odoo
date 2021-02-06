# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015 Dynexcel (<http://dynexcel.com/>).
#
##############################################################################
{
    'name': 'Detailed_tax_Report',
    'version': '1.0',
    'summary': 'This module will Print All Taxes in Details and the summary',
    'description': 'This module provides the movement of individual products with opening and closing stocks',
    'author': 'Leen',
    'maintainer': 'Leen',
    'company': 'Leen',
    'website': 'https://www.leen.com.eg,
    'depends': [
		'base', 'account',
		],
    'category': 'Accounting',
    'demo': [],
    'data': ['views/detailed_tex_views.xml',
             'security/ir.model.access.csv',
             'report/detailed_tax_report_template.xml',
             'report/detailed_tax_report.xml'],
    'installable': True,
    'images': ['static/description/banner.png'],
    'qweb': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
