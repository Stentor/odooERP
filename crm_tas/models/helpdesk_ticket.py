# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime, date
from odoo.exceptions import ValidationError, UserError

#listas de seleccion fijas
SERVICE_TYPE_SELECTION = [
    ('Centro_Medico', 'Centro Médico'), 
    ('Consulta_con_Especialista', 'Consulta con Especialista'), 
    ('Laboratorio_clinico', 'Laboratorio clínico'),
    ('Medico_Domiciliario', 'Médico Domiciliario'),
    ('MayoMedios_diagnostico	', 'Medios diagnostico'),
    ('Odontologia', 'Odontología'),
    ('Repatriacion_Funeraria', 'Repatriación Funeraria'),
    ('Repatriacion_Sanitaria', 'Repatriación Sanitaria'),
    ('Tratamiento', 'Tratamiento'),
    ('Telemedico', 'Telemedico'),
    ('Interrupcion_de_viaje', 'Interrupcion de viaje'),
    ('Ambulancia', 'Ambulancia'),
    ('Consulta_externa', 'Consulta externa'),
    ('Videoconferencia', 'Videoconferencia')
]
MONTHS_SELECTION = [
    ('Enero', 'Enero'), 
    ('Febrero', 'Febrero'), 
    ('Marzo', 'Marzo'),
    ('Abril', 'Abril'),
    ('Mayo', 'Mayo'),
    ('Junio', 'Junio'),
    ('Julio', 'Julio'),
    ('Agosto', 'Agosto'),
    ('Septiembre', 'Septiembre'),
    ('Octubre', 'Octubre'),
    ('Noviembre', 'Noviembre'),
    ('Diciembre', 'Diciembre')
]
CLAIM_TYPE_SELECTION = [
    ('Sugerencia', 'Sugerencia'), 
    ('Peticion', 'Petición'), 
    ('Queja', 'Queja'), 
    ('Reclamo', 'Reclamo'), 
    ('Felicitacion', 'Felicitación')
]
RECEPTION_TYPE_SELECTION = [
    ('Correo_electronico', 'Correo electrónico'), 
    ('llamada_telefonica', 'llamada telefónica'), 
    ('WhatsApp', 'WhatsApp'), 
    ('Trustpilot', 'Trustpilot'), 
    ('Facebook', 'Facebook'), 
    ('TripAdvisor', 'TripAdvisor'), 
    ('Instagram', 'Instagram'), 
    ('Otro', 'Otro')
]
CONTACT_TYPE_SELECTION = [
    ('Telefonica', 'Telefonica'), 
    ('Correo_electronico', 'Correo electrónico'), 
    ('WhatsApp', 'WhatsApp'), 
    ('Otro', 'Otro')
]
Q_SERVICE_TYPE_SELECTION = [
    ('Telemedico', 'Telemedico'), 
    ('Coordinacion', 'Coordinacion'), 
    ('Reembolso', 'Reembolso')
]
CLASSIFICATION_SELECTION = [
    ('NA', 'N/A'), 
    ('Sugerencia', 'Sugerencia'), 
    ('Reclamo', 'Reclamo'), 
    ('Queja', 'Queja'), 
    ('Felicitacion', 'Felicitacion')
]
URGENCY_LEVEL_SELECTION = [
    ('0','0- no se coordina'),
    ('1','1- Telémédico'),
    ('2','2- Médico a domicilio'),
    ('3','3- Centro médico'),
    ('4','4- Hospitalización'),
    ('5','5- Repatriación'),
    ('6','6-Videoconferencia')
]
CASE_CLOSE_MOTIVE_SELECTION = [
    ('Pago_Reembolso','Pago de Reembolso'),
    ('Negacion_Rembolso','Negación de Rembolso'),
    ('Superacion_90_dias	','Superación de 90 días'),
    ('Falta_contacto','Falta de contacto con el cliente'),
    ('No_desea_reembolso','No desea reembolso')

]
TRACKING_TYPE_SELECTION = [
    ('Llamada', 'Llamada'), 
    ('WhatsApp', 'WhatsApp'), 
    ('Correo', 'Correo'), 
    ('Sirena', 'Sirena'),
    ('Interno', 'Interno'),
    ('Chat', 'Chat'),
    ('Skype', 'Skype')
]
CASE_STATE_SELECTION = [
    ('lote2','LOTE 2'),
    ('Distribuido','Distribuido'),
    ('Cerrado','Cerrado'),
    ('Nuevo','Nuevo'),
    ('Desembolsado','Desembolsado'),
    ('Documento_pendiente','Documento pendiente'),
    ('Proceso_reembolso','Proceso de reembolso'),
    ('Proceso_reembolso_medicamentos','Proceso de reembolso medicamentos'),
    ('Pendiente_informacion_bancaria	','Pendiente información bancaria'),
    ('Notificacion_cliente','Notificación del cliente'),
    ('lote1','LOTE 1'),
    ('Coordinacion','Coordinación'),
    ('Validacion','Validación'),
    ('Reembolsos_Complejos','Reembolsos Complejos'),
    ('Negaciones','Negaciones'),
    ('Formulario','Formulario'),
    ('SIN_VOBO','SIN VOBO'),
    ('COMODIN','COMODIN'),
    ('Pago_inmediato','Pago inmediato'),
    ('Caso_disputa','Caso en disputa'),
    ('CONTABILIDAD','CONTABILIDAD')
]
SERVICE_LEVEL_SELECTION = [
    ('No_coordina','No se coordina'),
    ('Telemedico','Telemédico'),
    ('Medico_domicilio','Médico a domicilio'),
    ('Exento_cobertura','Exento de cobertura'),
    ('Enfermera_domicilio','Enfermera a domicilio'),
    ('Centro_odontologico','Centro odontológico'),
    ('Centro_urgencia','Centro de urgencia'),
    ('Centro_medico','Centro médico'),
    ('Consulta_externa','Consulta externa'),
    ('Auto_asistencia','Auto asistencia'),
    ('Videoconferencia','Videoconferencia')
]
DISPUTED_CASE_SELECTION = [
    ('En_estudio','En estudio'),
    ('Negado','Negado'),
    ('Aprobado','Aprobado'),
    ('Aprobado_Parcialmente','Aprobado Parcialmente')
]
REFUND_TYPE_SELECTION = [
    ('Auto_asistencia','Auto asistencia'),
    ('Cancelacion_vuelo','Cancelación de vuelo'),
    ('Cancelacion_e_interrupcion_viaje	','Cancelación e interrupción del viaje'),
    ('Demora_de_equipaje','Demora de equipaje'),
    ('Gasto_medico','Gasto médico'),
    ('Ginecologico','Ginecologico'),
    ('Odontologia','Odontología'),
    ('Perdida_de_equipaje','Perdida de equipaje'),
    ('Perdida_de_Pasaporte','Perdida de Pasaporte'),
    ('Reagrupacion_familiar','Reagrupacion familiar'),
    ('Repatriacion_funeraria','Repatriacion funeraria'),
    ('Repatriacion_sanitaria','Repatriacion sanitaria'),
    ('Retraso_de_vuelo','Retraso de vuelo'),
    ('Transferencia_de_fondos','Transferencia de fondos'),
    ('Urologia','Urología'),
    ('Exceso_de_equipaje','Exceso de equipaje'),
    ('Embarazo','Embarazo'),
    ('Enfermedad_Preexistente','Enfermedad Pre-existente'),
    ('Protesis_Ortesis','Prótesis y Ortesis'),
    ('TECH_PROTECTION','TECH PROTECTION'),
    ('Pandemia','Pandemia')
]
CASE_PRIORITY_SELECTION = [
    ('Alta','Alta'),
    ('Media','Media'),
    ('Baja','Baja')
]
ASSIT_TYPE_SELECTION = [
    ('asistencia_medica','Asistencia médica'),
    ('fuera_cobertura','Fuera de cobertura'),
    ('repatriacion_traslado','Repatriación y traslado'),
    ('asistencia_equipaje','Asistencia Equipaje'),
    ('asistencia_viaje','Asistencia Viaje'),
    ('aux_asistencia_legal','Aux y Asistencia Legal')
]
COMMENT_SELECTION = [
    ('Reembolso','Reembolso'),
    ('Conciliacion','Conciliacion'),
    ('Proveedores','Proveedores'),
    ('Calidad','Calidad'),
    ('Coordinacion','Coordinación'),
    ('Seguimiento','Seguimiento')
]
ACCOUNT_TYPE_SELECTION = [
    ('Ahorro','AHORRO'),
    ('Corriente','CORRIENTE'),
    ('Tarjeta_de_Credito','Tarjeta de Crédito'),
    ('Cheques','CHEQUES'),
    ('Premium','Premium'),
    ('Smart_Premium','Smart Premium'),
    ('Cuneta_ON','Cuneta ON'),
    ('Debito_123_Smart','Débito 123 Smart'),
    ('Cuenta_Negocios','Cuenta Negocios'),
    ('NO_APLICA','NO APLICA'),
    ('Expansion','Expansión'),
    ('Cuenta_Vista','Cuenta Vista'),
    ('smart_access','smart access'),
    ('BASE','BASE'),
    ('Safe_Balance_account','Safe Balance account'),
    ('UNICA','UNICA'),
    ('Sin_nomina','Sin nómina'),
    ('Smart','Smart')
]
# MODELOS
# Create Model GOPS
class HelpdeskTicketGOP(models.Model):
    _name = 'helpdesk.ticket.gop'
    _description = "GOPS"

    name = fields.Char(string='GOPS')
    code = fields.Char(string='Codigo de GOP')
    amount = fields.Float(string='Monto', digits=(16,2), tracking=True)
    currency_id = fields.Many2one('res.currency', string="Moneda GOP", tracking=True)
    service_type = fields.Selection(SERVICE_TYPE_SELECTION, string='Tipo de Servicio', tracking=True)
    reference = fields.Text(string="Referencia GOP")
    medical_center_name = fields.Text(string="Nombre de Centro Médico")
    observation = fields.Text(string="Observaciones")
    asisst = fields.Selection([('si', 'SI'), ('no', 'NO'), ('autoasistencia', 'Autoasistencia')], string='Asistió')
    is_reviewed = fields.Boolean('Revisado?')
    is_paid = fields.Boolean('Pagado?')
    invoice_number = fields.Text(string="Número de Facturas")
    is_disputed = fields.Boolean('Disputa?')
    invoice_month = fields.Selection(MONTHS_SELECTION, string='Mes de Facturación')
    payment_month = fields.Selection(MONTHS_SELECTION, string='Mes de Pago')
    res_partner_id = fields.Many2one('res.partner', string="Proveedor", domain="[('is_provider','=','true')]")
    helpdesk_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Id")
    auto_id_gop = fields.Char(string='ID Gop')
    operator_id = fields.Many2one('helpdesk.ticket.operator', string="Operador", domain="[('is_active','=','true')]")
    #aplicación de secuencia
    @api.model
    def create(self, vals):
        vals['auto_id_gop'] = self.env['ir.sequence'].next_by_code(
                'sequence_gop') or 'New'
        result = super(HelpdeskTicketGOP, self).create(vals)
        return result

