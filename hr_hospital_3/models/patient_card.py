"""
jamais
"""

from odoo import api, fields, models, _
from odoo.exceptions import UserError


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
    date_time_visite = fields.Date(
        string='Date of visit',
        default=fields.Date.today,
        required=False)
    time_visite = fields.Float(
        string='Time of visit',
        required=False)
    duree_visite = fields.Integer(
        string=' minut ',
        required=False)
    research_ids = fields.One2many(
        comodel_name='hr_hospital_3.research',
        inverse_name='patient_card_id',
        string='Research appointment',
        required=False)
    schedule_doctor_id = fields.Many2one(
        comodel_name='hr_hospital_3.schedule_doctor',
        domain="['&',('doctor_id', '=', doctor_id),('patient_card_id','=',None)]",
        string='Schedule')
    is_finish = fields.Boolean(
        string='Visist is finished')
    active = fields.Boolean(default=True)

    def unlink(self):
        for card in self:
            if card.diagnostic_id:
                raise UserError(_('Cannot do it!'))

    @api.constrains("schedule_doctor_id")
    def _chang_schedule(self):
        for card in self:
            recordset = self.env['hr_hospital_3.patient_card'].search_count([('schedule_doctor_id', '=', card.schedule_doctor_id.id)])
            if recordset > 1 and card.schedule_doctor_id:
                raise UserError(_("Schedule is not free, chose other, pls"))
            if card.is_finish:
                raise UserError(_('Visit is finished. Cannot do it!'))
            card.schedule_doctor_id.write({'patient_card_id': card.id})

    @api.constrains("active")
    def _chang_active(self):
        for card in self:
            if card.diagnostic_id and not card.active:
                raise UserError(_('Cannot do it!'))
