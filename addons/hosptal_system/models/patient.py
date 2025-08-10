from odoo import models, fields, api

class Patient(models.Model):
    _inherit = 'mail.thread'
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name', required=True, tracking=True)
    age = fields.Integer(string='Age', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='other', tracking=True)
    patient_tag_ids = fields.Many2many(
        'hospital.patient.tag',
        string='Tags',
        help='Tags to categorize the patient'
    )