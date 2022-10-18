from odoo import api, fields, models

class Malade(models.Model):
    _name = 'hr_hospital.malade'
    _description = 'Les malades'

    name = fields.Char()


