# !/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import pandas.io.data as web

__author__ = 'frm.kpmg'

source_data=pd.read_csv('./stock_px.csv',index_col=0,parse_dates=True)
# symbols=['AAPL','MSFT','YHOO','DB','GLD','BIDU','SINA','ACH']

#1
symbols=['BIDU','SINA']
data=pd.DataFrame()
for sym in symbols:
    data[sym]=source_data[sym]
print data
rets=np.log(data/data.shift(1))
n=len(data.columns)
prets=[]
pvols=[]
length=len(data)
for p in range(2500):
    weights=np.random.random(n)
    weights/=np.sum(weights)
    prets.append(np.sum(rets.mean()*weights*length))
    pvols.append(np.sqrt(np.dot(weights.T,np.dot(rets.cov()*length,weights))))
plt.scatter(pvols,prets,c='b')

#2
symbols=['BIDU','ACH']
data=pd.DataFrame()
for sym in symbols:
    data[sym]=source_data[sym]
print data
rets=np.log(data/data.shift(1))
n=len(data.columns)
prets=[]
pvols=[]
length=len(data)
for p in range(2500):
    weights=np.random.random(n)
    weights/=np.sum(weights)
    prets.append(np.sum(rets.mean()*weights*length))
    pvols.append(np.sqrt(np.dot(weights.T,np.dot(rets.cov()*length,weights))))
plt.scatter(pvols,prets,c='r')

#3
symbols=['SINA','ACH']
data=pd.DataFrame()
for sym in symbols:
    data[sym]=source_data[sym]
print data
rets=np.log(data/data.shift(1))
n=len(data.columns)
prets=[]
pvols=[]
length=len(data)
for p in range(2500):
    weights=np.random.random(n)
    weights/=np.sum(weights)
    prets.append(np.sum(rets.mean()*weights*length))
    pvols.append(np.sqrt(np.dot(weights.T,np.dot(rets.cov()*length,weights))))

plt.scatter(pvols,prets,c='g')

plt.xlabel('Vol')
plt.ylabel('Ret')
plt.grid(True)
# plt.show()
#4
symbols=['DB','GLD','BIDU','SINA','ACH']
# symbols=['BIDU','SINA','ACH']
data=pd.DataFrame()
for sym in symbols:
    data[sym]=source_data[sym]
print data
rets=np.log(data/data.shift(1))
n=len(data.columns)
prets=[]
pvols=[]
length=len(data)
for p in range(2500):
    weights=np.random.random(n)
    weights/=np.sum(weights)
    prets.append(np.sum(rets.mean()*weights*length))
    pvols.append(np.sqrt(np.dot(weights.T,np.dot(rets.cov()*length,weights))))

prets=np.array(prets)
pvols=np.array(pvols)

plt.scatter(pvols,prets,c=prets/pvols,marker='o')
plt.xlabel('Vol')
plt.ylabel('Ret')
plt.colorbar(label='Sharp Ratio')
plt.grid(True)
plt.show()