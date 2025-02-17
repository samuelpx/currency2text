#!/usr/bin/python
# -*- coding: utf8 -*-

from currency2text.ctt_objects import ctt_currency

class eur(ctt_currency):
    def _init_currency(self):
        self.language = u'es_ES'
        self.code = u'EUR'
        self.fractions = 100
        self.cur_singular = u' euro'
        self.cur_plural = u' euros'
        self.frc_singular = u' centimo'
        self.frc_plural = u' centimos'
        # grammatical genders: f - feminine, m - masculine, n -neuter
        self.cur_gram_gender = 'm'
        self.frc_gram_gender = 'm'
    
eur()
