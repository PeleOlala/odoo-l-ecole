from odoo import api, fields, models
import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'

    name = fields.Char(
        string='Prenom'
    )
    numero = fields.Char(
        string="Numéro d'assurance",
        required=False)
    nom = fields.Char(
        string='Nom',
        required=True)
    date_de_naissance = fields.Date(
        string='Date de naissance',
        required=True)
    sexe = fields.Selection(
        string='Sexe',
        selection=[('masculin', 'Masculin'),
                   ('féminin', 'Féminin'), ('indécis', 'Indécis')],
        required=False, )
    passeport = fields.Char(
        string='Le passeport',
        required=False)
    personne_de_contact = fields.Char(
        string='Personne de contact',
        required=False)
    age = fields.Integer(
        string="l'Age",
        compute='_compute_age_patient',
        )
    state = fields.Selection(
        required=True, default='draft', selection=[
            ('draft', 'Draft'), ('sent', 'Sent'),
            ('test', 'Test Mode')], )
#@api.multi

    @api.depends('date_de_naissance')
    def _compute_age_patient(self):
        for card in self:
            date1 = card.date_de_naissance
            date_ah = datetime.date.today()
            if type(date1) == type(date_ah):
                card.age = (date_ah.year-date1.year-1)+(date_ah.month+12-date1.month)//12
            else:
                card.age = 0



