#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'alexyli1'

# 1.在第3次作业的基础上，读取新的fixedBond文件，计算现金流
# 2.将cashflow写入数据库(sqlite)

import datetime
import csv
import json
from itertools import islice
import sqlite3

conn=sqlite3.connect('cashflow.db')
c = conn.cursor()
c.execute('''CREATE TABLE CashFlow
(ID, Date date, cashFlow real)''')

class BondError(Exception):
    """ Bond Input Error"""
    def __init__(self, argument):
        Exception.__init__(self)
        print 'Line',argument,'exit error info'

csvread=csv.reader(file('fixedBond.csv','rt'))
count=0

for i in islice(csvread,1,None):
    count=count+1
    try:
        try:
            error=0
            float(i[5])
        except:
            error=1

        if error==1:
            raise BondError(count)
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
            for x in range(0,len(cash_list)):
                cash_list[x]=tuple(cash_list[x])
            print cash_list
            #将cashFlow写入数据库中
            c.executemany('INSERT INTO CashFlow VALUES (?,?,?)', cash_list)

    except IOError:
        print u'Error:文件导入失败'

    except BondError:
        continue

conn.commit()
c.close()