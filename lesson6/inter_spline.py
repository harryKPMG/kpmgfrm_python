# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'

import scipy.interpolate as spi
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-2*np.pi,2*np.pi,25)
def f(x):
    return np.sin(x)+0.5*x

x1=np.linspace(1,3,100)

fun1=spi.splrep(x,f(x),k=1)
iy=spi.splev(x1,fun1)

fun2=spi.splrep(x,f(x),k=3)
iy2=spi.splev(x1,fun2)
print spi.splev(2.5,fun2)
fun2_=spi.interp1d(x,f(x),'cubic')
print fun2_(2.5)
plt.plot(x1, f(x1 ), 'b' , label='f(x)')
plt.plot(x1, iy, 'b.' , label='interpolation')
plt.plot(x1, iy2, 'r.' , label='interpolation')
#
# x2=np.linspace(-2*np.pi,2*np.pi,100)
# fun2=spi.splrep(x,f(x),k=3)
# iy=spi.splev(x2,fun2)
# plt.plot(x, f(x ), 'r' , label='f(x)')
# plt.plot(x2, iy, 'r.' , label='interpolation')

plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()