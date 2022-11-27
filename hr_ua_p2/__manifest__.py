{
    'name': "hr_ua_p2",

    'summary': "Personnel information on employees, "
               "in accordance with the current "
               "legislation of Ukraine",

    'author': "Olha Holodaieva",
    'website': "http://golodaeva.org.ua",

    'category': 'module_category_human_resources',
    'version': '15.0.1.19',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_contract', 'hr_skills'],

    # always loaded
    'data': [
        'security/hr_ua_p2_groups.xml',
        'security/ir.model.access.csv',
        'data/data_kzot.xml',
        'data/data_kind_of_contract.xml',
        'data/data_pc.xml',
        'views/hr_ua_p2_views.xml',
        'views/hr_views.xml',
        'views/kzot_views.xml',
        'views/employee_family_views.xml',
        'views/military_views.xml',
        'views/hr_contract_views.xml',
        'views/appointment_views.xml',
        'views/pc_ua_views.xml',
        'wizard/appointment_wizard_views.xml'
    ],
    'assets': {
        'web.assets_qweb': [
            'hr_ua_p2/static/src/xml/**/*',
        ],
    },
        # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': True,
}
