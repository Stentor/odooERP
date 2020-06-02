# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

# Create model Channel
class crmLeadChannel(models.Model):
    _name = 'crm.lead.channel'
    _description = "Canales"
    name = fields.Char(string='Channel')
    

# Create Model Plan
class crmLeadPlan(models.Model):
    _name = 'crm.lead.plan'
    _description = "Planes"
    name = fields.Char(string='Plan')

# Create Model Media
class crmLeadMedia(models.Model):
    _name = 'crm.lead.media'
    _description = "Medio"
    name = fields.Char(string='Media')

# Create model Payment
class crmLeadPaymen(models.Model):
    _name = 'crm.lead.payment'
    _description = "Formas de Pago"
    name = fields.Char(string='Payment')

# Create model fraction payment
class crmLeadPaymenFraction(models.Model):
    _name = 'crm.lead.payment.fraction'
    _description = "Formas de Pago Fracción"
    name = fields.Char(string='Payment Fraction')

# Create Relationship Model
class crmLead(models.Model):
    _inherit = 'crm.lead'

    def _domain_crm(self):
        code = self.user_id.partner_id.seller_code
        code_ids = self.env['res.partner.code'].search([('name','ilike',code)])
        return [('id','in',code_ids._ids)]

    channel_id = fields.Many2one('crm.lead.channel', string='Channel')
    plan_id = fields.Many2one('crm.lead.plan', string='Plan')
    media_id = fields.Many2one('crm.lead.media', string='Media')
    payment_id = fields.Many2one('crm.lead.payment', string='Payment')
    payment_fraction_id = fields.Many2one('crm.lead.payment.fraction', string='Payment Fraction')
    code_ids = fields.Many2many('res.partner.code','crm_lead_rel_res_partner', 'code_partner_id', 'crm_lead_id', String="Codigos de Descuento", domain=_domain_crm)
    user = fields.Char(string='Usuarioi', help="Este campo es para tas-system")
    helpdesk_ids = fields.One2many('helpdesk.ticket','crm_lead_id', string="Casos")


    



    

    