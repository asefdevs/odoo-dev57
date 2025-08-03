from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class Appointment(models.Model):
    _inherit = 'mail.thread'
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _rec_name = 'name'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default="NEW")
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True, tracking=True)
    note = fields.Text(string='Notes', tracking=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'NEW') == 'NEW':
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or 'NEW'
        return super(Appointment, self).create(vals)

    def action_confirm(self):
        self.write({'status': 'confirmed'})

    