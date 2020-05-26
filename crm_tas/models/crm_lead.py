# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

# Create model Channel
class crmLeadChannel(models.Model):
    _name = 'crm.lead.channel'
    _description = "Canales"
    name = fields.Char(string='Channel')

# Create Relationship Model
class crmLead(models.Model):
    _inherit = 'crm.lead'
    channel_id = fields.Many2one('crm.lead.channel', string='Channel')

# Create Model Plan
class crmLeadPlan(models.Model):
    _name = 'crm.lead.plan'
    _description = "Planes"
    name = fields.Char(string='Plan')
    
class crmLead(models.Model):
    _inherit = 'crm.lead'
    plan_id = fields.Many2one('crm.lead.plan', string='Plan')

# Create Model Medium
class crmLeadMedium(models.Model):
    _name = 'crm.lead.medium'
    _description = "Medios"
    name = fields.Char(string='Medium')
    
class crmLead(models.Model):
    _inherit = 'crm.lead'
    medium_id = fields.Many2one('crm.lead.medium', string='Medium')

# Create model Payment
class crmLeadPaymen(models.Model):
    _name = 'crm.lead.payment'
    _description = "Formas de Pago"
    name = fields.Char(string='Payment')

# Create Relationship Model    
class crmLead(models.Model):
    _inherit = 'crm.lead'
    payment_id = fields.Many2one('crm.lead.payment', string='Payment')


# Create model fraction payment
class crmLeadPaymenFraction(models.Model):
    _name = 'crm.lead.payment.fraction'
    _description = "Formas de Pago Fracción"
    name = fields.Char(string='Payment Fraction')

# Create Relationship Model    
class crmLead(models.Model):
    _inherit = 'crm.lead'
    payment_id = fields.Many2many('crm.lead.payment.fraction', string='Payment Fraction')