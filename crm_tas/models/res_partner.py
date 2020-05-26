# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

# Codigos de Descuento
class ResPartnerCode(models.Model):
    _name = 'res.partner.code'
    _description = "Códigos de Descuento"
    name = fields.Char(string='Code')
    
class ResPartner(models.Model):
    _inherit = 'res.partner'
    code_id = fields.Many2many('res.partner.code', string='Code')