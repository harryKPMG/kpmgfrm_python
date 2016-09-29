# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'

import numpy as np
import matplotlib.pyplot as plt
# fv
# 利率3%，每季度支付10， 存款5年，现金 1000
fv=np.fv(0.03/4,5*4,-10,-1000)
print "future value", fv
pv=np.pv(0.03/4,4*5,-10,fv)
print 'present value',pv

years=np.linspace(1,10,10)
print years
fv_vals=np.fv(0.03/4,years*4,-10,-1000)
pv_vals=np.pv(0.03/4,years*4,-10,fv_vals)
print fv_vals
# print pv_vals
# plt.plot(fv_vals,'bo')
# plt.plot(pv_vals,'ro')
# plt.show()


cashflows=np.random.randint(100,size=5)
cashflows=np.insert(cashflows,0,-100)
print 'cashflows',cashflows
print 'npv', np.npv(0.03,cashflows)
sum=0
for i in xrange(len(cashflows)):
    df=(1+0.03)**(-1*i)
    sum+=df*cashflows[i]
print sum
print 'irr',np.irr(cashflows)

#分期付款
print 'Payment',np.pmt(0.10/12,12*30,100000)
print 'Number of payments', np.nper(0.1/12,-100,9000)

#rate
print 'Interest rate', 12*np.rate(167,-100,9000,0)

