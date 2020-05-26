# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

# Create Model GOPS
class HelpdeskTicketGOP(models.Model):
    _name = 'helpdesk.ticket.gop'
    _description = "GOPS"

    name = fields.Char(string='GOPS')
    code = fields.Char(string='Codigo de GOP')
    amount = fields.Float(string='Monto', digits=(16,2))
    currency = fields.Selection([('ARS-Peso Argentino', 'ARS-Peso Argentino'), ('AUD-Dolar Australia', 'AUD-Dolar Australia')], string='Moneda GOP')
    service_type = fields.Selection([('Centro Médico', 'Centro Médico'), ('Consulta con Especialista', 'Consulta con Especialista'), ('Laboratorio clínico', 'Laboratorio clínico'),('Médico Domiciliario', 'Médico Domiciliario'),('MayoMedios diagnostico	', 'Medios diagnostico'),('Odontología', 'Odontología'),('Repatriación Funeraria', 'Repatriación Funeraria'),('Repatriación Sanitaria', 'Repatriación Sanitaria'),('Tratamiento', 'Tratamiento'),('Telemedico', 'Telemedico'),('Interrupcion de viaje', 'Interrupcion de viaje'),('Ambulancia', 'Ambulancia'),('Consulta externa', 'Consulta externa'),('Videoconferencia', 'Videoconferencia')], string='Tipo de Servicio')
    reference = fields.Text(string="Referencia GOP")
    medical_center_name = fields.Text(string="Nombre de Centro Médico")
    observation = fields.Text(string="Observaciones")
    asisst = fields.Selection([('si', 'SI'), ('no', 'NO'), ('autoasistencia', 'Autoasistencia')], string='Asistió')
    is_reviewed = fields.Boolean('Revisado?')
    is_paid = fields.Boolean('Pagado?')
    invoice_number = fields.Text(string="Número de Facturas")
    is_disputed = fields.Boolean('Disputa?')
    invoice_month = fields.Selection([('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'),('Abril', 'Abril'),('Mayo', 'Mayo'),('Junio', 'Junio'),('Julio', 'Julio'),('Agosto', 'Agosto'),('Septiembre', 'Septiembre'),('Octubre', 'Octubre'),('Noviembre', 'Noviembre'),('Diciembre', 'Diciembre')], string='Mes de Facturación')
    payment_month = fields.Selection([('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'),('Abril', 'Abril'),('Mayo', 'Mayo'),('Junio', 'Junio'),('Julio', 'Julio'),('Agosto', 'Agosto'),('Septiembre', 'Septiembre'),('Octubre', 'Octubre'),('Noviembre', 'Noviembre'),('Diciembre', 'Diciembre')], string='Mes de Pago')
    helpdesk_id = fields.Many2one('helpdesk.ticket')

class HelpdeskTicketQuality(models.Model):
    _name = 'helpdesk.ticket.quality'
    _description = "Calidad"

    claim_type = fields.Selection([('Sugerencia', 'Sugerencia'), ('Petición', 'Petición'), ('Queja', 'Queja'), ('Reclamo', 'Reclamo'), ('Felicitación', 'Felicitación')], string='Tipo De Reclamación')
    comments_date = fields.Date(string="Fecha de Recepción de comentario")
    reception_type = fields.Selection([('Correo electrónico	', 'Correo electrónico'), ('llamada telefónica', 'llamada telefónica'), ('WhatsApp', 'WhatsApp'), ('Trustpilot', 'Trustpilot'), ('Facebook', 'Facebook'), ('TripAdvisor', 'TripAdvisor'), ('Instagram', 'Instagram'), ('Otro', 'Otro')], string='Tipo De Reclamación')
    claim_motive = fields.Text(string="Motivo de Reclamación")
    expend = fields.Float(string='Gasto Incurrido', digits=(16,2))
    cmments_delete = fields.Selection([('si', 'SI'), ('no', 'NO')], string='Eliminación / Cambio de comentario')
    helpdesk_id = fields.Many2one('helpdesk.ticket')

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    gop_ids = fields.One2many('helpdesk.ticket.gop', 'helpdesk_id', string='GOP')
    quality_ids = fields.One2many('helpdesk.ticket.quality','helpdesk_id', string='Calidad')