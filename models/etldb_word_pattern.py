# -*- coding: utf-8 -*-
from odoo import models


class InformatioWordPattern(models.Model):
    _name = 'etldb.word_pattern'
    _inherit = 'etldb_base.model'
    _description = 'Ключевые слова'
