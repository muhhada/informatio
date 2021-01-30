# -*- coding: utf-8 -*-
##############################################################################
#
#    etldb module for odoo
#    Copyright (C) 2020 
#       Anton Goroshkin, 
#       Oksana Goroshkina, 
#       Rostislav Shaydurov
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "informatio",

    'summary': """

        Informatio

    """,

    'description': """
       Informatio 
    """,

    'author': "Oksana Goroshkina, Anton Goroshkin",
    'website': "www.ya.ru",

    'category': 'Education',
    'version': '0.1',
    'license': 'AGPL-3',

    'depends': [

    ],

    'data': [
        # 'security/main/group_security.xml',
        # 'security/main/moderator/ir.model.access.csv',
        # 'security/main/editor/ir.model.access.csv',
        # 'security/main/user/ir.model.access.csv',

        # 'menu.xml',

        # 'views/etldb_resource_stage_view.xml',

    ],
    'qweb': ['static/src/xml/*.xml']
}
