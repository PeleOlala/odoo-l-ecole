import datetime
from odoo import fields, models, _


class DeseaseSummary(models.TransientModel):

    _name = 'hr_hospital_3.desease.summary.report'
    _description = 'Summary diseases by month'

    date_from = fields.Date(string='From')
    doctor_ids = fields.Many2many('hr_hospital_3.doctor', string='Doctor(s)')
    year = fields.Integer(
        string='',
        required=False,
        default=2022)
    month = fields.Selection(
        string='Month',
        selection=[('1', 'Jan'),
                   ('2', 'Feb'),
                   ('3','Mar'),
                   ('4', 'Avr')])


    def action_open_wizard(self):
        return {
            'name': _('Report disease'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr_hospital_3.desease.summary.report',
            'target': 'new',
            'context': {'active_ids': self._context.get('active_ids', [])},
        }

    def print_report(self):
        self.ensure_one()
        [data] = self.read()
        self.date_from = datetime.date(self.year, int(self.month), 1)
        data['doctor_ids'] = self.env.context.get('active_ids', [])
        doctors = self.env['hr_hospital_3.doctor'].browse(data['doctor_ids'])
        datas = {
            'ids': [],
            'model': 'hr_hospital_3.doctor',
            'form': data
        }
        return (datas, doctors)
