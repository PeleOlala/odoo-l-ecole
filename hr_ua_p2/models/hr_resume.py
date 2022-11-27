import datetime
import calendar
from odoo import api, fields, models


class ResumeLineXt(models.Model):
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

    @api.depends('date_end')
    def _compute_stage(self):
        for card in self:
            date1 = card.date_start
            date_ah = card.date_end
            if isinstance(date_ah, datetime.date):
                days = calendar.monthrange(date1.year, date1.month)[1]
                card.stage_year = (date_ah.year - date1.year - 1) + (
                        date_ah.month + 12 - date1.month - 1 + (date_ah.day + days - date1.day) // days) // 12
                card.stage_month = (date_ah.month + 12 - date1.month - 1 + (
                        date_ah.day + days - date1.day) // days) % 12
                card.stage_day = (date_ah.day + days - date1.day) % days
                card.stage_text = 'Stage %d year %d month %d days' % (card.stage_year, card.stage_month, card.stage_day)
            else:
                card.stage_year, card.stage_month, card.stage_day = 0, 0, 0
                card.stage_text = 'Current'
