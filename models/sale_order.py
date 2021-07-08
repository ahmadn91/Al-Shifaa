from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrderExt(models.Model):
    _inherit="sale.order"
        
    categ_id = fields.Many2one(related="order_line.product_id.categ_id")
    current_customer_debit = fields.Monetary(string="Cuurent Debit", compute="get_customer_debit_details")
    farthest_due_date = fields.Date(string="farthest Due", compute="get_customer_debit_details")
    warehouse_location_id = fields.Many2one('stock.picking', compute='calc_warehouse_location_id')
    date_order = fields.Datetime(readonly=False)

    @api.depends("partner_id")
    def calc_warehouse_location_id(self):
        for sale_order in self:
            transfers=self.env["stock.picking"].search([("origin","=",sale_order.name)],limit=1)
            sale_order.warehouse_location_id = transfers.id

    @api.onchange("partner_id")
    def get_customer_debit_details(self):
        for sale_order in self:
            # Get Current Debit
            sale_order.current_customer_debit = sale_order.partner_id.total_due + sale_order.amount_total

            # Get lastest Debit Date
            dates=[]
            move_id = self.env["account.move"].search([("invoice_partner_display_name","=",sale_order.partner_id.name)], order="invoice_date_due desc", limit=1)
            if move_id:
                sale_order.farthest_due_date = move_id.invoice_date_due
            else:
                sale_order.farthest_due_date= False

    def action_confirm(self):
        date_order = self.date_order
        res = super(SaleOrderExt, self).action_confirm()
        self.date_order = date_order
        return res

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    lot_life_date = fields.Datetime(related="lot_id.life_date")
    lot_note = fields.Html(related="lot_id.note")