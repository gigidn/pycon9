# -*- coding: utf-8 -*-
from odoo import http

# class OdooService(http.Controller):
#     @http.route('/odoo_service/odoo_service/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_service/odoo_service/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_service.listing', {
#             'root': '/odoo_service/odoo_service',
#             'objects': http.request.env['odoo_service.odoo_service'].search([]),
#         })

#     @http.route('/odoo_service/odoo_service/objects/<model("odoo_service.odoo_service"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_service.object', {
#             'object': obj
#         })