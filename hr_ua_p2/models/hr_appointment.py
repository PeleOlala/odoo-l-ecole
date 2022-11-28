from odoo import fields, models


class Appointment(models.Model):
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
                   ('approve', 'Approve'), ] )

    def name_get(self):
        return [(tag.id, "Employee: %s de %s á %s job position new %s" % (
            tag.employee_id.name, tag.date_begin, tag.date_end, tag.job_end_id)) for
                tag in self]
