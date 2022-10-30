from odoo import fields, models


class Sample(models.Model):
    _name = 'hr_hospital_4.sample'
    _description = 'Samples'

    name = fields.Char()
