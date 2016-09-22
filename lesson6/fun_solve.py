# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'

import scipy.optimize as opt
# import  sympy as sp
def f(x):
    return x**2-1
#x^2-1=0
# result =opt.fsolve(f,[-0.5])
# print  result
# result=opt.fmin(f,[0.5])
# print result

# result =opt.fsolve(f,[0.5,-0.5,-2,4])
# print  result
#
# result =opt.fsolve(f,[0.5],full_output=True)
# print  result
#
# result =opt.fsolve(f,[0.],full_output=True)
# print  result
# #
#
# #
def f(a,x,b,c):
    return x**2+a*x+1+b+c
# lambda x,a:f(a,x)==
# def f1(x,a):
#     return f(a,x)

result =opt.fsolve(f,[-0.5],(-1,1,-1))
print  result

# def f(x):
#     return x[0]**2+x[0]*x[1]+1,x[0]**2-1
#
# result =opt.fsolve(f,[-0.5,1])
# print  result

def  f1(x):
    eq1=0.01-x[0]
    eq2=3*x[0]-x[1]
    eq3=x[2]
    return eq1,eq2,eq3
# x0-0.01=0
# 3*x0-x1=0
# x2=0
result=opt.fsolve(f1,[1,2,3])
print result

# [sin(1),sin(2),sin(3)]=sin([1,2,3])