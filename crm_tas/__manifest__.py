# coding: utf-8

{
    'name': "CRM TAs",
    'version': '0.1',
    'depends': [
        'base',
        'crm'
    ],
    'author': "TAS NETWORK LLC.",
    'category': 'Generic Modules / CRM',
    'description': """
    Modulo de Listas para Canales
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
         'demo/demo_data.xml',
     ],
    'installable': True,
    'application': True,
    'auto_install': False,
}