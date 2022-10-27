from odoo import api, fields, models


class UnePersonne(models.AbstractModel):
    _name = 'hr_hospital.personne'
    _description = 'Identifie personne'

    nom = fields.Char(
        string='Nom',
        required=True)
    telephone = fields.Char(
        string='Telephone',
        required=False)
    email = fields.Char(
        string='Email',
        required=False)
    sexe = fields.Selection(
        string='Sexe',
        selection=[('masculin', 'Masculin'),
                   ('féminin', 'Féminin'), ('indécis', 'Indécis')],
        required=False, )
    photo = fields.Image(string="Photo", max_width=1920, max_height=1920)
