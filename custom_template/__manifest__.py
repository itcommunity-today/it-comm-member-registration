# -*- coding: utf-8 -*-
{
    'name': "custom_template",

    'summary': """
        For Custom all Template in System """,

    'description': """
       For Custom all Template in System 
    """,

    'author': "Chaiy Kroem",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom Template',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web','mail','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/data.xml',
        'views/custom_preferences.xml',
        # 'views/custom_profile.xml',
        'views/templates.xml',
        'views/views.xml',
        'views/q_database.xml',
        'views/webclient_template.xml',
        'views/res_config.xml',
        'views/web_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/xml/q_template.xml',

    ],
}
