from odoo import fields, models


class KZOTUAArticles(models.Model):
    """
    Il s'agit une classe nouvelle
    """
    _name = 'hr_ua_p2.kzot'
    _description = 'Articles KZOT UA'

    name = fields.Char(string="Article's full name")
    article = fields.Char(string="Article's code")
    active = fields.Boolean(default=True)
