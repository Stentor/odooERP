# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class codigo(models.Model):
    _name = 'lista.codigo'
    name = fields.Char(string='Codigo')
    _description = "Codigos"
    description = fields.Text(string='Descripción')
    
class codigo(models.Model):
    _inherit = 'crm.lead'
    lista_id = fields.Many2one('lista.codigo', string='Codigos Descuento')