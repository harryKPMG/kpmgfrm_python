# !/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import traceback
class StartDateInputError(ValueError):
    def __init__(self,info):
        ValueError.__init__(self, info)
        print  u'格式错误',info
__author__ = 'li'
def fun():
    a='2016-08-09'
    try:
        ss= datetime.datetime.strptime(a,'%Y-%m-%d')
    except ValueError as e:
        # print  traceback.format_exc()
        # print e.message
        raise  StartDateInputError('hi')
    return ss
try:
    print fun()
except StartDateInputError as e:
    print e.message