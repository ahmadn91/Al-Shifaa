
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockLot(models.Model):
  _inherit="stock.production.lot"
  on_hold_qty = fields.Float(string="On Hold Quantity")
  open_qty = fields.Float(string="Available Quantity", compute='_get_open_quantity')

  @api.constrains('on_hold_qty', 'product_qty')
  def _get_open_quantity(self):
    for line in self:
      if line.product_qty < 1 and not line.on_hold_qty:
        line.open_qty = 0
      elif line.on_hold_qty > line.product_qty:
        raise UserError(_("You can not set on hold quantity more the the available one"))
      else:
        line.open_qty = line.product_qty - line.on_hold_qty