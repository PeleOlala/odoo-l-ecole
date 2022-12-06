from odoo import fields, models, _


class ContractUA(models.Model):
    _inherit = 'hr.contract'

    type_labor = fields.Selection(
        string='Type labor',
        selection=[('main', _('Main')),
                   ('internal', _('Internal')),
                   ('external', _('External')), ], )
    reason_for_dismissal = fields.Many2one(
        comodel_name='hr_ua_p2.kzot',
        string='Reason for dismissal')
