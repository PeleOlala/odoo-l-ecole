from odoo import fields, models


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
        selection=[('draft', 'Draft'),
                   ('approve', 'Approve'), ])
    department_begin_id = fields.Many2one(
        comodel_name='hr.department',
        string='Department de')
    department_end_id = fields.Many2one(
        comodel_name='hr.department',
        string='Department á')

    def name_get(self):
        return [(tag.id, "Employee: {name} de {dtb} á {dte} job position new {jobnew}".format(
            name=tag.employee_id.name, dtb=tag.date_begin, dte=tag.date_end, jobnew=tag.job_end_id)) for
                tag in self]
