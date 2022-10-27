from odoo import api, fields, models, _
from odoo.exceptions import UserError
import datetime


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'

    name = fields.Char(
       string='Prenom'
    )
    numero = fields.Char(
        string="Numéro d'assurance",
        required=False)
    date_de_naissance = fields.Date(
        string='Date de naissance',
        required=True)
    passeport = fields.Char(
        string='Le passeport',
        required=False)
    personne_de_contact_id = fields.Many2one(
        comodel_name='hr_hospital.personne_de_contact',
        string='La personne de contact',
        required=False)
    age = fields.Integer(
        string="l'Age",
        compute='_compute_age_patient',
        )
    state = fields.Selection(
        required=True, default='draft', selection=[
            ('draft', 'Draft'), ('sent', 'Sent'),
            ('test', 'Test Mode')], )

    @api.depends('date_de_naissance')
    def _compute_age_patient(self):
        for card in self:
            date1 = card.date_de_naissance
            date_ah = datetime.date.today()
            if type(date1) == type(date_ah):
                card.age = (date_ah.year-date1.year-1)+(date_ah.month+12-date1.month)//12
            else:
                card.age = 0

class Patient_ext(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient ext 3'
    _inherit = ['hr_hospital.personne','hr_hospital.patient']
    _rec_name = 'name'

    medecin_traitant_id = fields.Many2one(
        comodel_name='hr_hospital.medecin',
        string='Le medecin traitant',
        inverse='_histoir_medecin',
        required=False)

    def _histoir_medecin(self):
        for cadr in self:
            if cadr.id:
                self.env['hr_hospital.histoir'].create({
                    'name':cadr.name+' '+cadr.medecin_traitant_id.name,
                    'medecin_id':cadr.medecin_traitant_id.id,
                    'patient_id':cadr.id,
                    'date_de_nomination':datetime.date.today()})
            else:
                raise UserError(_('Il faut garde la carte de patient.'))



