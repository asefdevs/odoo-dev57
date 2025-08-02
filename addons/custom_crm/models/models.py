import odoo
from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'  
    short_note = fields.Char(string='Short Note')

