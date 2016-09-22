# !/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'frm.kpmg'

def f(x):
    return np.sin(x)+0.5*x

x=np.linspace(-2*np.pi,2*np.pi,50)
y=f(x)+0.25*np.random.standard_normal(len(x))

reg=np.polyfit(x,y,deg=7)
ry=np.polyval(reg,x)
plt.plot(x,y,'b^',label='f(x)')
plt.plot(x,ry,'r',label='regression')
plt.legend(loc=0)
plt.show()