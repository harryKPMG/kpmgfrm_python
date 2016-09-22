# !/usr/bin/env python
# -*- coding:utf-8 -*-
import scipy.optimize as spo
import numpy as np
import matplotlib.pyplot as plt
__author__ = 'frm.kpmg'

output=False
def f(x):
    z=np.sin(x)+0.05*x**2
    if output==True:
        print (x,z)

    return z

# output=True
ret= spo.brute(f,((-10,10.1,5),),finish=None)
print ret, f(ret)
ret1= spo.brute(f,((-10,10.1,0.1),),finish=None)
print ret1, f(ret1)
ret2= spo.fmin(f,ret1)
print ret2, f(ret2)


output=False
x1=np.linspace(-10,10.1,500)
plt.plot(x1,f(x1),label='f(x)')
plt.plot([ret],[f(ret)],'ro',label='min1')
plt.plot([ret1],[f(ret1)],'go',label='min2')
plt.plot(ret2,f(ret1),'bo',label='min3')
plt.legend(loc=0)
plt.show()