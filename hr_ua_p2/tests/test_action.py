from datetime import datetime
from odoo.addons.hr_ua_p2.tests.common import TestHrUACommon


class TestAddSkillsFamily(TestHrUACommon):

    @classmethod
    def setUpClass(cls):
        super(TestAddSkillsFamily, cls).setUpClass()

    def test_stage_year(self):
        start = datetime.strptime('2015-11-01', '%Y-%m-%d').date()
        end = datetime.strptime('2020-11-01', '%Y-%m-%d').date()
        recored = self.env['hr.resume.line'].create({
            'name': 'Contract',
            'employee_id': self.employee.id,
            'date_start': start,
            'date_end': end,
            'line_type_id': self.env.ref('hr_skills.resume_type_experience').id
        })
        self.assertEqual(recored.stage_year, 5)
        self.assertEqual(recored.stage_month, 0)
        self.assertEqual(recored.stage_day, 0)
        self.assertEqual(recored.stage_text,
                         'Stage %d year %d month %d days' % (5, 0, 0))

    def create_member_family(self, nom, sex, birthday, rel):
        return self.env['hr_ua_p2.family'].create({
            'name': nom,
            'relation': rel,
            'birthday': birthday,
            'sex': sex,
            'employee_id': self.employee.id
        })

    def test_compt_enfans(self):
        self.create_member_family('Luisa Ferra', 'féminin',
                                 datetime.strptime('2015-11-01', '%Y-%m-%d').date(), 'child')
        self.create_member_family( 'Martin Ferra', 'masculin',
                                 datetime.strptime('2002-11-01', '%Y-%m-%d').date(),
                                 'child')
        self.create_member_family('Fabrisia Ferra', 'féminin',
                                 datetime.strptime('1985-02-28', '%Y-%m-%d').date(),
                                 'spouse')
        self.create_member_family('PaticiaFerra', 'féminin',
                                 datetime.strptime('2015-07-03', '%Y-%m-%d').date(), 'brother-sister')
        self.assertEqual(self.employee.children, 1)
