# !/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import traceback

__author__ = 'frm.kpmg'
# a=1/0

try:
    a=1/0
except Exception as e:
    print 'hello'
    print traceback.format_exc()
    print e.message
    # sys.exit(-1)

print '-'*16

try:
    raise RuntimeError('run time exception')
except Exception as e:
    print e.message
    # sys.exit(-1)
finally:
    print 'finish'

print '*'*20

try:
    # a=1/1
    a=1/0
except Exception as e:
    print 'hello'
    print traceback.format_exc()
    print e.message
    print sys.exc_info()
else:
    print 'no issue'
finally:
    print 'finish!!!'