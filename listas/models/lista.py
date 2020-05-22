# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class lista(models.Model):
    _name = 'lista.canal'
    name = fields.Char(string='Descripción')
    _description = "Canales"
    description = fields.Text()
    
class lista(models.Model):
    _inherit = 'crm.lead'
    lista_id = fields.Many2one('lista.canal', string='Canales')
