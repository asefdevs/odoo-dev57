{
    "name": "Hospital System",
    "author": "Asaf Guluzade",
    "version": "1.0",
    "license": "LGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/patient_views.xml",
        "views/appointment_views.xml",
        "views/patient_tag_views.xml",
        "views/appointment_line_views.xml",
        "views/menu.xml",
    ],
    "depends": ["mail", "product"],
    "installable": True,
    "application": True,
}