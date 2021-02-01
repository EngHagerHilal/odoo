# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Partner Report',
    'version': '12.0.0.0',
    'summary': 'Easily Customizable Report Template for Partner',
    'category': 'Tools',
    'description': """
		Customize report		
    """,
    'license':'OPL-1',
    'author': 'Leen',
    'depends': ['base', 'account' ,'base_vat'],
    'data': [
		
		"views/partner_report.xml",
		"views/report_partner_cash.xml",
		
             ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}
