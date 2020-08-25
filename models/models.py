# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Shifaa(models.Model):
    _inherit = "res.partner"
    
    CATEGORIES=[("bureau","Bureau"),("company","Company"),("drugstore","Drugstore"),("pharmacy","Pharmacy"),("medical supplies","Medical Supplies"),("hospital","Hospital"),("private","Private")]
    category = fields.Selection(CATEGORIES,string="Category")
    department = fields.Char(string="Department")
    price_category = fields.Char(string="Price Category")
    client_code = fields.Integer(string="Client Code")