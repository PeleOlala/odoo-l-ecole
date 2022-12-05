from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProfessionClassifier(models.Model):
    _name = "hr_ua_p2.profession_classifier"
    _description = "Profession Classifier UA"

    name = fields.Char('Name')
    code = fields.Char('Name')
    profession_classifier_catalog_id = fields.Many2one(
        comodel_name='hr_ua_p2.profession_classifier_catalog',
        string='Catalog',
        required=False)


class ProfessionClassifierCatalog(models.Model):
    _name = 'hr_ua_p2.profession_classifier_catalog'
    _description = 'Catalog Profession Classifier UA'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char()
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name',
        store=True, recursive=True)
    parent_id = fields.Many2one('hr_ua_p2.profession_classifier_catalog',
                                'Parent catalog', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('hr_ua_p2.profession_classifier_catalog', 'parent_id', 'Child Class')
    pc_count = fields.Integer(
        '# Profession Classifier', compute='_compute_ps_count',
        help="The number of Profession Classifier under this category (Does not consider the children categories)")
    profession_classifier_ids = fields.One2many(
        comodel_name='hr_ua_p2.profession_classifier', inverse_name='profession_classifier_catalog_id')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_pc_count(self):
        read_group_res = self.env['hr_ua_p2.profession_classifier'].read_group(
            [('profession_classifier_catalog_id', 'child_of', self.ids)],
            ['profession_classifier_catalog_id'], ['profession_classifier_catalog_id'])
        group_data = dict(
            (data['profession_classifier_catalog_id'][0], data['profession_classifier_catalog_count'])
            for data in read_group_res)
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


class JobPositionUA(models.Model):
    _inherit = 'hr.job'

    code_kp_id = fields.Many2one(
        comodel_name='hr_ua_p2.profession_classifier',
        string='profession classifier')
