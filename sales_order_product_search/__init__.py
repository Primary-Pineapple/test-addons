# -*- coding: utf-8 -*-

def _set_product_desc_name_post_init(env):
    env['product.product'].search([])._compute_var_desc()

from . import models