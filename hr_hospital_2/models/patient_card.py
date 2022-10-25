from odoo import fields, models


class PatientCard(models.Model):
    _name = 'hr_hospital_2.patient_card'
    _description = 'Description'

    name = fields.Char()