class HelpdeskTicketComment(models.Model):
    _name = 'helpdesk.ticket.comment'
    _description = "Comentarios"

    name = fields.Char(string='Comentarios')
    auto_id_comentario = fields.Char(string='ID Comentario')
    comment_type = fields.Selection(COMMENT_SELECTION, string='Tipo')
    comment_description = fields.Text(string="Descripcion")
    helpdesk_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Id")
    operator_id = fields.Many2one('helpdesk.ticket.operator', string="Operador", domain="[('is_active','=','true')]")
    #aplicación de secuencia
    @api.model
    def create(self, vals):
        vals['auto_id_comentario'] = self.env['ir.sequence'].next_by_code(
                'sequence_comment') or 'New'
        result = super(HelpdeskTicketComment, self).create(vals)
        return result
    

class HelpdeskTicketQuality(models.Model):
    _name = 'helpdesk.ticket.quality'
    _description = "Calidad"
    _rec_name = "claim_type"

    claim_type = fields.Selection(CLAIM_TYPE_SELECTION, string='Tipo De Reclamación')
    comments_date = fields.Date(string="Fecha de Recepción de comentario")
    reception_type = fields.Selection(RECEPTION_TYPE_SELECTION, string='Tipo De Recepción')
    claim_motive = fields.Text(string="Motivo de Reclamación")
    expend = fields.Float(string='Gasto Incurrido', digits=(16,2))
    cmments_delete = fields.Selection([('si', 'SI'), ('no', 'NO')], string='Eliminación / Cambio de comentario')
    helpdesk_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Id")
    auto_id_quality = fields.Char(string='ID Calidad')
    #aplicación de secuencia
    @api.model
    def create(self, vals):
        vals['auto_id_quality'] = self.env['ir.sequence'].next_by_code(
                'sequence_quality') or 'New'
        result = super(HelpdeskTicketQuality, self).create(vals)
        return result

