# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'
import pyopt


def f(x):
    y = [0, 0, 0, 0]
    y[0] = 4005 * (1 + x[0])
    y[1] = 164693 * (1 + x[1])
    y[2] = 10600 * (1 + x[2])
    y[3] = 300962 * (1 + x[3])
    return sum(y) * 2.11 / 100

def f1(x):
    return (f(x)*11.67/100-2500)**2
# 14186.8804
def f2(x):
    return -f(x)
cons = ({'type': 'ineq', 'fun': lambda (x): f(x)-14186.8804})
# x1 = spo.minimize(f2, [1, 1, 1, 1],method='SLSQP',
#                  bounds=((0.7,1.3),(0.7,1.3),(0.7,1.3),(0.7,1.3)),
#                  constraints=cons)