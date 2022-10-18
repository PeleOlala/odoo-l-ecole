from odoo import api, fields, models 

class Diagnostic(models.Model):
    _name = 'hr_hospital.diagnostic'
    _description = 'Les diagnostic'

    name = fields.Char(string='Les diagnostic du patient')
    date_de_diagnistic = fields.Date(
        string='Date de diagnistic',
        default=fields.Date.today,
        required=False)
    traitement_prescrit = fields.Char(
        string='Traitement prescrit',
        required=False)
    patient_id = fields.Many2one(
        comodel_name='hr_hospital.patient',
        string='Patient(e)',
        required=False)
    medecin_id = fields.Many2one(
        comodel_name='hr_hospital.medecin',
        string='Medecin',
        required=False)
    malade_id = fields.Many2one(
        comodel_name='hr_hospital.malade',
        string='Malade',
        required=False)
