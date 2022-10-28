from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SheduleDoctor(models.Model):
    _name = 'hr_hospital_3.schedule_doctor'
    _description = 'Schedule doctors'

    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_3.doctor',
        string='Doctor',
        required=True)
    date_time_rec = fields.Date(
        string='Date of reception',
        inverse='_check_time',
        required=True)
    time_rec = fields.Float(
        string='Time of reception',
        required=True)

    def _check_time(self):
        for cadr in self:
            recordset = self.env['hr_hospital_3.schedule_doctor'].search_count(['&','&',('time_rec','=',cadr.time_rec),('doctor_id','=',cadr.doctor_id.id),('date_time_rec','=',cadr.date_time_rec)])
            if recordset > 1:
                raise UserError(_("Double reception. Verefied schedule, pls"))

    def name_get(self):
        return [(tag.id, "%s %s:%dh %dm" % (tag.doctor_id.name, tag.date_time_rec, tag.time_rec, tag.time_rec.as_integer_ratio()[1]*6/10)) for tag in self]

