# -*- coding: utf-8 -*-
# from odoo import http


# class Al-shiffa(http.Controller):
#     @http.route('/al-shiffa/al-shiffa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/al-shiffa/al-shiffa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('al-shiffa.listing', {
#             'root': '/al-shiffa/al-shiffa',
#             'objects': http.request.env['al-shiffa.al-shiffa'].search([]),
#         })

#     @http.route('/al-shiffa/al-shiffa/objects/<model("al-shiffa.al-shiffa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('al-shiffa.object', {
#             'object': obj
#         })
