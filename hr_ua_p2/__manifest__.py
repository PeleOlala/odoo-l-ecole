{
    'name': "hr_ua_p2",

    'summary': "Personnel information on employees, "
               "in accordance with the current "
               "legislation of Ukraine",

    'author': "Olha Holodaieva",
    'website': "http://golodaeva.org.ua",
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'version': '15.0.1.1.19',

    # any module necessary for this one to work correctly
    'depends': ['hr_contract', 'hr_skills'],

    # always loaded
    'data': [
        'security/hr_ua_p2_groups.xml',
        'security/ir.model.access.csv',
        'data/data_kzot.xml',
        'views/hr_ua_p2_views.xml',
        'views/pc_ua_views.xml',
        'views/appointment_views.xml',
        'data/data_kind_of_contract.xml',
        'data/data_pc.xml',
        'views/kzot_views.xml',
        'views/employee_family_views.xml',
        'views/military_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_views.xml',
        'wizard/appointment_wizard_views.xml',
        'report/p2_report_template.xml'
    ],
    'assets': {
        'web.assets_qweb': [
            'hr_ua_p2/static/src/xml/**/*',
        ],
        'web.assets_backend': [
            'hr_ua_p2/static/src/scss/hr_ua_appointment.scss',
        ],
    },
        # only loaded in demonstration mode
    'demo': ['demo/demo.xml'
    ],
    'images': ['static/description/drapo.jpg'],
    'installable': True,
    'application': True,
}
