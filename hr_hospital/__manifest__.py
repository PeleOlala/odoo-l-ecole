{
    'name': 'hr_hospital',
    'version': '1.1.2.0',
    'summary': 'Test cree module addon hopital',
    'description': 'Test cree modeles addon',
    'category': 'Employees',
    'author': 'Olga Holodaieva',
    'website': '',
    'license': '',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
             'views/hr_hospital_menu.xml',
             'views/patient_view.xml',
             'views/medecin_view.xml'],
    'demo': ['data/hr_hospital_demo.xml'],
    'installable': True,
    'application': True,
    'auto_install': True
}