import time

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Doctor(models.Model):
    _name = 'hr_hospital_4.doctor'
    _description = 'Doctor'

    name = fields.Char()
    specialiste = fields.Char(
        string='Doctor',
        required=False)


class DoctorExt3(models.Model):
    _name = 'hr_hospital_4.doctor'
    _description = 'MedecinExt3'
    _inherit = ['hr_hospital_4.personne', 'hr_hospital_4.doctor']
    _rec_name = 'name'

    intern = fields.Boolean(string="Intern",
                            default=False,
                            required=False,
                            compute='_compute_intern',
                            readonly=False, store=True)

    mentor_id = fields.Many2one(
        comodel_name='hr_hospital_4.doctor',
        domain="[('intern', '=', False)]",
        string='Doctor mentor',
        required=False
    )
    patient_declaration_ids = fields.One2many(
        comodel_name='hr_hospital_4.patient',
        inverse_name='doctor_personal_id',
        string='Mes patients',
        auto_join=True)
    intern_ids = fields.One2many(
        comodel_name='hr_hospital_4.doctor',
        inverse_name='mentor_id',
        string='Mes intern',
        auto_join=True)

    @api.depends('mentor_id')
    def _compute_intern(self):
        for cadr in self:
            cadr.intern = (cadr.mentor_id)

    @api.constrains("intern")
    def _chang_intern(self):
        for card in self:
            if card.intern and not card.mentor_id:
                raise UserError(_('First fill mentor'))
            elif not card.intern and card.mentor_id:
                raise UserError(_('Erase field mentor or put intern.'))
