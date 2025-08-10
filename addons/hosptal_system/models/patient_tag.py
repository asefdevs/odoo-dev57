from odoo import models, fields, api

class PatientTag(models.Model):
    _name = 'hospital.patient.tag'
    _description = 'Hospital Patient Tag'
    _rec_name = 'name'

    name = fields.Char(string='Tag Name', required=True)
    
    