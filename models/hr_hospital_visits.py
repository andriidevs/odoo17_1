from odoo import models, fields

class HrHospitalVisits(models.Model):
    _name = 'hr.hospital.visits'
    _description = 'HR Hospital Visits'

    id = fields.Integer()
    date = fields.Datetime()
    hr_patient_id = fields.Many2one(comodel_name='hr.hospital.patient', string='HR Patient')
    hr_doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', string='HR Doctor')