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



class StockReturnExt(models.TransientModel):
    _inherit="stock.return.picking"


    def notify(self,rec_id="",rec_name=""): #takes in record_id and record_name
        try:
            channel_id = self.env['mail.channel'].search([('name', '=', 'Sales')])
            
            notification = ('<div class="sale.order"><a href="#" class="o_redirect" data-oe-model = "sale.order" data-oe-id="%s">#%s</a></div>') % (rec_id, rec_name,)
            channel_id.message_post(
                        body='Automated Message : Order has been returned: '+notification,
                        subtype='mail.mt_comment')
        except:
            raise UserError(_("Unable to send Notification,Please check channel Name"))
        
    def create_returns(self):
        origin = self.env['stock.picking'].search([("id","=",self.picking_id.id)],limit=1).origin
        rec = self.env['sale.order'].search([("name","=",origin)],limit=1)
        self.notify(rec_id = rec.id,rec_name=rec.name)
        res = super(StockReturnExt,self).create_returns()
        return res



class SaleOrderExt(models.Model):
    _inherit="sale.order"

    customer_debit = fields.Float(string="Customer Debit",compute="get_customer_debit_details",readonly=True)
    farthest_due_date = fields.Date(string="farthest Due",readonly=True)



    @api.onchange("partner_id")
    def get_customer_debit_details(self):
        amount=0
        dates=[]
        rec = self.env["account.move"].search([("invoice_partner_display_name","=",self.partner_id.name)])
        for item in rec:
            amount += item.amount_total_signed
            dates.append(item.invoice_date_due)
        if amount:
            self.customer_debit = amount
        else:
            self.customer_debit = 0
        if dates:
            self.farthest_due_date = dates[0]
        else:
            self.farthest_due_date=""
        

