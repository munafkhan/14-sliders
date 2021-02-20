# -*- coding: utf-8 -*-

from odoo.http import request
from odoo import http
from odoo.addons.website.controllers.main import Website

# class Website(Website):
#     @http.route(auth='public')
#     def index(self, **kw):
#         super(Website, self).index()
#         product_ids = http.request.env['product.template'].sudo().search([('is_published','=',True)])
#         print(">>>>>>>>>>>>product_ids",product_ids.ids[-1])
#         return http.request.render('slider.home',{
#             'product_ids_1':product_ids.ids[-1], 
#             'product_ids_2':product_ids.ids[-2], 
#             'product_ids_3':product_ids.ids[-3],
#             })