class HelpdeskTicketQuiz(models.Model):
    _name = 'helpdesk.ticket.quiz'
    _description = "Encuesta"
    name = fields.Char(string='Encuestas')
    q_contact_type = fields.Selection(CONTACT_TYPE_SELECTION, string='Medio de contacto')
    q_service_type = fields.Selection(Q_SERVICE_TYPE_SELECTION, string='Tipo De Servicio')
    q_classification = fields.Selection(CLASSIFICATION_SELECTION, string='Clasificacion')
    q_observation = fields.Text(string='Eliminación / Cambio de comentario')
    helpdesk_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Id")
    q_subject = fields.Char(string='Asunto')
    q_is_email_survey = fields.Boolean('Encuesta por email?')
    q_is_wsp_survey = fields.Boolean('Encuesta por WSP?')
    auto_id_quiz = fields.Char(string='ID Encuesta')
    #aplicación de secuencia
    @api.model
    def create(self, vals):
        vals['auto_id_quiz'] = self.env['ir.sequence'].next_by_code(
                'sequence_quiz') or 'New'
        result = super(HelpdeskTicketQuiz, self).create(vals)
        return result

class HelpdeskTicketSubType(models.Model):
    _name = 'helpdesk.ticket.subtype'
    _description = "Subtipo"
    name = fields.Char(string='Sub Tipo')
    assist_type = fields.Selection(ASSIT_TYPE_SELECTION, string='Tipo de Asistencia')

