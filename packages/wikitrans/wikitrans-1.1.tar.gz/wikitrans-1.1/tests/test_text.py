#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import unittest
from wikitrans.wiki2text  import TextWikiMarkup
from wikitest import populate_methods

class TestTextWikiMarkup (unittest.TestCase):
    pass

populate_methods(TestTextWikiMarkup, TextWikiMarkup, '.text')

if __name__ == '__main__':
    unittest.main()
