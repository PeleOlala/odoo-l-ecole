from odoo import api, fields, models

class BrefHistoirique(models.Model):
    _name = 'hr_hospital.bref_histoirique'
    _description = 'BrefHistoirique'

    name = fields.Char()
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
        required=True)
    diagnostic_id = fields.Many2one(
        comodel_name='hr_hospital.diagnostic',
        string='Le diagnostic',
        requests=False,
        domain="['&',('medecin_id', '=', self.medecin_id),('parient_id', '=', self.patient_id)]"),
    data_rdv = fields.Date(
        string='Data de RDV',
        required=False)
    time_rdv = fields.Datetime(
        string='Time de RDV',
        required=False)


