from odoo import api, fields, models


class SheduleDoctor(models.Model):
    _name = 'hr_hospital_3.schedule_doctor'
    _description = 'Schedule doctors'

    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_3.doctor',
        string='Doctor',
        required=True)
    data_time_rec = fields.Datetime(
        string='Date and time of reception',
        inverse='_check_time',
        required=True)

    def _check_time(self):
        for cadr in self:
            recordset = self.env['hr_hospital_3.schedule_doctor'].search_count(['&',('doctor_id','=',cadr.doctor_id),('data_time_rec','=',cadr.doctor_id)])
            if recordset > 0:
                raise UserError(_("Double reception. Verefied schedule, pls"))
