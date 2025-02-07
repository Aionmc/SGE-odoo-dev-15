# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cine(models.Model):
    _name = 'amc_cine.cine'
    _description = 'Cine'
    
    name = fields.Char('Nombre', required=True, help='Introduzca el nombre del cine')
    valoracion = fields.Integer('Valoración', help='Introduzca la valoración del cine según sus reseñas')
    localizacion = fields.Char('Localización', help='Introduzca la dirección en la que se encuentra el cine')
 