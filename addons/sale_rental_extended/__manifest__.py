# -*- coding: utf-8 -*-

{
    "name": "Sale Rental Extended",
    "summary": "Sale Rental Extended",
    "version": "12.0.1.0.2",
    "category": "",
    "author": "",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'base',
        'sale',
        'sale_start_end_dates',
        'event_sale',
        'web_domain_field',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/branch.xml',
        'views/sale_order.xml',
        'views/invoice.xml',
        'views/event.xml',
        'views/payment.xml',
        'views/product.xml',
        'views/partner.xml',
        'reports/report_sale_order.xml',
        'reports/report_account_invoice.xml',
    ],
}
