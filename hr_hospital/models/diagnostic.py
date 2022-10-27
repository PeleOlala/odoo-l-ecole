from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Diagnostic(models.Model):
    _name = 'hr_hospital.diagnostic'
    _description = 'Les diagnostic'

    name = fields.Char(string='Les diagnostic du patient')
    date_de_diagnistic = fields.Date(
        string='Date de diagnistic',
        default=fields.Date.today,
        required=True)
    traitement_prescrit = fields.Char(
        string='Traitement prescrit',
        required=False)
    patient_id = fields.Many2one(
        comodel_name='hr_hospital.patient',
        string='Patient(e)',
        required=True)
    medecin_id = fields.Many2one(
        comodel_name='hr_hospital.medecin',
        string='Medecin',
        required=False,
        inverse='_appel_mentor'
    )
    malade_id = fields.Many2one(
        comodel_name='hr_hospital.malade',
        string='Malade',
        required=False)
    age_de_malade = fields.Integer(
        string='Age de malade',
        compute='_compute_age_patient',
        readonly=True)
    observation = fields.Text(
        string="L'observation du mentor",
        required=False)

    def _appel_mentor(self):
        for cadr in self:
            if (not cadr.observation) and cadr.medecin_id.intern:
                raise UserError(_("Il faut d'abord appel du mentor."))


    @api.depends('patient_id', 'date_de_diagnistic')
    def _compute_age_patient(self):
        for card in self:
            date1 = card.patient_id.date_de_naissance
            date_ah = card.date_de_diagnistic
            if type(date1) == type(date_ah):
                card.age_de_malade = (date_ah.year-date1.year-1)+(date_ah.month+12-date1.month)//12
            else:
                card.age_de_malade = 0
    
