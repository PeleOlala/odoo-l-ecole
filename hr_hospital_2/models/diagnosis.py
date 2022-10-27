from odoo import fields, models  # Модулі, що імпортуються повинні йти в алфавітному порядку. Імпорти, що не використовуються потрібно видалити.


class Diagnosis(models.Model):
    _name = 'hr_hospital_2.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(string='Diagnosis')

