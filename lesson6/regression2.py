# !/usr/bin/env python
# -*- coding:utf-8 -*-
import copy
import numpy as np
import matplotlib.pyplot as plt
__author__ = 'frm.kpmg'

def  f(x):
    return np.sin(x)+0.5*x

x=np.linspace(-2*np.pi,2*np.pi,50)

matrix=np.zeros((3+1,len(x)))
matrix[3,:]=x**3
matrix[2,:]=x**2
matrix[1,:]=x**1
matrix[0,:]=1

reg=np.linalg.lstsq(matrix.T,f(x))[0] #least square
ry=np.dot(reg,matrix)
print matrix
print reg,ry
matrix1=copy.deepcopy(matrix)
matrix1[3,:]=np.sin(x)  #1,x,x^2,sin(x)

reg1=np.linalg.lstsq(matrix1.T,f(x))[0]
ry1=np.dot(reg1,matrix1)
print reg1
# np.allc
plt.plot(x,f(x),'b',label='f(x)')
plt.plot(x,ry,'r.',label='regression')
plt.plot(x,ry1,'ro',label='regression1')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()