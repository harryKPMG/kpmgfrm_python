# !/usr/bin/env python
# -*- coding:utf-8 -*-
import csv,sqlite3
import datetime,calendar

__author__ = 'afli'


class EmptyBond(Exception):
    '''
    The defined exception about empty Bond info.
    '''
    def __init__(self,num):
        Exception.__init__(self)
        self.num=num
        print 'Empty Bond exception: No.%d bond info is empty.'%num #@d or not

class WrongFormat(Exception):
    '''
    The defined exception for rates that are in wrong format.
    '''
    def __init__(self,num):
        Exception.__init__(self)
        self.rate=num
        print 'WrongFormat exception: No.%d bond has wrong coupon format.'%num

class OutofBound(Exception):
    '''
    The defined exception for rates that are out of boundary.
    '''
    def __init__(self,num,rate):
        Exception.__init__(self)
        self.num=num
        self.rate=rate
        print 'OutofBound exception: No.%d bond coupon,%f,is out of boundary.'%(num,rate)

def wrongFormat(rate):
    '''
    defined function to return 1 if format is wrong.
    '''
    try:
        float(rate)
    except ValueError:
        return 1

#读取csv数据并检测异常
count=-1
csv1=csv.reader(file('../fixedBond.csv','rb'))
ref=[]

for i in csv1:
    count+=1
    if csv1.line_num==1:
        continue
    try:
        if len(i)==0:
            raise EmptyBond(count)
        elif wrongFormat(i[5])==1:
            raise WrongFormat(count)
        elif float(i[5])<=-1.0 or float(i[5])>=1.0:
            raise OutofBound(count,float(i[5]))
    except EmptyBond as e:
        e.num=count
        print e.message
    except WrongFormat as e:
        e.num=count
        print e.message
    except OutofBound as e:
        e.num=count
        e.rate=float(i[5])
        print e.message
    else:
        ref.append(i)

print ref

def addMonths(dt,months):
    '''
    Defined function to add months to 'date' objects.
    '''
    month = dt.month-1+months
    year = dt.year+month/12
    month = month%12 +1
    day = min(dt.day,calendar.monthrange(year,month)[1])
    return dt.replace(year=year,month=month,day=day)

#计算现金流并输出至list
cf=[['order','bondID','date','cashflow']]
for j in ref:
    date=datetime.date(int(j[1][:4]),int(j[1][5:7]),int(j[1][8:10]))
    num=int(j[3])*int(j[4]) #tenor*freq 现金流次数
    for k in range(1,num+1):
        if k==num: #last cash flow = coupon + notional
            cf.append([k,j[0],str(addMonths(date,12*k/int(j[4]))),
                       round(int(j[2])+int(j[2])*float(j[5])/int(j[4]),2)])
        else: #coupons
            cf.append([k,j[0],str(addMonths(date,12*k/int(j[4]))),
                       round(int(j[2])*float(j[5])/int(j[4]),2)])
print cf

#将现金流信息写入csv
csv2=csv.writer(file('cashflow.csv','wb')) #csv writing
for x in cf:
    csv2.writerow(x)

del cf[0]
print cf

#将现金流信息写入数据库
conn=sqlite3.connect('homework4.db')
c=conn.cursor()

c.execute('''DROP TABLE CashFlow''')
c.execute('''
    CREATE TABLE CashFlow(Orders int,BondID text not null,Date date,Cashflow real)
    ''')
c.executemany('INSERT INTO CashFlow VALUES(?,?,?,?)',cf)
conn.commit()
conn.close()