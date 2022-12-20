import datetime
import calendar
from odoo import api, fields, models, _


class ResumeLineXt(models.Model):
    """
        C'est une classe heritage qui exsiste pour ajouter de nouvelles propriétés.
    """
    _inherit = 'hr.resume.line'
    _description = 'Labor stage for Ukraine'

    stage_year = fields.Integer(
        string='Stage year', compute='_compute_stage')
    stage_month = fields.Integer(
        string='month', compute='_compute_stage')
    stage_day = fields.Integer(
        string='day', compute='_compute_stage')
    stage_text = fields.Char(
        string='Stage text', compute='_compute_stage')
    diploma = fields.Char(
        string='Diploma', help='number & seria')
    specialty = fields.Char(
        string='specialty', help='Specialty profession')
    qualification = fields.Char(
        string='Qualification', help='Qualification of diploma')
    forma_ed = fields.Selection(
        string='Forma education',
        selection=[('daytime', _('Daytime')),
                   ('evening', _('Evening')), ('correspondence', _('Correspondence'))],
        required=False, )

    is_education = fields.Boolean(
        string='This is education', compute='_compute_ed')

    @api.depends('date_end')
    def _compute_stage(self):
        for card in self:
            date1 = card.date_start
            date_ah = card.date_end
            if isinstance(date_ah, datetime.date):
                days = calendar.monthrange(date1.year, date1.month)[1]
                card.stage_year = (date_ah.year - date1.year - 1) + (
                        date_ah.month + 12 - date1.month - 1
                        + (date_ah.day + days - date1.day) // days) // 12
                card.stage_month = (date_ah.month + 12 - date1.month - 1 + (
                        date_ah.day + days - date1.day) // days) % 12
                card.stage_day = (date_ah.day + days - date1.day) % days
                card.stage_text = "Stage {d1} year {d2} month {d3} days".format(d1=card.stage_year,
                                                                                d2=card.stage_month,
                                                                                d3=card.stage_day)
            else:
                card.stage_year, card.stage_month, card.stage_day = 0, 0, 0
                card.stage_text = 'Current'

    @api.depends('line_type_id')
    def _compute_ed(self):
        for card in self:
            card.is_education = (card.line_type_id == self.env.ref('hr_skills.resume_type_education'))
