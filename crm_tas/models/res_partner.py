# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

# Codigos de Descuento
class ResPartnerCode(models.Model):
    #nombre del objeto
    _name = 'res.partner.code'
    #nombre a visualizar
    _description = "Códigos de Descuento"
    name = fields.Char(string='Code')
    
class ResPartner(models.Model):
    _inherit = 'res.partner'
    code_id = fields.Many2many('res.partner.code', string='Code')