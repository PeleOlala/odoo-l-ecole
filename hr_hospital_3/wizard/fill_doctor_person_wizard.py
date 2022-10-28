from odoo import api, fields, models, _


class FillDoctorPerson(models.TransientModel):
    _name = "hr_hospital_3.fill_doctor_wizard"
    _discription = "Fill person doctor"

    name = fields.Char(
        string='Name'
    )
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_3.doctor',
        string='Doctor',
        required=True)
    patient_ids = fields.Many2many(
        comodel_name='hr_hospital_3.patient',
        string='List patient',
        required=False)

    @api.model
    def action_open_wizard(self):
        _wizard = self.create({})
        return _wizard._action_open_modal()

    def _action_open_modal(self):
        self.refresh()
        return {
            'name': _('Fill doctor personal'),
            'type': 'ir.actions.act_window',
            'res_model': 'hr_hospital_3.fill_doctor_wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
            'context': {'active_ids': self._context.get('active_ids', [])},
        }

    def action_fill(self):
        self.ensure_one()
        self.patient_ids = self.env['hr_hospital_3.patient'].browse(self.env.context.get('active_ids', []))
        for chaque in self.patient_ids:
            chaque.write({'doctor_personal_id': self.doctor_id.id})
