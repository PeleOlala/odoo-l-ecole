from odoo import fields, models, api

class HistoirMedecin(models.Model):
    _name = 'hr_hospital.histoir'
    _description = "L'histoir de medecin"

    name = fields.Char()
    medecin_id = fields.Many2one(
        comodel_name='hr_hospital.medecin',
        string='Le medecin generaliste',
        required=False)
    patient_id = fields.Many2one(
        comodel_name='hr_hospital.patient',
        string='Le patient(e)',
        required=False)
    date_de_nomination = fields.Date(
        string='Date de nomination',
        required=False)

    @api.model_create_multi
    def create(self, vals_list):
        # OVERRIDE
        return super().create(vals_list)
