from odoo import api, fields, models, _
import datetime
import calendar


class FillScheduleDoctor(models.TransientModel):
    _name = 'hr_hospital_3.fill_schedule_wizard'
    _description = 'Fill schedule wizard'

    date_begin = fields.Date(
        string='de Date:', default=fields.Date.today)
    date_end = fields.Date(
        string='á Date:', default=fields.Date.today)   # + datetime.timedelta(days=7)))
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_3.doctor',
        string='For doctor')
    dure_rec = fields.Integer(
        string='duration of one reception in minute',
        default=40)
    time_begin_odd = fields.Float('start and end for week odd')
    time_begin_even = fields.Float('start and end for week even :')
    time_end_odd = fields.Float(':')
    time_end_even = fields.Float(':')

    @api.model
    def action_open_wizard(self):
        _wizard = self.create({})
        return _wizard._action_open_modal()

    def _action_open_modal(self):
        self.refresh()
        return {
            'name': _('Fill doctor personal'),
            'type': 'ir.actions.act_window',
            'res_model': 'hr_hospital_3.fill_schedule_wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
            'context': {'active_ids': self._context.get('active_ids', [])},
        }

    def action_fill_schedule(self):
        self.ensure_one()
        cur_day = self.date_begin
        delta_time = (self.dure_rec % 60)/60 + self.dure_rec//60
        while cur_day <= self.date_end:
            if cur_day.weekday() != calendar.SUNDAY and cur_day.weekday() != calendar.SATURDAY:
                if cur_day.isocalendar()[1] % 2 == 0:
                    cur_time = self.time_begin_even
                    cur_teme_end = self.time_end_even
                else:
                    cur_time = self.time_begin_odd
                    cur_teme_end = self.time_end_odd
                while cur_time <= cur_teme_end:
                    self.env['hr_hospital_3.schedule_doctor'].create({'doctor_id': self.doctor_id.id,
                                                                      'date_time_rec': cur_day,
                                                                      'time_rec': cur_time})
                    cur_time += delta_time
            cur_day += datetime.timedelta(days=1)
