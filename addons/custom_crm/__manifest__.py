{
    'name': 'crm_custom_fields',
    'version': '1.0',
    'summary': 'Add custom fields to CRM leads',
    'category': 'Sales',
    'author': 'Your Name',
    'depends': ['crm', 'base'],   # CRM modülüne bağımlılık
    'data': [
    'views/crm.xml',
    ],
    'installable': True,
    'application': False,
}
