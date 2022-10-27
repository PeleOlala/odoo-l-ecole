from odoo import fields, models, api


class HistoirMedecin(models.Model):
    _name = 'hr_hospital_3.histoir_person_doctor'
    _description = "Histoir person doctor "

    name = fields.Char()
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_3.doctor',
        string='Doctor generaliste',
        required=False)
    patient_id = fields.Many2one(
        comodel_name='hr_hospital_3.patient',
        string='Patient(e)',
        required=False)
    date_appointment = fields.Date(
        string='Date appointment',
        required=False)

    @api.model_create_multi
    def create(self, vals_list):
        # OVERRIDE
        return super().create(vals_list)
