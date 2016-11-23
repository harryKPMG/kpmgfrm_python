# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'

import scipy.optimize as opt
#
#
# def f(x):
#     return x**2-1
#
# result =opt.fsolve(f,[-0.5])
# print  result
#
#
# result =opt.fsolve(f,[0.5],full_output=True)
# print  result
#
# result =opt.fsolve(f,[0.],full_output=True)
# print  result



def f(x,a):
    y=x**2+a*x
    return y-1

result =opt.fsolve(f,[-0.5],(3))

print  result

def  f1(x,rf=0.01):
    eq1=rf-x[0]
    eq2=3*x[0]-x[1]
    eq3=x[2]
    return eq1,eq2,eq3

result=opt.fsolve(f1,[1,2,3])
print result
print f1(result)