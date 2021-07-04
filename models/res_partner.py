# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime


class ResPartner(models.Model):
    _inherit = "res.partner"

    department = fields.Char(string="Department")
    price_category = fields.Char(string="Price Category")
    client_code = fields.Integer(string="Client Code")
    client_category_id = fields.Many2one('res.category', string='Category')


class ResPartnerClientCategory(models.Model):
    _name = "res.category"

    name = fields.Char(string="Category Name")
