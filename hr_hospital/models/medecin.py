from odoo import api, fields, models

class medecins(models.Model):
    _name = 'hr_hospital.medecin'
    _description = 'Les Medecins'

    name = fields.Char()
    specialiste = fields.Char(
        string='Médecin',
        required=False)

