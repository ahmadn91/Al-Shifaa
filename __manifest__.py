# -*- coding: utf-8 -*-
{
    'name': "Al-Shifaa",

    'summary': """Al-Shifaa Custom Changes""",

    'description': """
        A module for custom changes made for Al-Shifaa By Integrated Path. That includes changes to sale.order, stock.picking & hr.employee
         models and reports""",

    'author': "Integerated Path",
    'website': "https://www.int-path.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','sale_management', 'hr_contract', 'sale_order_multi_lot', 'account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/stock_production_lot_view.xml',
        'report/sale_order_report.xml',
        'report/delievery_slip_ext.xml',
        'report/picking_operation_report.xml',
    ],
}
