# coding: utf-8

{
    'name': "Listas",
    'version': '1.0',
    'depends': ['base','crm'],
    'author': "TAS NETWORK LLC.",
    'category': 'Administration',
    'description': """
    Modulo de Listas para Canales
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/lista_view.xml',
    ],
    # data files containing optionally loaded demonstration data
      'demo': [
         'demo/demo_data.xml',
     ],
    #'installable': True,
    #'application': True,
    #'auto_install': False,
}