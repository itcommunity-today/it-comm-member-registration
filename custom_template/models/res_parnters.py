# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import AccessError


class ResUsers(models.Model):
    _inherit = ['res.users']

    superintendent = fields.Many2one('super.intendent',string='អគ្គនាយកដ្ឋាន')
    position_id = fields.Many2one('position.position',string='មុខតំណែង')


class SuperIntendent(models.Model):
    _name = 'super.intendent'
    _description = 'Superintendent for User'
    name = fields.Char(string='អគ្គនាយកដ្ឋាន')


class Position(models.Model):
    _name = 'position.position'
    _description = 'Position for User'
    name = fields.Char(string='មុខតំណែង')