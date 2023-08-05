#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import unittest
from wikitrans.wiki2html  import HtmlWikiMarkup
from wikitest import populate_methods

class TestWikiMarkup (unittest.TestCase):
    pass

populate_methods(TestWikiMarkup, HtmlWikiMarkup, '.html')

if __name__ == '__main__':
    unittest.main()
