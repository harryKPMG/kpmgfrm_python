# !/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import doctest1
__author__ = 'frm.kpmg'
#https://my.oschina.net/lionets/blog/268704
class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_3_4(self):
        self.assertEqual(doctest1.func(3),4)

class simple_test(unittest.TestCase):
    def setUp(self):
        self.foo=list(range(10))

    def test_1st(self):
        self.assertEqual(self.foo.pop(),9)


    def test_2st(self):
        self.assertEqual(self.foo.pop(),9)
if __name__=='__main__':
    unittest.main()