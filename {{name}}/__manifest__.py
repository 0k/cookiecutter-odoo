# Copyright {{license_years}} {{author}} ({{company}})
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "{{name}}",
    "version": "{{version}}",
    "author": "{{company}}",
{%- if website %}
    "website": "{{ website }}",
{%- endif %}
    "maintainer": "{{author}}",
    "license": "AGPL-3",
    "category": "{{category}}",
    "summary": "{{summary}}",
    "description": """
   :image: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3
===============
{{name}}
===============

{{summary}}

Installation
============

Use Odoo normal module installation procedure to install
``{{name}}``.

Known issues / Roadmap
======================

None yet.

{%- if issue_url %}
Bug Tracker
===========

Bugs are tracked on `our issues website <{{issue_url}}>`_. In case of
trouble, please check there if your issue has already been
reported. If you spotted it first, help us smashing it by providing a
detailed and welcomed feedback.

{%- endif %}

Credits
=======

Contributors
------------

* {{author}}

Funders
-------

The development of this module has been financially supported by:
* {{company}} ({{website}})


Maintainer
----------

This module is maintained by {{company}}.

""",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
    ],
    "qweb": [
        # "static/src/xml/*.xml",
    ],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        # "security/security.xml",
        "security/ir.model.access.csv",
        # "views/menu.xml",
        # "data/data.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}