# !/usr/bin/env python
# -*- coding:utf-8 -*-
import scipy.optimize as spo
import numpy as np
__author__ = 'frm.kpmg'

output=False
def f((x,y)):
    z=np.sin(x)+0.05*x**2+0.05*y**2
    if output==True:
        print '%f %f %f '%(x,y,z)

    return z

# output=True
ret= spo.brute(f,((-10,10.1,5),(-10.,10.1,5)),finish=None)
print ret, f(ret)
# output=True
ret1= spo.brute(f,((-10,10.1,0.1),(-10.,10.1,0.1)),finish=None)
print ret1,f(ret1)

ret3=spo.fmin(f,ret1)
print ret3,f(ret3)

ret3=spo.fmin(f,ret)
print ret3,f(ret3)