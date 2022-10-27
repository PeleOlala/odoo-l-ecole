from odoo import api, fields, models

class medecins(models.Model):
    _name = 'hr_hospital.medecin'
    _description = 'Les Medecins'

    name = fields.Char()
    specialiste = fields.Char(
        string='Médecin',
        required=False)

class MedecinExt3(models.Model):
    _name = 'hr_hospital.medecin'
    _description = 'MedecinExt3'
    _inherit = ['hr_hospital.personne', 'hr_hospital.medecin']
    _rec_name = 'name'

    intern = fields.Boolean(string="L'elevant", default=False, required=False, compute='_compute_intern', readonly=False, store=True)

    mentor_id = fields.Many2one(
        comodel_name='hr_hospital.medecin',
        domain="[('intern', '=', False)]",
        string='Le medecin mentor',
        required=False
    )

    @api.depends('mentor_id')
    def _compute_intern(self):
        for cadr in self:
            cadr.intern=(cadr.mentor_id!=None)







