"""
jamais
"""

import datetime
from odoo import fields, models


class PersonneIdentifi(models.AbstractModel):
    _name = 'hr_hospital_3.personne'
    _description = 'Identifie personne'

    last_name = fields.Char(
        string='Last name',
        required=True)
    telephone = fields.Char(
        string='Telephone',
        required=False)
    email = fields.Char(
        string='Email',
        required=False)
    sex = fields.Selection(
        string='Sex',
        selection=[('masculin', 'Masculin'),
                   ('féminin', 'Féminin'), ('indécis', 'Indécis')],
        required=False, translate=True)
    photo = fields.Image(string="Photo", max_width=1920, max_height=1920)

# якщо ви це читаєте, то хочу сказати, що в вас помилка в вікторині 3.2
# питання 4. всі запропановані вами моделі - всі є корректними з точки
# зору коди. жоден з них не дає помилки!!!!! працюють всі
# скажу даже більше, що використовувала атрибут inverse для не компьюте
# поля та все було добре.
# чому тоді перша модель не корректна?
# Залишу тут, хай повисить.


class MyModel1(models.Model):
    _name = 'my.model1'
    birthday = fields.Date(inverse='_inverse_compute_birthday')

    def _inverse_compute_birthday(self):
        for card in self:
            card.birthday = datetime.date.today()


class MyModel2(models.Model):
    _name = 'my.model2'
    birthday = fields.Date(compute='_compute_birthday', inverse='_inverse_compute_birthday')

    def _inverse_compute_birthday(self):
        pass

    def _compute_birthday(self):
        pass


class MyModel3(models.Model):
    _name = 'my.model3'
    birthday = fields.Date(compute='_compute_birthday', inverse='_inverse_compute_birthday'
                           , compute_sudo=True, )

    def _inverse_compute_birthday(self):
        pass

    def _compute_birthday(self):
        pass
