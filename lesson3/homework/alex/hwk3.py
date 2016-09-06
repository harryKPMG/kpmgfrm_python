#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'alexyli1'

# 1. 读取fixedBond.csv中的债券信息. 如有异常,则显示异常
# 2. 计算每一个债券的现金流信息
# 3. 将每一个债券的现金流信息存储导cashflow.csv文件. order代表现金流顺序id,date代表现金流发生时间,cashflow是现金流的金额
# 4. 将债券的信息存储为.json格式,并再界面上显示
# 5. 交作业的时候 请在homework作业下,建立自己的文件夹,并提交文件

import datetime
import csv
import json
from itertools import islice


class BondError(Exception):
    """ Bond Error"""
    def __init__(self, argument):
        Exception.__init__(self)
        print 'bond:',argument,'exit error'

# filename='/Users/alexyli1/PycharmProjects/kpmgfrm_python/lesson3/homework/fixedBond.csv'
# csvr=csv.reader(file(filename,'rt'))

csvw=csv.writer(file('cashflow.csv','w'))

try:
    csvread=csv.reader(file('fixedBond.csv','rt'))
    for i in islice(csvread,1,None):
        if i[0].startswith('bond')<>True:
            raise BondError(i)
        else:
            bond_name=str(i[0])
            # BondId,start,FaceValue,tenor,Freq,rate(year)
            bond_id=str(i[0])
            start_date=datetime.datetime.strptime(i[1], "%Y-%m-%d")
            face_value=int(i[2])
            tenor=int(i[3])
            freq=int(i[4])
            rate=float(i[5])
            time_templete=start_date
            cash_list=[]
            for j in range(tenor*freq):
                cash_flow=[]
                cash_flow.append(str(bond_id)+'CashFlow'+str(j+1)+':')
                cash_flow.append((time_templete+datetime.timedelta(days=(365*j)/freq)).strftime("%Y-%m-%d"))
                if j<>tenor*freq-1:
                    cash_flow.append('%.2f' %(face_value*rate/freq))
                else:
                    cash_flow.append('%.2f' %(face_value*(1+rate)/freq))
                cash_list.append(cash_flow)
            print cash_list
            writer = csv.writer(file('cashflow.csv','ab'))
            for n in cash_list:
                writer.writerow(n)
            writer.writerow('\n')
        encodedjson=json.dumps(cash_list,indent=2)
        print encodedjson
        print '\n'

except IOError:
    print u'Error:文件导入失败'

except BondError:
    print 'Error:bond error'



# csvw.writerow(i)



