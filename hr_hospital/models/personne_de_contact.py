from odoo import fields, models, api


class PersonneDeContact(models.Model):
    _name = 'hr_hospital.personne_de_contact'
    _description = 'Description'
    _inherit = ['hr_hospital.personne']

    name = fields.Char()
