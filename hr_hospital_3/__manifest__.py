{
    'name': "hr_hospital_3",

    'summary': "Lesson 3 ",

    'author': "Olha Holodaieva",
    'website': "http://golodaeva.org.ua",

    'category': 'module_category_human_resources',
    'version': '15.0.2.7',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_3_menu.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/personne_contact_view.xml',
        'views/disease_views.xml',
        'views/histoir_person_doctor_view.xml',
        'views/diagnostic_view.xml',
        'views/sample_view.xml',
        'views/research_views.xml',
        'views/patient_card_view.xml',
        'views/schedule_doctor_views.xml',
        'wizard/fill_doctor_person_wizard_views.xml',
        'wizard/disease_report_views.xml',
        'wizard/change_reception_wizard_views.xml',
        'wizard/fill_schedule_doctor_week_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
