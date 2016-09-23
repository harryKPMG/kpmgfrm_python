# !/usr/bin/env python
# -*- coding:utf-8 -*-
import unittes1t
import doctest1
__author__ = 'frm.kpmg'

class TestUM(unittes1t.TestCase):
    def setUp(self):
        pass

    def test_number_3_4(self):
        self.assertEqual(doctest1.func(3),4)

if __name__=='__main__':
    unittes1t.main()