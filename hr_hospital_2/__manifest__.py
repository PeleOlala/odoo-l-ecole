{
    'name': 'hr_hospital_2',
    'version': '15.0.1.0.0',  # Нумерація повінна бути у наступному форматі: номер версії Odoo, та далі три цифри версії
    'summary': 'Test task 2 module addon hospital',
    # 'description': 'Test task 2 modeles addon',  # __manifest__.py:1: [C8103(manifest-deprecated-key), ] Deprecated key "description" in manifest file
    'author': 'Olga Holodaieva',
    'website': '',
    'license': '',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
             'views/hr_hospital_2_menus.xml',
             'views/patient_views.xml',
             'views/doctor_views.xml',
             'views/patient_card_views.xml',
             'views/diagnosis_views.xml'],
    'category': 'Uncategorized',
    'installable': True,
    'application': True,
    'auto_install': True
}
