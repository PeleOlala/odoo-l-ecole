from odoo import fields, models


class Patient(models.Model):  # Перед класом потрібно залишати 2 рядки.
    _name = 'hr_hospital_2.patient'
    _description = 'Patient'

    name = fields.Char(
       string='Last name'
    )
    insurance = fields.Char(
        string="insurance",
        required=False)
    date_birthday = fields.Date(
        string='Birthday',
        required=True)
    sex = fields.Selection(
        string='Sex',
        selection=[('male', 'Male'),
                   ('femail', 'Femail'), ('other', 'Other')],
        required=False, )
    passport = fields.Char(
        string='Passport',
        required=False)
    personne_contact = fields.Char(
        string='Personne de contact',
        required=False)
    age = fields.Integer(
        string="Age")
