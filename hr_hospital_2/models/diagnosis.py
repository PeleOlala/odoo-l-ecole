from odoo import fields, models, api


class Diagnosis(models.Model):
    _name = 'hr_hospital_2.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(string='Diagnosis')

