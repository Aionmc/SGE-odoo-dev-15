# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sala(models.Model):
    _name = 'amc_cine.sala'
    _description = 'Sala'
    
    numero = fields.Integer('Número', required=True, help='Introduzca el número de la sala')
    filas = fields.Integer('Filas', required=True, help='Introduzca el número de filas que tiene la sala')
    butacas = fields.Integer('Butacas', required=True, help='Introduzca el número de butacas que tiene la sala')
    inclusividad = fields.Boolean('Inclusividad', help='Marque si esta sala tiene medidas para discapacitados')