# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'harry'

import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

fixedBond = pd.read_csv('fixedBond.csv')
cashFlow = {'Order': [], 'BondId': [], 'Date': [], 'cashFlow': []}

for i in range(len(fixedBond[fixedBond.columns[0]])):
    order = 0
    try:
        num = int(fixedBond['tenor'][i]) * int(fixedBond['Freq'][i])
        monPay = 12 / int(fixedBond['Freq'][i])
        ratePay = float(fixedBond['rate(year)'][i])
        startDate = datetime.strptime((fixedBond['start'])[i], "%Y-%m-%d")
        for t in range(num):
            order += 1
            cashFlow['Order'].append(order)
            cashFlow['BondId'].append(fixedBond['BondId'][i])
            cashFlow['Date'].append(startDate + relativedelta(months=monPay * (t + 1)))
            if t == num - 1:
                cashFlow['cashFlow'].append(
                    float(fixedBond['FaceValue'][i]) + float(fixedBond['FaceValue'][i]) * ratePay)
            else:
                cashFlow['cashFlow'].append(float(fixedBond['FaceValue'][i]) * ratePay)
    except:
        print"注意：读取第%d笔交易时出现问题！\n" % (i + 1)
        continue
cashFlows = pd.DataFrame(cashFlow, columns=['Order', 'BondId', 'Date', 'cashFlow'])
cashFlows.to_csv("cashflow.csv", index=False)
