# -*- coding: utf-8 -*-
from datetime import datetime
from odoo.exceptions import UserError
from odoo import models, fields, api, _


class EventEvent(models.Model):
    _inherit = "event.event"

    expense_count = fields.Integer(compute="_expense_count")
    
    def _expense_count(self):
        for record in self:
            record.expense_count = self.env['hr.expense'].search_count(
                [('event_id', '=', record.id)])

    def redirect_to_expense(self, context={}):
        form_view_id = self.env.ref("hr_expense.hr_expense_view_form").id
        tree_view_id = self.env.ref("hr_expense.view_expenses_tree").id

        context.update({"default_event_id": self.id})

        return {
            'type': 'ir.actions.act_window',
            'name': 'Expenses',
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'hr.expense',
            'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
            'domain': [('event_id', '=', self.id)],
            'target': 'current',
            'context': context,
        }
