# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime


class AccountPayment(models.Model):
    _inherit = "account.payment"

    salesman_id = fields.Many2one("res.partner", "Salesman")
    partner_category = fields.Selection(related="partner_id.category", string="Category")
    district_id = fields.Many2one(related="partner_id.district_id", string="District")
