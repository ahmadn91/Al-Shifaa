# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime


class ResPartner(models.Model):
    _inherit = "res.partner"

    CATEGORY = [('', '')]

    category = fields.Selection(CATEGORY, string="Category")
    department = fields.Char(string="Department")
    price_category = fields.Char(string="Price Category")
    client_code = fields.Integer(string="Client Code")
