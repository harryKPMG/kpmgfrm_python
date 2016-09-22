# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'

import scipy.interpolate as sci
import numpy as np
# 1D
x=np.linspace(0,10,num=11,endpoint=True)
# y=x
# print x
# print y
y=np.cos(-x)
#  x=range(0,11)
# y=x
#
# print x
# print y
#
f1=sci.interp1d(x,y)
print f1(5.1)
print f1([5.1,5.8])
f2=sci.interp1d(x,y,kind='zero')
print f2([5.1,5.8])
f3=sci.interp1d(x,y,kind='nearest')
print f3([5.1,5.8])

f4=sci.interp1d(x,y,kind='cubic') #cubic spline
print f4([5.1,5.8])

fun1=sci.splrep(x,y)
print sci.splev([5.1,5.8],fun1) #evlatuion
import matplotlib.pyplot as plt
import numpy as np
xnew=np.linspace(0,10,num=100,endpoint=True)
# xnew=range(0,41)
print xnew
plt.plot(x,y,'o')
plt.plot(xnew,f1(xnew),'-')
plt.plot(xnew,f2(xnew),'--')
plt.plot(xnew,f3(xnew),'.')
plt.plot(xnew,f4(xnew),'^')
plt.show()
# 2D
# ND.
