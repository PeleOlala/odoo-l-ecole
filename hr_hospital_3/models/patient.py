from odoo import api, fields, models
import datetime


class Patient(models.Model):
    _name = 'hr_hospital_3.patient'
    _description = 'Patient'

    name = fields.Char()
    number = fields.Char(
        string="Number assurance",
        required=False)
    birthday = fields.Date(
        string='birthday',
        required=True)
    passport = fields.Char(
        string='Passport',
        required=False)
    personne_contact_id = fields.Many2one(
        comodel_name='hr_hospital_3.personne_contact',
        string='Personne contact',
        required=False)
    age = fields.Integer(
        string="Age",
        compute='_compute_age_patient',
        )
    state = fields.Selection(
        required=True, default='draft', selection=[
            ('draft', 'Draft'), ('sent', 'Sent'),
            ('test', 'Test Mode')], )

    @api.depends('birthday')
    def _compute_age_patient(self):
        for card in self:
            date1 = card.birthday
            date_ah = datetime.date.today()
            if type(date1) == type(date_ah):
                card.age = (date_ah.year-date1.year-1)+(date_ah.month+12-date1.month)//12
            else:
                card.age = 0


class Patient_ext(models.Model):
    _name = 'hr_hospital_3.patient'
    _description = 'Patient ext 3'
    _inherit = ['hr_hospital_3.personne', 'hr_hospital_3.patient']
    _rec_name = 'name'

    doctor_personal_id = fields.Many2one(
        comodel_name='hr_hospital_3.doctor',
        string='Personal doctor',
        inverse='_histoir_doctor',
        required=False)

    def _histoir_doctor(self):
        for cadr in self:
            if cadr.id and cadr.doctor_personal_id:
                self.env['hr_hospital_3.histoir_person_doctor'].create({
                    'name': cadr.name+' '+cadr.doctor_personal_id.name,
                    'doctor_id': cadr.doctor_personal_id.id,
                    'patient_id': cadr.id,
                    'date_appointment': datetime.date.today()})
