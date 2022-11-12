from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SetReception(models.TransientModel):
    _name = 'hr_hospital_4.set_reception.wizard'
    _description = 'Set reception of doctor'

    schedule_doctor_id = fields.Many2one(
        comodel_name='hr_hospital_4.schedule_doctor',
        domain="['&',('doctor_id', '=', doctor_id),('patient_card_id','=',False)]",
        string='New schedule reception')
    patient_id = fields.Many2one(
        comodel_name='hr_hospital_4.patient',
        string='Patient')
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_4.doctor',
        string='For doctor')

    @api.model
    def action_open_wizard(self):
        _wizard = self.create({})
        return _wizard._action_open_modal()

    def _action_open_modal(self):
        self.refresh()
        return {
            'name': _('Set reception'),
            'type': 'ir.actions.act_window',
            'res_model': 'hr_hospital_4.set_reception.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
            'context': {'doctor_id': self._context.get('doctor_id', [])
                ,'patient_id': self._context.get('patient_id', [])},
        }

    def action_set_visite(self):
        self.ensure_one()
        if not self.schedule_doctor_id.patient_card_id:
            sc_id = self.env['hr_hospital_4.patient_card'].create({'doctor_id': self.doctor_id.id
                                    , 'patient_id': self.patient_id.id
                                    , 'schedule_doctor_id': self.schedule_doctor_id.id
                                    , 'date_time_visite': self.schedule_doctor_id.date_time_rec
                                    , 'time_visite': self.schedule_doctor_id.time_rec
                                    , 'name': "Visit %s chez %s" % (self.patient_id.name, self.doctor_id.name)})
            self.schedule_doctor_id.write({'patient_card_id': sc_id.id})
        else:
            raise UserError(_("Schedule is not free, chose other, pls"))
