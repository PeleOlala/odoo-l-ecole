{
    'name': 'hr_hospital_2',
    'version': '1.0.0.0',
    'summary': 'Test task 2 module addon hospital',
    'description': 'Test task 2 modeles addon',
    'author': 'Olga Holodaieva',
    'website': '',
    'license': '',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
             'views/hr_hospital_2_menu.xml',
             'views/patient_view.xml',
             'views/doctor_view.xml',
             'views/patient_card_view.xml',
             'views/diagnosis_view.xml'],
    'category': 'Uncategorized',
    'installable': True,
    'application': True,
    'auto_install': True
}