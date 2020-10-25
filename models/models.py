# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Shifaa(models.Model):
    _inherit = "res.partner"
    
    #CATEGORIES=[("bureau","Bureau"),("company","Company"),("drugstore","Drugstore"),("pharmacy","Pharmacy"),("medical supplies","Medical Supplies"),("hospital","Hospital"),("private","Private")]
    category = fields.Char(string="Category")
    department = fields.Char(string="Department")
    price_category = fields.Char(string="Price Category")
    client_code = fields.Integer(string="Client Code")



class StockPickingExt(models.Model): # By AhmedNaseem, Used to block delivery validation if Done > Demand.
    _inherit="stock.picking"

    def button_validate(self):
        products=[]
        for item in self.move_ids_without_package:
            if item.product_uom_qty < item.quantity_done:
                products.append(item.product_id.name)
        if products:
            items = str(products)
            raise UserError(_("You have processed more than what was initially planned for the products %s " % items)) 
        else:
            res = super(StockPickingExt,self).button_validate()
            return res


    