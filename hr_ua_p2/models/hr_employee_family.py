import datetime
from odoo import api, fields, models, _


class FamilyEmployee(models.Model):
    _name = 'hr_ua_p2.family'
    _description = 'Family members'
    """
    Family status
    """

    name = fields.Char()
    relation = fields.Selection(
        string='Relation degree',
        selection=[('child', 'Child'),
                   ('spouse', 'Spouse'),
                   ('parents', 'Parents'),
                   ('brother-sister', 'Brother-Sister')])
    birthday = fields.Date(
        string='Birthday')
    age = fields.Integer(
        string="Age",
        compute='_compute_age')
    sex = fields.Selection(
        string='Sex',
        selection=[('masculin', _('Masculin')),
                   ('féminin', _('Féminin')), ('indécis', _('Indéc'))])
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee')

    @api.depends('birthday')
    def _compute_age(self):
        for card in self:
            date1 = card.birthday
            date_ah = datetime.date.today()
            if isinstance(date1, datetime.date):
                card.age = (date_ah.year - date1.year - 1) + (date_ah.month + 12 - date1.month) // 12
            else:
                card.age = 0


