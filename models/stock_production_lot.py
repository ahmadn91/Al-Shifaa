
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockLot(models.Model):
  _inherit="stock.production.lot"
  on_hold_qty = fields.Float(string="On Hold Quantity")
  open_qty = fields.Float(string="Available Quantity", compute='_get_open_quantity')

  @api.model
  def name_get(self):
    result = []
    for record in self:
      if self.env.user.has_group('sales_team.group_sale_salesman'):
        lot_name = f"{record.name} ({record.open_qty} Quantity)"
        result.append((record.id, lot_name))
      else:
        record_name = record.name
        result.append((record.id, record_name))
    return result

  @api.constrains('on_hold_qty', 'product_qty')
  def _get_open_quantity(self):
    for line in self:
      if line.product_qty < 1 and not line.on_hold_qty:
        line.open_qty = 0
      elif line.on_hold_qty > line.product_qty:
        raise UserError(_("You can not set on hold quantity more the the available one"))
      else:
        line.open_qty = line.product_qty - line.on_hold_qty