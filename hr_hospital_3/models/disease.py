from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class Disease(models.Model):
    _name = 'hr_hospital_3.disease'
    _description = 'disease'

    name = fields.Char()
    disease_catalog_id = fields.Many2one(
        comodel_name='hr_hospital_3.disease_catalog',
        string='Catalog',
        required=False)

class DiseaseCatalog(models.Model):
    _name = 'hr_hospital_3.disease_catalog'
    _description = 'Catalog disease'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char()
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name',
        store=True)
    parent_id = fields.Many2one('hr_hospital_3.disease_catalog', 'Parent catalog', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('hr_hospital_3.disease_catalog', 'parent_id', 'Child Class')
    disease_count = fields.Integer(
        '# disease', compute='_compute_disease_count',
        help="The number of disease under this category (Does not consider the children categories)")
    disease_ids = fields.One2many(comodel_name='hr_hospital_3.disease', inverse_name='id')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_disease_count(self):
        read_group_res = self.env['hr_hospital_3.disease'].read_group([('disease_catalog_id', 'child_of', self.ids)], ['disease_catalog_id'], ['disease_catalog_id'])
        group_data = dict((data['disease_catalog_id'][0], data['disease_catalog_id_count']) for data in read_group_res)
        for categ in self:
            disease_count = 0
            for sub_categ_id in categ.search([('id', 'child_of', categ.ids)]).ids:
                disease_count += group_data.get(sub_categ_id, 0)
            categ.disease_count = disease_count

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]

    def name_get(self):
        if not self.env.context.get('hierarchical_naming', True):
            return [(record.id, record.name) for record in self]
        return super().name_get()
