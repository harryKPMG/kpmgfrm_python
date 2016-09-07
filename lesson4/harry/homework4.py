# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'harry'

import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sqlite3
import numpy as np

# 读取债券信息
fixedBond = pd.read_csv('fixedBond.csv')
cashFlow = {'Order': [], 'BondId': [], 'Date': [], 'cashFlow': []}

# 计算现金流
for i in range(len(fixedBond[fixedBond.columns[0]])):
    order = 0
    try:
        num = int(fixedBond['tenor'][i]) * int(fixedBond['Freq'][i])
        monPay = 12 / int(fixedBond['Freq'][i])
        rateYear = float(fixedBond['rate(year)'][i])
        if np.abs(rateYear) >= 1:
            print"注意：第%d笔交易的利率有误！\n" % (i + 1)
            continue
        else:
            startDate = datetime.strptime((fixedBond['start'])[i], "%Y-%m-%d")
            for t in range(num):
                order += 1
                cashFlow['Order'].append(order)
                cashFlow['BondId'].append(fixedBond['BondId'][i])
                tempDate = datetime.strftime(startDate + relativedelta(months=monPay + t + 1), "%Y-%m-%d")
                cashFlow['Date'].append(tempDate)
                if t == num - 1:
                    cashFlow['cashFlow'].append(
                        float(fixedBond['FaceValue'][i]) + float(fixedBond['FaceValue'][i]) * (
                        rateYear / float(fixedBond['Freq'][i])))
                else:
                    cashFlow['cashFlow'].append(
                        float(fixedBond['FaceValue'][i]) * (rateYear / float(fixedBond['Freq'][i])))
    except:
        print"注意:读取第%d笔交易时出现问题！\n" % (i + 1)
        continue
cashResults = pd.DataFrame(cashFlow, columns=['Order', 'BondId', 'Date', 'cashFlow'])
#将cashFlow写入csv文件
cashResults.to_csv("cashflow.csv", index=False)

#将cashFlow写入数据库中
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE CashFlow
(Orders int, BondId text, Date date, cashFlow real)''')
zipCashFlow = zip(cashFlow['Order'], cashFlow['BondId'], cashFlow['Date'], cashFlow['cashFlow'])
c.executemany('INSERT INTO CashFlow VALUES (?,?,?,?)', zipCashFlow)
conn.commit()
