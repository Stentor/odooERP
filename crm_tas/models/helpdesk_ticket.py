# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime, date
#listas de seleccion fijas
CURRENCY_SELECTION = [
    ('ARS', 'ARS-Peso Argentino'), 
    ('AUD', 'AUD-Dolar Australia')
]
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
    ('Sirena', 'Sirena')
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
# MODELOS
# Create Model GOPS
class HelpdeskTicketGOP(models.Model):
    _name = 'helpdesk.ticket.gop'
    _description = "GOPS"

    name = fields.Char(string='GOPS')
    code = fields.Char(string='Codigo de GOP')
    amount = fields.Float(string='Monto', digits=(16,2))
    currency = fields.Selection(CURRENCY_SELECTION, string='Moneda GOP')
    service_type = fields.Selection(SERVICE_TYPE_SELECTION, string='Tipo de Servicio')
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
    helpdesk_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Id")

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

class HelpdeskTicketQuiz(models.Model):
    _name = 'helpdesk.ticket.quiz'
    _description = "Encuesta"
    name = fields.Char(string='Encuestas')
    q_contact_type = fields.Selection(CONTACT_TYPE_SELECTION, string='Medio de contacto')
    q_service_type = fields.Selection(Q_SERVICE_TYPE_SELECTION, string='Tipo De Servicio')
    q_classification = fields.Selection(CLASSIFICATION_SELECTION, string='Clasificacion')
    q_observation = fields.Text(string='Eliminación / Cambio de comentario')
    helpdesk_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Id")

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    gop_ids = fields.One2many('helpdesk.ticket.gop', 'helpdesk_id', string='GOP')
    quality_ids = fields.One2many('helpdesk.ticket.quality','helpdesk_id', string='Calidad')
    quiz_ids = fields.One2many('helpdesk.ticket.quiz','helpdesk_id', string='Encuesta')

    ticket_type = fields.Char(related="ticket_type_id.name")
    crm_lead_id = fields.Many2one('crm.lead', string="Oportunidad", domain="[('type','=','opportunity')]")
    #Información del Caso
    urgency_level = fields.Selection(URGENCY_LEVEL_SELECTION, string='Nivel de Urgencia')
    consultation_reason = fields.Text(string='Motivo de Consulta')
    observations = fields.Text(string='Observaciones')
    case_close_motive = fields.Selection(CASE_CLOSE_MOTIVE_SELECTION, string='Motivo Cierre Caso')
    tracking_type = fields.Selection(TRACKING_TYPE_SELECTION, string='Tipo De Seguimiento')
    is_disputed = fields.Boolean('Disputa?', default=True)
    case_state = fields.Selection(CASE_STATE_SELECTION, string='Estado de Caso')
    turn = fields.Selection([('B', 'B'), ('C', 'C')], string='Turno')
    copay = fields.Selection([('si', 'SI'), ('no', 'NO')], string='Copago')
    lack = fields.Selection([('si', 'SI'), ('no', 'NO')], string='Carencia')
    service_level = fields.Selection(SERVICE_LEVEL_SELECTION, string='Nivel de Servicio')
    pending_document_id = fields.Many2one('res.users', string="Documento pendiente por")
    ubication = fields.Html(string="Vínculos personalizados")

    #información del cliente
    currency_id = fields.Many2one('res.currency', string="Moneda")
    amount = fields.Float(string='Monto')
    amount_local = fields.Float(string='Monto TRM',compute='cambio_trm')
    #fecha = fields.Date(string='Fecha', default= date.today())
    #fechaactual = fields.Datetime(string='Fecha Actual', default= datetime.now())

    @api.depends('amount','currency_id')
    def cambio_trm(self):
        for s in self:
            if s.currency_id.name == 'USD':
                s.amount_local = s.amount * 0.00028
            elif s.currency_id.name == 'ARS':
                s.amount_local = s.amount * 0.00023
            else: 
                s.amount_local = 0