from datetime import datetime
from odoo.exceptions import AccessError
from odoo.addons.hr_ua_p2.tests.common import TestHrUACommon
from odoo.tests import new_test_user, tagged


@tagged('post_install', '-at_install')
class TestAccessRight(TestHrUACommon):

    @classmethod
    def setUpClass(cls):
        super(TestAccessRight, cls).setUpClass()

    def test_01_access_right(self):
        self.richard = new_test_user(self.env, login='ric', groups='base.group_user', name='Simple employee',
                                     email='ric@example.com')
        with self.assertRaises(AccessError):
            self.env['hr_ua_p2.family'].with_user(self.richard).create({
                'name': 'Nom test',
                'relation': 'child',
                'birthday': datetime.strptime('2015-11-01', '%Y-%m-%d').date(),
                'sex': 'féminin',
                'employee_id': self.employee.id

            })
