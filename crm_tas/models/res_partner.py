# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

# Codigos de Descuento
class ResPartnerCode(models.Model):
    _name = 'res.partner.code'
    _description = "Códigos de Descuento"
    name = fields.Char(string='Code')
    crm_code_ids = fields.One2many('crm.lead','code_ids', string='Iniciativas/Oportunidades')
    
class ResPartner(models.Model):
    _inherit = 'res.partner'

    #seller code relaciona los codigos de descuento
    seller_code = fields.Char(string='Codigo Vendedor')
    res_partner_description = fields.Text(string='Descripción')
    tenant = fields.Char(string='Tenant')
    dni_ruc = fields.Char(string='DNI RUC')
    age = fields.Integer(string='Edad', tracking=True)
    age_date = fields.Date(string='Fecha de Nacimiento', tracking=True)
    city_id = fields.Char(string='Ciudad ID', tracking=True)
    client_name = fields.Char(string='Nombre de Cliente')
    client_surname = fields.Char(string='Apellido de Cliente')
    is_provider = fields.Boolean('Proveedor?')
