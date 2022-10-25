from odoo import fields, models


class Doctor(models.Model):  # У назві класів повинен використовуватися CamelCase.
    _name = 'hr_hospital_2.doctor'
    _description = 'Doctor'

    name = fields.Char()
    specialiste = fields.Char(
        string='Specialiste',
        required=False)
