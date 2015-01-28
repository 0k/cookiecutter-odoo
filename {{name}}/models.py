# -*- coding: utf-8 -*-

import logging

from openerp.osv import orm, fields
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

##
## Models
##

# class mymodel(orm.Model):
#
#     _name = '{{name}}.mymodel'
#     _inherit = "res.company"
#
#     _columns = {
#         'res_model': fields.char('Model'),
#         'file': fields.binary(i
#             'File', help="File to check"),
#         'partner_id': fields.many2one(
#             'res.partner',
#             string="Attached Partner",
#             domain="[('type', '=', 'other')]",),
#     }
#
