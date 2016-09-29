# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'
"""
https://my.oschina.net/lionets/blog/268542
global doc
"""
def func(x):
    '''

    :param x:
    :return:
    function test
    >>> func(3)
    4
    '''
    return x+1

if __name__=='__main__':
    import doctest
    # doctest.testmod(verbose=True)

    # doctest.testmod(verbose=False)
    #python -m doctest doctest1.py
    #python -m doctest -v doctest1.py

    doctest.testfile('test.txt',verbose=True)
    #python -m doctest -v test.txt