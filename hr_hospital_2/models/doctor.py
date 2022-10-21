from odoo import api, fields, models

class doctor(models.Model):
    _name = 'hr_hospital_2.doctor'
    _description = 'Doctor'

    name = fields.Char()
    specialiste = fields.Char(
        string='Specialiste',
        required=False)
