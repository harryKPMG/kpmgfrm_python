# !/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import pandas.io.data as web

__author__ = 'frm.kpmg'

source_data=pd.read_csv('./stock_px.csv',index_col=0,parse_dates=True)
symbols=['AAPL','MSFT','YHOO','DB','GLD','BIDU','SINA','ACH']
data=pd.DataFrame()
for sym in symbols:
    data[sym]=source_data[sym]
print data
rets=np.log(data/data.shift(1))
n=len(data.columns)
prets=[]
pvols=[]
len=len(data)
for p in range(25000):
    weights=np.random.random(n)
    weights/=np.sum(weights)
    prets.append(np.sum(rets.mean()*weights*len))
    pvols.append(np.sqrt(np.dot(weights.T,np.dot(rets.cov()*len,weights))))

prets=np.array(prets)
pvols=np.array(pvols)

plt.scatter(pvols,prets,c=prets/pvols,marker='o')
plt.xlabel('Vol')
plt.ylabel('Ret')
plt.colorbar(label='Sharp Ratio')
plt.grid(True)
plt.show()