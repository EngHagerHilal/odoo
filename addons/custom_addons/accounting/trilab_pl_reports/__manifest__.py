# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': "Trilab PL Financial Reports",

    'summary': """
        Trilab PL Financial Reports: Balance and P&L
        """,

    'description': """
        Structure for the financial reports Balance and P&L according to polish account rules and in accordance
         to electronic reports for IRS.
    """,

    'author': "Trilab",
    'website': "https://trilab.pl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '1.0',

    'depends': ['account_accountant', 'l10n_pl_reports'],

    'data': [
        'data/trilab_financial_reports.xml',
    ],
    'images': [
        'static/description/banner.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1'
}
