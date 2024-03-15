# -*- coding: utf-8 -*-

{
    'name': "Product Advanced Search",
    'summary': """Product Advanced Search""",
    'description': """Product Advanced Search""",
    'category': 'Sales',
    'version': "17.0.0.1",
    'post_init_hook': '_set_product_desc_name_post_init',
    'depends': [
        'sale_stock'
    ],
}
