import datetime
from odoo import api, fields, models


class ResUserExt(models.Model):
    _inherit = 'res.users'

    stag_curient_date = fields.Datetime(
        compute="_comp_curient_date")

    def _comp_curient_date(self):
        for card in self:
            card.stag_curient_date = \
                datetime.date.today()-datetime.timedelta(days=30)
