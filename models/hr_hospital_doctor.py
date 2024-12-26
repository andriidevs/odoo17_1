from odoo import models, fields


class HrHospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'HR Hospital Doctor'

    id = fields.Integer()
    name = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    active = fields.Boolean()
    description = fields.Text()
    hr_hospital_diseases_id = fields.Many2one(
        'hr.hospital.diseases',
        string = "Diseas"
    )

