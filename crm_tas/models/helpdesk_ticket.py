# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

# Create Model GOPS
class HelpdeskTicketGOP(models.Model):
    #nombre del objeto
    _name = 'helpdesk.ticket.gop'
    #nombre a visualizar
    _description = "GOPS"
    name = fields.Char(string='GOPS')
    code = fields.Char(string='Codigo de GOP')
    
class ResPartner(models.Model):
    _inherit = 'res.partner'
    gop_id = fields.One2many('helpdesk.ticket.gop', string='GOP')