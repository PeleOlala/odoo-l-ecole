from odoo import api, fields, models


class EmployeeUA(models.Model):
    _inherit = 'hr.employee'

    family_ids = fields.One2many(
        comodel_name='hr_ua_p2.family',
        inverse_name='employee_id',
        string='Membres de famille')
    children = fields.Integer(string='Number of Children', compute='_compte_enfans')
    address_registration_id = fields.Many2one(
        'res.partner', 'Address',
        help='Enter here the address of registration of the employee, not the one linked to your company.',
        groups="hr.group_hr_user", tracking=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    military_id = fields.Many2one(
        comodel_name='hr_ua_p2.military',
        string='Military compte')
    appointment_ids = fields.One2many(
        comodel_name='hr_ua_p2.appointment',
        inverse_name='employee_id',
        string='HR appointment')

    @api.depends('family_ids')
    def _compte_enfans(self):
        for ch_r in self:
            ch_r.children = self.env['hr_ua_p2.family'].search_count(
                ['&', '&', ('relation', '=', 'child'), ('age', '<=', 18), ('employee_id', '=', ch_r.id)])
