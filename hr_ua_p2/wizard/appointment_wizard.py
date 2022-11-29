from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AppointmentWizard(models.TransientModel):
    _name = 'hr_ua_p2.appointment_wizard'
    _description = 'Appointment employees'

    date_begin = fields.Date('Date appointment')
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee')
    date_end = fields.Date(
        string='Á date')
    job_end_id = fields.Many2one(
        comodel_name='hr.job',
        string='Job á')
    permanent = fields.Boolean(
        string='Permanent')
    department_begin_id = fields.Many2one(
        comodel_name='hr.department',
        string='Department de')
    department_end_id = fields.Many2one(
        comodel_name='hr.department',
        string='Department á')

    @api.model
    def action_open_wizard(self):
        _wizard = self.create({})
        return _wizard._action_open_modal()

    def _action_open_modal(self):
        self.refresh()
        return {
            'name': _('Set appointmant'),
            'type': 'ir.actions.act_window',
            'res_model': 'hr_ua_p2.appointment_wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
            'context': {'employee_id': self._context.get('employee_id', [])},
        }

    def action_set_appointment(self):
        self.ensure_one()
        if self.employee_id:
            job_begin_id = self.employee_id.job_id.id
            department_begin_id = self.employee_id.deprtment_id.id
            self.env['hr_ua_p2.appointment'].create({'employee_id': self.employee_id.id,
                                                                   'permanent': self.permanent,
                                                                   'date_begin': self.date_begin,
                                                                   'date_end': self.date_end,
                                                                   'job_end_id': self.job_end_id.id,
                                                                   'job_begin_id': job_begin_id,
                                                     'department_begin_id': department_begin_id,
                                                     'department_end_id': self.department_end_id,
                                                     'state': 'draft'})
            if self.permanent:
                self.employee_id.write({'job_id': self.job_end_id.id, 'department_id':self.department_end_id.id})
        else:
            raise UserError(_("Select employee at first"))
