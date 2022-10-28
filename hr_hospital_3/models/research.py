from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ResearchCatalog(models.Model):
    _name = 'hr_hospital_3.research_catalog'
    _description = 'Catalog research'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char()
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name',
        store=True)
    parent_id = fields.Many2one('hr_hospital_3.research_catalog', 'Parent catalog', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('hr_hospital_3.research_catalog', 'parent_id', 'Child Class')
    research_count = fields.Integer(
        '# research', compute='_compute_research_count',
        help="The number of reseach under this category (Does not consider the children categories)")
    research_ids = fields.One2many(
        comodel_name='hr_hospital_3.research',
        inverse_name='research_catalog_id',
        string='Groupe research')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_research_count(self):
        read_group_res = self.env['hr_hospital_3.research'].read_group([('research_catalog_id', 'child_of', self.ids)], ['research_catalog_id'], ['research_catalog_id'])
        group_data = dict((data['research_catalog_id'][0], data['research_catalog_id_count']) for data in read_group_res)
        for categ in self:
            research_count = 0
            for sub_categ_id in categ.search([('id', 'child_of', categ.ids)]).ids:
                research_count += group_data.get(sub_categ_id, 0)
            categ.research_count = research_count

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


class Research(models.Model):
    _name = 'hr_hospital_3.research'
    _description = 'research'

    name = fields.Char()
    patient_id = fields.Many2one(
        comodel_name='hr_hospital_3.patient',
        string='Patient',
        required=True)
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital_3.doctor',
        string='Doctor',
        required=False
    )
    patient_card_id = fields.Many2one(
        comodel_name='hr_hospital_3.patient_card',
        string='Visit doctor',
        domain="['&',('doctor_id', '=', doctor_id),('patient_id','=',patient_id)]",
        required=False
    )
    sample_id = fields.Many2one(
        comodel_name='hr_hospital_3.sample',
        string='',
        required=False)
    research_catalog_id = fields.Many2one(
        comodel_name='hr_hospital_3.research_catalog',
        string='Catalog research',
        required=False)
