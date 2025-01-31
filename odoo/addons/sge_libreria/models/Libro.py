# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Libro(models.Model):
    _name = 'sge_libreria.libro'
    _description = 'Libro'

    name = fields.Char('Título', required=True, help='Introduzca el título del libro')
    price = fields.Float('Precio', help='Introduzca el precio del libro')
    copies = fields.Integer('Ejemplares', help='Introduzca el número de ejemplares del libro')
    date = fields.Date('Fecha de compra', help='Introduzca la fecha de compra del libro')
    segmano = fields.Boolean('Segunda mano', help='Introduzca si el libro es de segunda mano o no')
    state = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Malo')
    ], string='Estado', default='0')
    