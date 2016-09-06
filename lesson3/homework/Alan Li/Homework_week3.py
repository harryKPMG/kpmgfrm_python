# !/usr/bin/env python
# -*- coding:utf-8 -*-
import csv,json
import datetime,calendar

__author__ = 'afli'

class ErrorBond(Exception):
    '''
    The defined exception about wrong Bond info.
    '''
    def __init__(self,type):
        Exception.__init__(self)
        self.type=type

count=-1
csv1=csv.reader(file('fixedBond.csv','rb'))
ref=[]

for i in csv1:
    count+=1
    try:
        if csv1.line_num==1:
            continue
        elif len(i)==0:
            raise ErrorBond(0)
        elif i[5]=='error_rate':
            raise ErrorBond(1)
        else:
            ref.append(i)
    except ErrorBond as e:
        if e.type==0:
            print '"ErrorBond" exception: Empty Data.'
        elif e.type==1:
            print '"ErrorBond" exception: NO.%d Bond rate is wrong.'%count
    # else:
    #     print 'No Exceptions.'

def addMonths(dt,months):
    '''
    Defined function to add months to 'date' objects.
    '''
    month = dt.month-1+months
    year = dt.year+month/12
    month = month%12 +1
    day = min(dt.day,calendar.monthrange(year,month)[1])
    return dt.replace(year=year,month=month,day=day)

cf=[['order','bondID','date','cashflow']]
for j in ref:
    date=datetime.date(int(j[1][:4]),int(j[1][5:7]),int(j[1][8:10]))
    num=int(j[3])*int(j[4]) #tenor*freq 现金流次数
    for k in range(1,num+1):
        if k==num: #last cash flow = coupon + notional
            # cf.append([k,j[0],str(date+k*datetime.timedelta(360//int(j[4]))),
            #            round(int(j[2])+int(j[2])*float(j[5])/int(j[4]),2)])
            cf.append([k,j[0],str(addMonths(date,12*k/int(j[4]))),
                       round(int(j[2])+int(j[2])*float(j[5])/int(j[4]),2)])
        else: #coupons
            # cf.append([k,j[0],str(date+k*datetime.timedelta(360//int(j[4]))),
            #            round(int(j[2])*float(j[5])/int(j[4]),2)])
            cf.append([k,j[0],str(addMonths(date,12*k/int(j[4]))),
                       round(int(j[2])*float(j[5])/int(j[4]),2)])
print cf

csv2=csv.writer(file('cashflow.csv','wb')) #csv writing
for x in cf:
    csv2.writerow(x)

encodedjson=json.dumps(cf,indent=2)
print encodedjson