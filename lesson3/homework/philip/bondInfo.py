# !/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import csv
import json
from random import random as rd
from itertools import islice
import sys
import traceback

__author__ = 'philip'

# 1. 读取fixedBond.csv中的债券信息. 如有异常,则显示异常
# 2. 计算每一个债券的现金流信息
# 3. 将每一个债券的现金流信息存储导cashflow.csv文件. order代表现金流顺序id,date代表现金流发生事件,cashflow是现金流的金额
# 4. 将债券的信息存储为.json格式,并再界面上显示
# 5. 交作业的时候 请在homework作业下,建立自己的文件夹,并提交文件

class bondInputError(Exception):
    def __init__(self, argument):
        Exception.__init__(self)
        self.argument = argument


class IDInputError(bondInputError):
    def __init__(self, bondID):
        Exception.__init__(self, bondID)
        self.bondID = bondID
        print 'bondID=', bondID, u'输入的ID格式错误'


class startDateInputError(bondInputError):
    def __init__(self, bondID, startDate):
        bondInputError.__init__(self, bondID)
        self.startDate = startDate
        print bondID, u'输入的开始日期', startDate, u'格式错误'


class tenorInputError(bondInputError):
    def __init__(self, bondID, tenor):
        bondInputError.__init__(self, bondID)
        self.startDate = tenor
        print bondID, u'输入的存续期', tenor, u'格式错误'


class frequencyInputError(bondInputError):
    def __init__(self, bondID, frequency):
        bondInputError.__init__(self, bondID)
        self.frequency = frequency
        print bondID, u'输入的付息频率', frequency, u'格式错误'


class rateInputError(bondInputError):
    def __init__(self, bondID, rate):
        bondInputError.__init__(self, bondID)
        self.rate = rate
        print bondID, u'输入的票面利率', rate, u'格式错误'


try:
    bondSet = csv.reader(file('fixedBond.csv', 'r+'))
except IOError:
    print u'Error:没有找到文件或读取文件失败'
else:
    print u'Success:导入数据成功'

correctBonds = []
correctBondsCashflow = []
cashflowTemp = []
cashflowTemp1 = []
bondInfo = []
bondDict = {}

for line in islice(bondSet, 1, None):

    try:
        if line[0].startswith('bond') <> True:
            raise IDInputError(line[0])

        if line[1].find('-') == -1:
            raise startDateInputError(line[0], line[1])

        if line[3] < 0:
            raise tenorInputError(line[0], line[3])

        if line[4] not in ['1', '2', '6', '12', '4']:
            raise frequencyInputError(line[0], line[4])

        if float(line[5]) > 0.5:
            raise rateInputError(line[0], line[5])

    except IDInputError:
        line[0] = 'bond' + str(int(100 * rd()))

    except startDateInputError:
        pass

    except tenorInputError:
        pass

    except frequencyInputError:
        pass

    except rateInputError:
        line[5] = float(line[5]) * 0.01

    except Exception as e:
        print traceback.format_exc()
        print e.message
        print sys.exc_info()



    else:
        correctBonds.append(line)
        bondID = line[0]
        startDate = datetime.datetime.strptime(line[1], "%Y-%m-%d")
        faceValue = float(line[2])
        tenor = int(line[3])
        frequency = int(line[4])
        coupon = float(line[5])
        bondDict = {'bondID': bondID, 'startDate': startDate.strftime("%Y-%m-%d"), 'faceValue': faceValue,
                    'tenor': tenor, 'frequency': frequency, 'coupon': coupon}
        cashflowTemp1 = []
        cashflowTemp2 = []
        for i in range(0, tenor * frequency):
            cashflowTemp = []
            tempDelta = 365 * (i + 1) / frequency
            tempDate = (startDate + datetime.timedelta(days=tempDelta)).strftime("%Y-%m-%d")
            cashflowTemp.append(bondID)
            order = i + 1
            cashflowTemp.append(order)
            cashflowTemp.append(tempDate)
            if i == int(tenor * frequency) - 1:
                cashflowTemp.append(faceValue * (1 + coupon / frequency))
            else:
                cashflowTemp.append(faceValue * (coupon / frequency))
            cashflowTemp1.append(cashflowTemp)
            del cashflowTemp[0]
            cashflowTemp2.append(cashflowTemp)

        correctBondsCashflow.append(cashflowTemp1)
        bondDict["cashflow"] = cashflowTemp2
        bondInfo.append(bondDict)
print correctBonds
print correctBondsCashflow

cashflow = csv.writer(file('cashflow.csv', 'w'))

line1 = ['BondID', 'Order', 'Date', 'cash']

cashflow.writerow(line1)

print len(correctBondsCashflow)
for i in range(0, len(correctBondsCashflow)):
    for j in correctBondsCashflow[i]:
        cashflow.writerow(j)

bondInfo = json.dumps(bondInfo, indent=4)
# abd=json.dumps(a)
print bondInfo

print json.loads(bondInfo)
