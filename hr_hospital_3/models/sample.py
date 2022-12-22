"""
jamais
"""

from odoo import fields, models


class Sample(models.Model):
    """
2
    """
    _name = 'hr_hospital_3.sample'
    _description = 'Samples'

    name = fields.Char()
