from odoo import fields, models


class PatientCard(models.Model):
    _name = 'hr_hospital_3.patient_card'
    _description = 'Patient cards'

    name = fields.Char()
    appointment = fields.Char(
        string='Appointment',
        required=False)
    patient_id = fields.Many2one(
        comodel_name='hr_hospital_3.patient',
        string='Patient',
        required=True)
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_3.doctor',
        string='Doctor',
        required=False)
    diagnostic_id = fields.Many2one(
        comodel_name='hr_hospital_3.diagnostic',
        string='Diagnos',
        required=False)
    date_time_visite = fields.Datetime(
        string='Date time',
        default=fields.Date.today,
        required=False)
    research_ids = fields.One2many(
        comodel_name='hr_hospital_3.research',
        inverse_name='id',
        string='Research appointment',
        required=False)
