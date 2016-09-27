# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
#http://docs.pytest.org/
__author__ = 'frm.kpmg'
def func(x):
    return x+1

def test_answer():
    assert func(3)==4

def test_answer1():
    assert func(4)==4

class TestClass:
    def test_one(self):
        x='this'
        assert 'h' in x
if __name__=='__main__':
    #pytest.main()
    pytest.main('-q pytest1.py')
    # pytest.main('-q .')