class HelpdeskTicketOperator(models.Model):
    _name = 'helpdesk.ticket.operator'
    _description = "Operador"
    name = fields.Char(string='Nombre del Operador')
    is_active = fields.Boolean('Activo?')
    is_coordinator = fields.Boolean('Coordinador?')
    helpdesk_ids = fields.One2many('helpdesk.ticket','operator_id', string="Casos")
    comment_ids = fields.One2many('helpdesk.ticket.comment','operator_id', string="Comentarios")
    gop_ids = fields.One2many('helpdesk.ticket.gop','operator_id', string="GOPS")
    

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    gop_ids = fields.One2many('helpdesk.ticket.gop', 'helpdesk_id', string='GOP')
    comment_ids = fields.One2many('helpdesk.ticket.comment', 'helpdesk_id', string='Comentario')
    quality_ids = fields.One2many('helpdesk.ticket.quality','helpdesk_id', string='Calidad')
    quiz_ids = fields.One2many('helpdesk.ticket.quiz','helpdesk_id', string='Encuesta')
    ticket_type = fields.Char(related="ticket_type_id.name")
    crm_lead_id = fields.Many2one('crm.lead', string="Oportunidad")
    operator_id = fields.Many2one('helpdesk.ticket.operator', string="Operador", domain="[('is_active','=','true')]")
    
    #campos relacionados enlazados
    assist_type = fields.Selection(ASSIT_TYPE_SELECTION, string='Tipo de Asistencia')
    #sub_assist_type = fields.Selection(SUB_ASSIT_TYPE_SELECTION, string='Sub Tipo Asistencia')
    sub_assist_type = fields.Many2one('helpdesk.ticket.subtype', string="Sub Tipo")

    #Información del Caso
    urgency_level = fields.Selection(URGENCY_LEVEL_SELECTION, string='Nivel de Urgencia')
    consultation_reason = fields.Text(string='Motivo de Consulta')
    observations = fields.Text(string='Observaciones')
    case_close_motive = fields.Selection(CASE_CLOSE_MOTIVE_SELECTION, string='Motivo Cierre Caso')
    tracking_type = fields.Selection(TRACKING_TYPE_SELECTION, string='Origen de Asistencia')
    is_disputed = fields.Boolean('Disputa?', default=True)
    case_state = fields.Selection(CASE_STATE_SELECTION, string='Estado de Caso')
    turn = fields.Selection([('A', 'A'),('B', 'B'), ('C', 'C')], string='Turno')
    copay = fields.Selection([('si', 'SI'), ('no', 'NO')], string='Copago')
    lack = fields.Selection([('si', 'SI'), ('no', 'NO')], string='Carencia')
    service_level = fields.Selection(SERVICE_LEVEL_SELECTION, string='Nivel de Servicio', tracking=True)
    pending_document_id = fields.Many2one('res.users', string="Documento pendiente por")
    #información del cliente
    ubication = fields.Html(string="Vinculos Personalizados")
    client_direction = fields.Text(string="Direccion del Cliente")
    partner_age = fields.Integer(related="partner_id.age", string="Edad")
    partner_phone = fields.Char(related="partner_id.phone", string="Telefono")
    partner_phone_extra = fields.Char(related="partner_id.phone", string="Telefono 2")
    wsp_skype = fields.Char( string="Whatsapp/Skype")
    partner_phone_extra = fields.Char(related="partner_id.phone", string="Telefono 2")
    crm_lead_destination = fields.Char(related="crm_lead_id.destination_country", string="Pais Destino")
    partner_destination_city = fields.Char( string="Ciudad Destino")

    currency_id = fields.Many2one('res.currency', string="Moneda")
    amount = fields.Float(string='Monto', digits=(16,2))
    amount_local = fields.Float(string='Monto TRM',compute='cambio_trm')

    @api.depends('amount','currency_id')
    def cambio_trm(self):
        for s in self:
            if s.currency_id.name == 'USD':
                s.amount_local = s.amount * 0.00028
            elif s.currency_id.name == 'ARS':
                s.amount_local = s.amount * 0.00023
            else: 
                s.amount_local = 0
    
    #información de Reembolso
    is_approved = fields.Boolean('Aprobado?')
    amount_requested = fields.Float(string='Monto Solicitado', digits=(16,2), tracking=True)
    currency_id_amount_requested = fields.Many2one('res.currency', string="Moneda Monto Solicitado", tracking=True)
    amount_requested_usd = fields.Float(string='Monto Solicitado USD', digits=(16,2), tracking=True)
    answer_date = fields.Date(string='Fecha de Respuesta')
    disputed_case = fields.Selection(DISPUTED_CASE_SELECTION, string='Caso en Disputa')
    payment_date = fields.Date(string='Fecha de Pago')
    refund = fields.Selection([('si', 'SI'), ('no', 'NO')], string='Reembolso')
    amount_approved = fields.Float(string='Monto Aprobado', digits=(16,2))
    currency_amount_refunded = fields.Many2one('res.currency', string="Moneda Monto Reembolsado")
    refund_type = fields.Selection(REFUND_TYPE_SELECTION, string='Tipo de Reembolso')
    #, default= date.today()
    documents_reception_date = fields.Date(string='Fecha Recepción de documentos')
    located = fields.Char(string='Radicado')
    #, default= datetime.now()
    payday_limit_datetime = fields.Datetime(string='Fecha Límite de Pago')
    #Others
    case_days = fields.Integer(string="Edad del caso en días", compute="calcule_days")
    @api.depends('close_date','create_date','case_state')
    def calcule_days(self):
        for s in self:
            if s.case_state == 'Cerrado':
                if s.close_date:
                    s.case_days = abs(s.close_date - s.create_date).days
                else:
                    s.close_date = datetime.now()
                    s.case_days = abs(s.close_date - s.create_date).days
            else:
                s.case_days = 0

    case_priority = fields.Selection(CASE_PRIORITY_SELECTION, string='Prioridad')
    other_description = fields.Text(string='Descripciones')
    subject = fields.Char(string='Asunto')
    is_email_survey = fields.Boolean('Encuesta por email?')
    is_wsp_survey = fields.Boolean('Encuesta por WSP?')
    #coordenadas de reembolso
    authorized_usd_value = fields.Float(string='Valor Autorizado en USD', digits=(16,2))
    authorized_currency = fields.Many2one('res.currency', string="Moneda Autorizada")
    coord_description = fields.Char(string='Descripcion')
    bank_id = fields.Many2one('res.partner.bank', string="Nombre del Banco")
    account_number = fields.Char(string='Numero de Cuenta')
    account_type = fields.Selection(ACCOUNT_TYPE_SELECTION, string='Tipo de Cuenta')
    coor_address = fields.Text(string='Dirección')
    country_send = fields.Char(string='Pais de Envio')
    city_send = fields.Char(string='Ciudad de Envio')
    state_send = fields.Char(string='Estado de Envio')
    interbank_code = fields.Char(string='Codigo Iterbancario')
    identity_number = fields.Char(string='Numero Identificacion')
    beneficiary = fields.Char(string='Beneficiario')
    contact_client_phone = fields.Char(string='Telefono de Contacto Cliente')
    contact_client_email = fields.Char(string='e-mail contacto cliente')
    coor_swift_code = fields.Char(string='Codigo Swift')
    coor_ab_code = fields.Char(string='Codigo AB')
    comission_value = fields.Char(string='Valor Comision')
    loot = fields.Char(string='lote')

    #google maps
    def open_map(self):
        url = "http://maps.google.com/maps?oi=map&q="
        if self.client_direction:
            url += self.client_direction.replace(' ','+')

        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new'
        }
    #validacion de fechas Helpdesk Informacion de Reembolso
    @api.depends('answer_date')
    @api.onchange('payday_limit_datetime')
    def validation_date_limit(self):
        if self.payday_limit_datetime:
            aux_limit_date = datetime.strptime(str(self.payday_limit_datetime),'%Y-%m-%d %H:%M:%S').date()
            if not self.answer_date or self.answer_date > aux_limit_date :
                self.payday_limit_datetime = ''
                self.env.cr.commit() 
                raise UserError('La fecha de Aprobacion debe ser menor a la fecha de limite de pago')
    
    @api.depends('partner_id')
    @api.onchange('partner_id')
    def add_lead_crm_partner(self):
        if self.partner_id:
            crm_res_obj = self.env['res.partner.child.crm.lead']
            aux_partner_ids = crm_res_obj.search([('res_partner_id','=',s.partner_id)])
            return {'domain': 'crm_lead_id': ['&',('partner_id','in', aux_partner_ids._ids),('type', '=', 'opportunity')]}
        else:
            return {'domain': 'crm_lead_id': [('type', '=', 'opportunity')]}
   
            