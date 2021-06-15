# -*- coding: utf-8 -*-
from datetime import datetime
from odoo.exceptions import UserError
from odoo import models, fields, api, _


class HrExpense(models.Model):
    _inherit = "hr.expense"

    event_id = fields.Many2one("event.event", "Event")
