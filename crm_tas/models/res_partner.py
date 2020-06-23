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
    res_partner_child_crm_lead_ids = fields.One2many('crm.lead.payment','res_partner_id', string='Pasajeros x Opp')

# relacion tabla intermedia entre candidatos y contacto
class ResPartnerChildCrmLead(models.Model):
    _name = 'res.partner.child.crm.lead'
    _description = "Tabla Intermedia entre Contactos y Leads"
    name = fields.Char(string='Leads And Partners')
    crm_lead_id = fields.Many2one('crm.lead', string='Lead')
    res_partner_id = fields.Many2one('res.partner', string='Contacto')
    is_parent = fields.Boolean('Principal?')