# -*- coding: utf-8 -*-
# from odoo import http


# class Sotask(http.Controller):
#     @http.route('/sotask/sotask', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sotask/sotask/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sotask.listing', {
#             'root': '/sotask/sotask',
#             'objects': http.request.env['sotask.sotask'].search([]),
#         })

#     @http.route('/sotask/sotask/objects/<model("sotask.sotask"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sotask.object', {
#             'object': obj
#         })
