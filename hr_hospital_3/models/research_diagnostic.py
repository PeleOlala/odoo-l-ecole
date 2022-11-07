"""
jamais
"""

from odoo import fields, models


class ResearchDiagnostic(models.Model):
    _name = 'hr_hospital_3.research_diagnostic'
    _description = 'relation research & diagnostic'

    name = fields.Char()
    diagnostic_id = fields.Many2many
    research_ids = fields.Many2many('hr.employee', 'employee_category_rel', 'category_id', 'emp_id', string='Employees')
