from odoo import fields, models, api


class PersonneContact(models.Model):
    _name = 'hr_hospital_3.personne_contact'
    _description = 'Personne contact'

    name = fields.Char()

class PersonneContactExt(models.Model):
    _name = 'hr_hospital_3.personne_contact'
    _description = 'Persson contact'
    _inherit = ['hr_hospital_3.personne', 'hr_hospital_3.personne_contact']
