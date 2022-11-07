"""
jamais
"""

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class CnahgeReception(models.TransientModel):
    _name = 'hr_hospital_3.change_reception.wizard'
    _description = 'I change reception of doctor'

    schedule_doctor_id = fields.Many2one(
        comodel_name='hr_hospital_3.schedule_doctor',
        string='New schedule reception',
        required=True)
    patient_card_id = fields.Many2one(
        comodel_name='hr_hospital_3.patient_card',
        string='for visit')
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_3.doctor',
        string='For doctor')

    @api.model
    def action_open_wizard(self):
        _wizard = self.create({})
        return _wizard._action_open_modal()

    def _action_open_modal(self):
        self.refresh()
        return {
            'name': _('Fill doctor personal'),
            'type': 'ir.actions.act_window',
            'res_model': 'hr_hospital_3.fill_doctor_wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
            'context': {'active_ids': self._context.get('active_ids', [])},
        }

    def action_change(self):
        self.ensure_one()
        self.patient_card_id = self.env['hr_hospital_3.patient_card'].\
            browse(self.env.context.get('active_ids', []))
        recordset = self.env['hr_hospital_3.patient_card'].\
            search_count([('schedule_doctor_id','=', self.schedule_doctor_id.id)])
        if recordset > 1:
            raise UserError(_("Schedule is not free, chose other, pls"))

        self.patient_card_id.schedule_doctor_id.write({'patient_card_id': None})
        self.patient_card_id.write({'schedule_doctor_id': self.schedule_doctor_id.id,
                                        'date_time_visite': self.schedule_doctor_id.date_time_rec,
                                        'time_visite': self.schedule_doctor_id.time_rec,
                                        'doctor_id': self.schedule_doctor_id.doctor_id.id})
