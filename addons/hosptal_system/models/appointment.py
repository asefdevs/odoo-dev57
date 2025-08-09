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

    def action_done(self):
        self.write({'status': 'done'})

    def action_change(self):
        for record in self:
            if record.status == 'draft':
                record.status = 'confirmed'
            elif record.status == 'confirmed':
                record.status = 'done'
            elif record.status == 'done':
                record.status = 'cancelled'
            elif record.status == 'cancelled':
                record.status = 'draft'

    