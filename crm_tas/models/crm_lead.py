# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

REASON_TRIP_SELECTION = [
    ('Turismo','Turismo'),
    ('Estudios','Estudios'),
    ('Trabajo','Trabajo'),
    ('Calamidad','Calamidad'),
    ('Reagrupacion','Reagrupacion'),
    ('Negocios','Negocios')
]

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
    # var_prueba =  fields.char(string='Campo Prueba')



    #@api.depends('user_id.partner_id')
    #@api.onchange('user_id')
    #def _domain_crm(self):
    #    code = self.user_id.partner_id.seller_code
    #    code_obj = self.env['res.partner.code']
    #    code_ids = code_obj.search([('name','ilike',code)])
    #    return [('id','in',code_ids._ids)]



    #campos relacionados
    channel_id = fields.Many2one('crm.lead.channel', string='Channel')
    plan_id = fields.Many2one('crm.lead.plan', string='Planes')
    media_id = fields.Many2one('crm.lead.media', string='Media')
    payment_id = fields.Many2one('crm.lead.payment', string='Formas de Pago')
    payment_fraction_id = fields.Many2one('crm.lead.payment.fraction', string='Payment Fraction')
    helpdesk_ids = fields.One2many('helpdesk.ticket','crm_lead_id', string="Casos")
    #campos con dominio
    code_ids = fields.Many2many('res.partner.code','crm_lead_rel_res_partner', 'code_partner_id', 'crm_lead_id', String="Codigos de Descuento")
    #otros campos
    user = fields.Char(string='UsuarioTS', help="Este campo es para tas-system")
    #Información del Viaje
    destination_country = fields.Char(string='Destino')
    is_usa = fields.Boolean('Destino es USA?')
    passenger_number = fields.Char(string='Nro Pasajeros')
    tenant_bd_id = fields.Char(string='ID BD', help="Este campo es identificador de tenant para tas-system")
    certificate_number = fields.Char(string='Certificado')
    status = fields.Integer(string='Estado')
    code_promotion = fields.Char(string='Codigo Web')
    code_discount = fields.Char(string='Codigo Manual')
    no_preexistence = fields.Boolean('Sin Preexistencia?')
    departure_date = fields.Date(string='Fecha de Salida')
    return_date = fields.Date(string='Fecha de Retorno')
    coverage_days = fields.Integer(string="Dias cubiertos", compute="calcule_days")
    @api.depends('departure_date','return_date')
    def calcule_days(self):
        for s in self:
            if s.return_date & s.departure_date:
                s.coverage_days = abs(s.return_date - s.departure_date).days
            else:
                s.coverage_days = 0
    initial_price = fields.Float(string='Precio Inicial', digits=(16,2))
    price_quote = fields.Float(string='Precio Cotización', digits=(16,2))
    #Asegurado y Pagos
    is_insurance = fields.Boolean('Asegurado?')
    sales_date = fields.Date(string='Fecha de Venta')
    paypal_reference = fields.Char(string='Referencia de Venta Paypal')
    payu_account = fields.Char(string='Cuenta Payu')
    order_payu = fields.Char(string='Orden Payu')
    payment_reference = fields.Char(string='Referencia de Pago')
    is_portfolio_recovery = fields.Boolean(string='Recuperación de Cartera?', help='Pago mayor a 45 dias')
    
    insurance_price = fields.Float(string='Precio Seguro', digits=(16,2))
    lead_source = fields.Char(string='Lead Source')
    web_site = fields.Char(string='Sitio Web')
    is_subscription = fields.Boolean('Suscrito a Newsletter?')
    reason_trip = fields.Selection(REASON_TRIP_SELECTION, string='Motivo de Viaje')
    
    luggage = fields.Boolean('Cobertura Equipaje?')
    pet = fields.Boolean('Cobertura Mascotas?')
    sport = fields.Boolean('Cobertura Deportes?')
    frequent_flyer = fields.Boolean('Cobertura Viajero Frecuente?')
    pregnancy = fields.Boolean('Cobertura Embarazo?')
    flight_cancellation = fields.Boolean('Cobertura Cancelación Vuelo?')
    damage_third_party =  fields.Boolean('Cobertura Daños a Terceros?')
    flight_delay =  fields.Boolean('Cobertura Retraso de Vuelo?')
    psychological_assistance =  fields.Boolean('Cobertura Asistencia Psicologica?')
    concierge = fields.Boolean('Cobertura Concierge?')
    plus = fields.Boolean('Plus?')
    luggage_plus = fields.Boolean('Equipaje Plus?')
    denial_visa = fields.Boolean('Negación de Visa?')
    adisa = fields.Boolean('ADISA?')
    tech_protection = fields.Boolean('Cobertura Tech Protection?')
    ded200 = fields.Boolean('Deducible 200?')
    pet_name = fields.Char(string='Nombre Mascota')
    pet_breed = fields.Char(string='Raza Mascota')
    pet_age = fields.Char(string='Edad Mascota')
    pet_type = fields.Char(string='Tipo Mascota')
    per_address = fields.Char(string='Residencia Mascota')
    purchase_status = fields.Char(string='Estado de Compra')
    other_payment = fields.Text(string='Observaciones de Pago')
    additional_information = fields.Text(string='Información Adicional')
    schedule_date = fields.Date(string='Fecha Programada')
    
    #para usar un campo relacionado se debe llamar al campo relacion 
    #por lo general termina en _id o _ids y luego al campo a llamar
    partner_seller_code = fields.Char(related="user_id.seller_code")

    def create_helpdesk(self):
        return {
            'type':'ir.actions.act_window',
            'name':'Caso',
            'res_model':'helpdesk.ticket',
            'view_mode':'form',
            'target':'new',
            'context':'{"default_crm_lead_id":%s, "default_partner_id":%s}' %(self.id, self.partner_id.id)
        }




    

    