from odoo import models, fields

class Appointment(models.Model):
    _inherit = 'mail.thread'
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True, tracking=True)
    note = fields.Text(string='Notes', tracking=True)
