from odoo.tests import common


class TestHrUACommon(common.TransactionCase):

    def setUp(self):
        super(TestHrUACommon, self).setUp()

    @classmethod
    def setUpClass(cls):
            super(TestHrUACommon, cls).setUpClass()

            cls.employee = cls.env['hr.employee'].create({
                'name': 'Richard',
                'gender': 'male',
                'country_id': cls.env.ref('base.ua').id,
            })

