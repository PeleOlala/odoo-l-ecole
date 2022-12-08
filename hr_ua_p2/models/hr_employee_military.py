from odoo import fields, models, _


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
    military_group = fields.Char(string="Military Group")
    ready_service = fields.Selection(
        string='Ready to Service',
        selection=[('ready', _('Ready')),
                   ('not_ready', _('Not ready')),
                   ('party_ready', _('Not suitable for a reasonable time. Suitable for wartime'))],
    )
    military_category = fields.Char(
        string='Military category')
    military_speciality = fields.Char(
        string='Military speciality',
        required=False)

    def name_get(self):
        return [(tag.id, "%s %s %s %s" % (
            tag.employee_id.name, tag.department, tag.range, tag.document)) for
                tag in self]
