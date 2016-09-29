# !/usr/bin/env python
# -*- coding:utf-8 -*-


__author__ = 'afli'

import csv
import scipy.optimize as opt
from scipy.interpolate import griddata
from scipy.stats import norm
from math import *


def bsm(sigma,s,k,r,t,pv):
    '''
    Black-Scholes-Merton option pricing model for European call option.
    :param sigma:
    :param s:
    :param k:
    :param r:
    :param t:
    :param pv:
    :return:difference between calculated value and input pv.
    '''
    d1=float(log(s/k)+(r+0.5*sigma**2)*t)/(sigma*sqrt(t))
    d2=float(d1-sigma*sqrt(t))
    eq=float(s*norm.cdf(d1)-k*exp(-r*t)*norm.cdf(d2)-pv)
    return eq


def vol(sigma0,s,k,r,t,pv):
    '''
    反解BSM模型，求得波动率sigma，并输出(k,t,sigma)组合
    :param sigma0:
    :param s:
    :param k:
    :param r:
    :param t:
    :param pv:
    :return:
    '''
    sigma=float('%0.4f'%opt.fsolve(bsm,sigma0,(s,k,r,t,pv)))
    result=list((k,t,sigma))
    return result

#example for volatility calculation
print 'calculated result:',vol(0.2,100,100,0.03,1.0,4)


#从csv文件读取波动率曲面，将strike,term与volatility分别存储于数组中
surf=csv.reader(file('surface.csv','rb'))
kt=[]
values=[]
for i in surf:
    if surf.line_num==1:
        continue
    kt.append((float(i[0]),float(i[1])))
    values.append(float(i[2]))


#对曲面进行插值
def inter(k,t):
    grid=griddata(kt,values,(k,t),method='linear')
    print "k0= %.2f,t0= %.2f,we get: %f" % (k,t,grid)

#example for interpolation
x=inter(100,0.5)