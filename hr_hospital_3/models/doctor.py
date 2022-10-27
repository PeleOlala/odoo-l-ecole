from odoo import api, fields, models


class Doctor(models.Model):
    _name = 'hr_hospital_3.doctor'
    _description = 'Doctor'

    name = fields.Char()
    specialiste = fields.Char(
        string='Doctor',
        required=False)

class DoctorExt3(models.Model):
    _name = 'hr_hospital_3.doctor'
    _description = 'MedecinExt3'
    _inherit = ['hr_hospital_3.personne', 'hr_hospital_3.doctor']
    _rec_name = 'name'

    intern = fields.Boolean(string="Intern", default=False, required=False, compute='_compute_intern', readonly=False, store=True)

    mentor_id = fields.Many2one(
        comodel_name='hr_hospital_3.doctor',
        domain="[('intern', '=', False)]",
        string='Doctor mentor',
        required=False
    )

    @api.depends('mentor_id')
    def _compute_intern(self):
        for cadr in self:
            cadr.intern=(cadr.mentor_id!=None)
