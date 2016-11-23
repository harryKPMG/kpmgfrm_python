# !/usr/bin/env python
# -*- coding:utf-8 -*-
import  doctest1
__author__ = 'frm.kpmg'
#https://my.oschina.net/lionets/blog/269174
#must start with test
def f(name):
    return name
def test_numbers():
    assert doctest1.func(4)==5

def test_name():
    assert f('harry')=='harry'
#nosetests nosetest.py
#python -m nose test.py
