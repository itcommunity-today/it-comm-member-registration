{
    'name': 'custom Signup Form',
    'version': '13.0.1.0.0',
    'category': 'Website',
    'summary': 'custom signup form with extra fields',
    'description': """
        This module add phone,Type, Partner Level, Free member
        * Phone Number
        * Company type
        * Free member
        * Partner Level
    """,
    'sequence': 1,
    'author': 'Chaiy Kroem & Mr.Vuthy',
    'website': 'it_community.com.kh',
    'depends': ['auth_signup','custom_template', 'website'],
    'data': [
        'views/views.xml',
        'views/auth_signup_extend_views.xml',
        'views/res_partner_view.xml',
    ],
    'images': [
        'static/description/auth_signup_banner.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
