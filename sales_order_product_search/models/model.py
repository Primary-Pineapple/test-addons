# -*- coding: utf-8 -*-

from odoo import fields, models, api, tools


class ProductProduct(models.Model):
    _inherit = 'product.product'

    var_desc = fields.Char(comment='Variant description', compute='_compute_var_desc', store=True)

    @api.depends('default_code', 'name', 'product_template_attribute_value_ids')
    def _compute_var_desc(self):
        for rec in self:
            rec.var_desc = rec.display_name

    @api.model
    def _name_search(self, name, domain=None, operator='ilike', limit=None, order=None):
        domainn = [('var_desc', operator, name)]
        pproduct_ids = list(self._search(domainn, limit=limit, order=order))
        if pproduct_ids:
            return pproduct_ids
        
        res = super(ProductProduct, self)._name_search(name, domain=domain, operator=operator, limit=limit, order=order)
        return res