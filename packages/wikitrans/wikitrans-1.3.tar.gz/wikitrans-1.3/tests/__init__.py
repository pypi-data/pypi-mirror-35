import unittest
import sys
from os.path import dirname, abspath

sys.path.insert(0,dirname(abspath(__file__)))

def wiki_test_suite():
    loader = unittest.TestLoader()
    return loader.loadTestFromModule()

