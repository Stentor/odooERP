# coding: utf-8

{
    'name': "CRM TAS",
    'summary': """
        Implementación de campos relacionados con Contactos y CRM""",
    'version': '0.1',
    'depends': [
        'base',
        'crm',
        'helpdesk'
    ],
    'author': "TAS NETWORK LLC.",
    'website': "https://www.traveler-assistance.com",
    'description': """
    Implementación de campos relacionados con Contactos y CRM
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
        'views/helpdesk_ticket_view.xml',
    ],
    'images': ['static/description/icon.png'],
    # data files containing optionally loaded demonstration data
    'demo': [
         'demo/demo_data.xml',
     ],
    'installable': True,
    'application': True,
    'auto_install': False,
}