from odoo import api, fields, models

class Maladie(models.Model):
    _name = 'hr_hospital.malade'
    _description = 'Malades'

    name = fields.Char()
    malade_class_id = fields.Many2one(
        comodel_name='hr_hospital.malade.class',
        string='le class',
        required=False)

class MaladieClass(models.Model):
    _name = 'hr_hospital.malade.class'
    _description = 'Catalog malades'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_nom'
    _order = 'complete_nom'

    name = fields.Char()
    complete_nom = fields.Char(
        'Complete Name', compute='_compute_complete_name',
        store=True)
    parent_id = fields.Many2one('hr_hospital.malade.class', 'Parent Class', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('hr_hospital.malade.class', 'parent_id', 'Child Class')
    malade_ids = fields.One2many(comodel_name='hr_hospital.malade', inverse_name='id')



