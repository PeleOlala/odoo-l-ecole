import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SheduleDoctor(models.Model):
    _name = 'hr_hospital_4.schedule_doctor'
    _description = 'Schedule doctors'

    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_4.doctor',
        string='Doctor',
        required=True)
    date_time_rec = fields.Date(
        string='Date of reception',
        inverse='_check_time',
        required=True)
    time_rec = fields.Float(
        string='Time of reception',
        required=True)
    date_time_rec_cal = fields.Datetime(
        string='pour calendar',
        compute='_compute_date')
    dure_time = fields.Float(
        string='Dure time')
    patient_card_id = fields.Many2one(
        comodel_name='hr_hospital_4.patient_card',
        string='Visit')

    def _check_time(self):
        for cadr in self:
            recordset = self.env['hr_hospital_4.schedule_doctor'].search_count(
                ['&', '&', ('time_rec', '=', cadr.time_rec), ('doctor_id', '=', cadr.doctor_id.id),
                 ('date_time_rec', '=', cadr.date_time_rec)])
            if recordset > 1:
                raise UserError(_("Double reception. Verefied schedule, pls"))

    def name_get(self):
        return [(tag.id, "%s %s:%dh %dm" % (
        tag.doctor_id.name, tag.date_time_rec, tag.time_rec, round(tag.time_rec - int(tag.time_rec), 2) * 60)) for
                tag in self]

    @api.depends('date_time_rec', 'time_rec')
    def _compute_date(self):
        for tag in self:
            tag.date_time_rec_cal = datetime.datetime(tag.date_time_rec.year, tag.date_time_rec.month,
                                                      tag.date_time_rec.day, int(tag.time_rec),
                                                      int(round(tag.time_rec - int(tag.time_rec), 2) * 600 / 10))
