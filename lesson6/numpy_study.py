# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
__author__ = 'frm.kpmg'


symbols = [ 'MSFT' ]

data = pd.DataFrame()
for sym in symbols:
    data[sym] = web.DataReader(sym, data_source='yahoo' ,
            start='1/1/2006')['Adj Close']
data = data.dropna()

print data.head()
data.plot()
plt.show()