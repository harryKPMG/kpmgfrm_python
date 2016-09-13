# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'
#http://www.cnblogs.com/linyawen/archive/2012/04/25/2469538.html
class P1(object):  #(object)
   def foo(self):
       print 'p1-foo'

class P2(object): #(object)
   def foo(self):
       print 'p2-foo'
   def bar(self):
       print 'p2-bar'

class C1 (P1,P2):
   pass

class C2 (P1,P2):
   def bar(self):
       print 'C2-bar'

class D(C1,C2):
   pass

d=D()
d.foo()
d.bar()