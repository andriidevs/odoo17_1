{
    'name': 'AB Hospital',
    'summary': '',
    'author': 'AB Prod',
    'website': 'https://odoo.ab/',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.0.1.0',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'views/hr_hospital_views.xml',
        'data/diseases_data.xml',
    ],
    'demo': [
        'demo/doctor_demo.xml',         # Демо-данные
        'demo/patient_demo.xml',        # Демо-данные
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],

}