# !/usr/bin/env python
# -*- coding:utf-8 -*-
import  doctest1
__author__ = 'frm.kpmg'
#https://my.oschina.net/lionets/blog/269174
#must start with test
def test_numbers():
    assert doctest1.func(4)==5

#nosetests nosetest.py
#python -m nose test.py
