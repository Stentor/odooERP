# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

# Codigos de Descuento
class ResPartnerCode(models.Model):
    _name = 'res.partner.code'
    _description = "Códigos de Descuento"
    name = fields.Char(string='Code')
    crm_code_ids = fields.One2many('crm.lead','code_ids', string='Codigo')
    
class ResPartner(models.Model):
    _inherit = 'res.partner'
    code_id = fields.Char(string='Code')
    abbreviation_code = fields.Char(string='Código', help='Codigo de Vendedor para los codigos de descuento')
    description_resparter = fields.Text(string='Código')
