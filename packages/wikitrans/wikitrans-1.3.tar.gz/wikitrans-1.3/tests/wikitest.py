#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from glob import glob
import os.path

def wiki_markup_test(classname, name_in, name_out):
    fh = open(name_out)
    buf = ''.join(fh.readlines()).strip()
    fh.close()
    hwm = classname(filename=name_in, lang="en")
    hwm.parse()

    if str(hwm).strip() == buf:
        return True

    # fail
    print("\n>>>%s<<<" % buf)
    print(">>>%s<<<" % str(hwm).strip())
    return False

def populate_methods(cls, wcls, suffix):
    def settest(self, base, wiki_name, pat_name):
        def dyntest(self):
            self.assertTrue(wiki_markup_test(wcls, wiki_name, pat_name))
        meth = 'test_' + wcls.__name__ + '_' + base
        dyntest.__name__ = meth
        setattr(cls, meth, dyntest)
    for file in glob('testdata/*.wiki'):
        if os.path.isfile(file):
            patfile = file[:len(file) - 5] + suffix
            base, ext = os.path.splitext(os.path.basename(file))
            if os.path.exists(patfile) and os.path.isfile(patfile):
                settest(cls, base, file, patfile)
