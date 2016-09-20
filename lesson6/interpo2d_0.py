# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'

import numpy as np
import scipy.interpolate as spi

x=np.arange(-5.01,5.01,0.25)
y=np.arange(-50.1,5.01,0.25)
xx,yy=np.meshgrid(x,y)

z=np.sin(xx**2+yy**2)
print z
f=spi.interp2d(x,y,z,kind='cubic')
print f([5],[5])