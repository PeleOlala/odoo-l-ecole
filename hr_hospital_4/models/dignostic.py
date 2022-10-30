from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Diagnostic(models.Model):
    _name = 'hr_hospital_4.diagnostic'
    _description = 'Diagnostic'

    name = fields.Char(string='Diagnostic patient')
    date_diagnistic = fields.Date(
        string='Date diagnistic',
        default=fields.Date.today,
        required=True)
    appointment = fields.Char(
        string='Appointment',
        required=False)
    patient_id = fields.Many2one(
        comodel_name='hr_hospital_4.patient',
        string='Patient',
        required=True)
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_4.doctor',
        string='Doctor',
        required=False,
        inverse='_appel_mentor')
    disease_id = fields.Many2one(
        comodel_name='hr_hospital_4.disease',
        string='Disease',
        required=False)
    age_for_disease = fields.Integer(
        string='Age for disease',
        compute='_compute_age_patient',
        readonly=True, story=True)
    comment = fields.Text(
        string="Comment of mentor",
        required=False)
    research_ids = fields.Many2many(
        comodel_name='hr_hospital_4.research',
        relation="hr_hospital_4_patient_card_rel",
        column1="diagnostic_id", column2="research_ids",
        domain="['&','&',('doctor_id', '=', doctor_id),('patient_id','=',patient_id),('patient_card_id.diagnostic_id','=',id)]",
        string='Rel research')

    def _appel_mentor(self):
        for cadr in self:
            if (not cadr.comment) and cadr.doctor_id.intern:
                raise UserError(_("Il faut d'abord appel du mentor."))

    @api.depends('patient_id', 'date_diagnistic')
    def _compute_age_patient(self):
        for card in self:
            date1 = card.patient_id.birthday
            date_ah = card.date_diagnistic
            if type(date1) == type(date_ah):
                card.age_for_disease = (date_ah.year - date1.year - 1) + (date_ah.month + 12 - date1.month) // 12
            else:
                card.age_for_disease = 0
