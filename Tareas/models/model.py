
from odoo import models, fields, api

class tareas():
    _name = 'tareas.tareas'
    _description = 'tareas.tareas'

    name = fields.Char()
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('hecho', 'Hecho'),
        ('cancelada', 'Cancelada'),
    ], 'Estado', default='pendiente')

    @api.multi
    def action_realizada(self):
        self.state = 'realizada'

    @api.multi
    def action_cancelada(self):
        self.state = 'cancelada'