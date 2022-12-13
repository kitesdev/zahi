# -*- coding: utf-8 -*-

{
    "name": "POS Receipt Custom",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    "author": "KitesDev",
    "summary": """POS Receipt Custom.""",
    "category": "Sales/Point of Sale",
    "website": "https://kitesdev.com",
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'web.assets_qweb': [
            "pos_receipt_custom/static/src/xml/pos_receipt.xml",
        ],
    },
    "installable": True,
}
