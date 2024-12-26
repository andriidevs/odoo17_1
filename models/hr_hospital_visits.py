from odoo import models, fields


class HrHospitalVisits(models.Model):
    _name = 'hr.hospital.visits'
    _description = 'HR Hospital Visits'

    id = fields.Integer()
    date = fields.Datetime()
    hr_patient_id = fields.Many2one('hr.patient', string='HR Patient')
    hr_doctor_id = fields.Many2one('hr.doctor', string='HR Doctor')
