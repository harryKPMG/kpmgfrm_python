# !/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
__author__ = 'frm.kpmg'

def  f(x):
    return np.sin(x)+0.5*x

x=np.linspace(-2*np.pi,2*np.pi,50)

reg=np.polyfit(x,f(x),deg=1)
ry=np.polyval(reg,x)
print reg,ry
print np.allclose(f(x),ry)
print np.sum((f(x)-ry)**2/len(x))
print '-'*12
reg3=np.polyfit(x,f(x),deg=5)
ry3=np.polyval(reg3,x)
print reg3,ry3
print np.allclose(f(x),ry3)
print np.sum((f(x)-ry3)**2/len(x))


plt.plot(x,f(x),'b',label='f(x)')
plt.plot(x,ry,'r.',label='regression1')
plt.plot(x,ry3,'r.',label='regression3')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
