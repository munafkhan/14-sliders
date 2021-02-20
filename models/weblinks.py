# -*- coding: utf-8 -*-
# Part of Synconics. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _


class multicatgdata(models.Model):
    _inherit = 'product.template'


    @api.model
    def _get_categ_wise_pro(self):
        categ = self.env["product.public.category"].search([])
        pro_list = []
        for pro_id in categ:
            product = self.env["product.template"].search([('public_categ_ids','in',pro_id.id)])
            pro_list.append([pro_id.name, product])
        print(">>>>>>>>>>>>dict",pro_list)

        return pro_list

        
        # return lista