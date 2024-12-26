from odoo import models, fields


class HrHospitalDiseases(models.Model):
    _name = 'hr.hospital.diseases'
    _description = 'HR Hospital Diseases'

    id = fields.Integer()
    name = fields.Char()
    active = fields.Boolean()
    description = fields.Text()
