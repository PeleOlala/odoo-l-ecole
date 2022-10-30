from odoo import fields, models


class PersonneContact(models.Model):
    _name = 'hr_hospital_4.personne_contact'
    _description = 'Personne contact'

    name = fields.Char()


class PersonneContactExt(models.Model):
    _name = 'hr_hospital_4.personne_contact'
    _description = 'Persson contact'
    _inherit = ['hr_hospital_4.personne', 'hr_hospital_4.personne_contact']
