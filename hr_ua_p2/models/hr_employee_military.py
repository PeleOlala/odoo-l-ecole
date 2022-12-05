from odoo import fields, models


class MilitaryUA(models.Model):
    _name = 'hr_ua_p2.military'
    _description = 'Military inscrite'

    range = fields.Char(
        string='Military range', translate=True)
    document = fields.Char(
        string='N document')
    department = fields.Char(
        string='Military department', translate=True)
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee')

    def name_get(self):
        return [(tag.id, "%s %s %s %s" % (
            tag.employee_id.name, tag.department, tag.range, tag.document)) for
                tag in self]
