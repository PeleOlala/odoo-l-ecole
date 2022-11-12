from odoo import api, fields, models


class Appointment(models.Model):
    _name = 'hr_hospital_4.appointment'
    _description = 'Appointment'

    name = fields.Char()
    patient_card_id = fields.Many2one(
        comodel_name='hr_hospital_4.patient_card',
        string='Visit to doctor',
        required=True)
    patient_id = fields.Many2one(
        comodel_name='hr_hospital_4.patient',
        string='Patient',
        required=True)
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_4.doctor',
        string='Doctor',
        required=True
    )

    @api.depends('patient_card_id')
    def rampli_touts(self):
        for card in self:
            card.patient_id = card.patient_card_id.patient_id.id
            card.doctor_id = card.patient_card_id.doctor_id.id
