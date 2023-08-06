#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import unittest
from wikitrans.wiki2texi  import TexiWikiMarkup
from wikitest import populate_methods

class TestTexiWikiMarkup (unittest.TestCase):
    pass

populate_methods(TestTexiWikiMarkup, TexiWikiMarkup, '.texi')

if __name__ == '__main__':
    unittest.main()
