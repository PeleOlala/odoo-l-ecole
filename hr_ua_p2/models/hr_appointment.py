from odoo import fields, models, _


class Appointment(models.Model):
    """
    Appointment temporare or permanent
    """
    _name = 'hr_ua_p2.appointment'
    _description = 'Appointment job position'

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee')
    date_begin = fields.Date(
        string='De date')
    date_end = fields.Date(
        string='Á date')
    job_begin_id = fields.Many2one(
        comodel_name='hr.job',
        string='Job de')
    job_end_id = fields.Many2one(
        comodel_name='hr.job',
        string='Job á')
    permanent = fields.Boolean(
        string='Permanent')
    state = fields.Selection(
        string='status',
        selection=[('draft', _('Draft')),
                   ('approve', _('Approve')),
                   ('cancel', _('Cancel')), ])
    department_begin_id = fields.Many2one(
        comodel_name='hr.department',
        string='Department de')
    department_end_id = fields.Many2one(
        comodel_name='hr.department',
        string='Department á')

    def name_get(self):
        return [(tag.id,
                 f"Employee: {tag.employee_id.name} de {tag.date_begin} á "
                 f"{tag.date_end} job position new {tag.job_end_id}")
                for tag in self]
