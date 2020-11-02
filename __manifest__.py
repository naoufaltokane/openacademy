# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board','account'],

    # always loaded
    'data': [
        #'security/security.xml',
        'security/ir.model.access.csv',
        'data/openacademy_data.xml',
        'views/templates.xml',
        #'views/analysis.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/user.xml',
        'views/session_board.xml',
        'reports.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}