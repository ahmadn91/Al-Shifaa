from odoo import models, fields, api, _
from odoo.exceptions import UserError

class StockQuant(models.Model):
    _inherit = "stock.quant"

    lot_expire_date = fields.Datetime("Lot Expire Date", related="lot_id.life_date")