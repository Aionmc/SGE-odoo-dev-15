# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pelicula(models.Model):
    _name = 'amc_cine.pelicula'
    _description = 'Pelicula'
    
    name = fields.Char('Nombre', required=True, help='Introduzca el nombre de la película')
    sinopsis = fields.Char('Sinopsis', help='Introduzca la sinopsis de la película')
    minutos = fields.Integer('Minutos', help='Introduzca la duración de la película en minutos')
    precio = fields.Float('Precio', required=True, help='Introzuca el precio a pagar para ver la película')
