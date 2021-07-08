# -*- coding: utf-8 -*-
{
    'name': "Al-Shifaa",

    'summary': """Al-Shifaa Custom Changes""",

    'description': """
        A module for custom changes made for Al-Shifaa By Integrated Path. That includes changes to Sales,
        Inventory, Accounting, Contacts, Hr, and Events.""",

    'author': "INTEGRATED PATH",
    'website': "https://www.int-path.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'stock', 'sale_management', 'hr_contract', 'mai_sale_order_lot_selection', 
        'account_accountant', 'hr_expense', 'event', 'contacts', 'sales_customisations'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/recorde_rules.xml',
        'views/views.xml',
        'views/product_product_views.xml',
        'views/stock_quant_views.xml',
        'views/stock_production_lot_view.xml',
        'views/stock_picking_view.xml',
        'views/sale_order_view.xml',
        'views/account_payment_view.xml',
        'views/hr_expense_views.xml',
        'views/hr_employee_view.xml',
        'views/event_event_views.xml',
        'views/res_partner_view.xml',
        'report/sale_order_report.xml',
        'report/delievery_slip_ext.xml',
        'report/picking_operation_report.xml',
    ],
}
