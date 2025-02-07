# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Actor(models.Model):
    _name = 'amc_cine.actor'
    _description = 'Actor'
    
    name = fields.Char('Nombre', required=True, help='Introduzca el nombre del actor')
    edad = fields.Integer('Edad', help='Introduzca la edad del actor')
    sexo = fields.Selection([
        ('0', 'Hombre'),
        ('1', 'Mujer')
    ], string='"Sexo"')
    fechaNacimiento = fields.Date('Fecha de nacimiento', help='Introduce la fecha de nacimiento del actor')
    