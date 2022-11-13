# -*- coding: utf-8 -*-
{
    'name': "POS Payment Difference Access",

    'summary': """
        POS Payment Difference Access""",

    'author': "Kites Development",
    'website': "https://kitesdev.com",

    'category': 'Point Of Sale',
    'version': '15.0.0.0',
    "license": "LGPL-3",
    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],
    'installable': True,
    'data': ['security/security.xml'],

    'assets': {
        'web.assets_backend': [
            'pos_payment_difference_access/static/src/js/ClosePosPopup.js',
        ],
    },
}
