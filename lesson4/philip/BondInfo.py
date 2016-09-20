#!/user/bin/python
# _*_ coding: utf-8 _*_

import datetime
import csv
from itertools import islice
import sqlite3

__author__ = 'philip'


class BondInputError(Exception):
    def __init__(self, argument):
        Exception.__init__(self)
        self.argument = argument


class IDInputError(BondInputError):
    def __init__(self, bondID):
        Exception.__init__(self, bondID)
        self.bondID = bondID
        print 'bondID=', bondID, u'输入的ID格式错误'


class StartDateInputError(BondInputError):
    def __init__(self, bondID, startDate):
        BondInputError.__init__(self, bondID)
        self.startDate = startDate
        print bondID, u'输入的开始日期', startDate, u'格式错误'


class FaceValueInputError(BondInputError):
    def __init__(self, bondID, faceValue):
        BondInputError.__init__(self, bondID)
        self.faceValue = faceValue
        print bondID, u'输入的债券面值', faceValue, u'格式错误'


class TenorInputError(BondInputError):
    def __init__(self, bondID, tenor):
        BondInputError.__init__(self, bondID)
        self.startDate = tenor
        print bondID, u'输入的存续期', tenor, u'格式错误'


class FrequencyInputError(BondInputError):
    def __init__(self, bondID, frequency):
        BondInputError.__init__(self, bondID)
        self.frequency = frequency
        print bondID, u'输入的付息频率', frequency, u'格式错误'


class RateInputError(BondInputError):
    def __init__(self, bondID, rate):
        BondInputError.__init__(self, bondID)
        self.rate = rate
        print bondID, u'输入的票面利率', rate, u'格式错误'


# 定义债券输入异常类

def checkDate(strDate):
    flag = 0
    try:
        datetime.datetime.strptime(strDate, "%Y%m%d")
    except ValueError:
        flag = flag + 1
    else:
        result = datetime.datetime.strptime(strDate, "%Y%m%d")

    try:
        datetime.datetime.strptime(strDate, "%Y-%m-%d")
    except ValueError:
        flag = flag + 1
    else:
        result = datetime.datetime.strptime(strDate, "%Y-%m-%d")

    try:
        datetime.datetime.strptime(strDate, "%y-%m-%d")
    except ValueError:
        flag = flag + 1
    else:
        result = datetime.datetime.strptime(strDate, "%y-%m-%d")

    try:
        datetime.datetime.strptime(strDate, "%y%m%d")
    except ValueError:
        flag = flag + 1
    else:
        result = datetime.datetime.strptime(strDate, "y%m%d")

    if flag == 4:
        return 1
    else:
        return result


def checkFaceValue(faceValue):
    try:
        float(faceValue)
    except ValueError:
        return 1
    else:
        return 0


def checkTenor(tenor):
    try:
        float(tenor)
    except ValueError:
        return 1
    else:
        if float(tenor) <= 0:
            return 1
        else:
            return 0


def checkFrequency(frequency):
    try:
        float(frequency)
    except ValueError:
        return 1
    else:
        if float(frequency) <= 0:
            return 1
        else:
            return 0


def checkRate(rate):
    try:
        float(rate)
    except ValueError:
        return 1
    else:
        if abs(float(rate)) > 0.5:
            return 1
        else:
            return 0


try:
    bondSet = csv.reader(file('./fixedBond.csv', 'r+'))
except IOError:
    print u'Error:没有找到文件或读取文件失败'
else:
    print u'Success:导入数据成功'
# 判断读取文件是否异常

correctBonds = []
correctBondsCashflow = []
correctBondsCashflow1 = []
cashflowTemp = []

for line in islice(bondSet, 1, None):

    if len(line) < 6:
        break

    bondID = line[0]
    startDate = line[1]
    faceValue = line[2]
    tenor = line[3]
    frequency = line[4]
    coupon = line[5]

    try:
        if bondID.startswith('bond') <> True:
            raise IDInputError(bondID)

        if checkDate(startDate) == 1:
            raise StartDateInputError(bondID, startDate)

        if checkTenor(tenor) == 1:
            raise TenorInputError(bondID, tenor)

        if checkFaceValue(faceValue) == 1:
            raise FaceValueInputError(bondID, faceValue)

        if checkFrequency(frequency) == 1:
            raise FrequencyInputError(bondID, frequency)

        if checkRate(coupon) == 1:
            raise RateInputError(bondID, coupon)

    except IDInputError as e:
        print e.message

    except StartDateInputError as e:
        print e.message

    except TenorInputError as e:
        print e.message

    except FrequencyInputError as e:
        print e.message

    except FaceValueInputError as e:
        print e.message

    except RateInputError as e:
        print e.message

    except Exception as e:
        print e.message

    else:

        correctBonds.append(line)
        startDate = checkDate(startDate)
        faceValue = float(faceValue)
        tenor = float(tenor)
        frequency = int(frequency)
        coupon = float(coupon)

        tenorDays = tenor * 365
        endDate = startDate + datetime.timedelta(days=tenorDays)
        delta = 365 / frequency

        cashflowStartDate = startDate
        cashflowEndDate = cashflowStartDate + datetime.timedelta(days=delta)

        order = 1
        cashflowTemp = []
        while cashflowEndDate < endDate:
            cashflowTemp = []
            cashflowTemp.append(bondID)
            cashflowTemp.append(order)
            cashflowTemp.append(cashflowEndDate.strftime('%Y-%m-%d'))
            yearFraction = (cashflowEndDate - cashflowStartDate).days / 365.0
            cashflowTemp.append(faceValue * (coupon * yearFraction))
            cashflowStartDate = cashflowEndDate + datetime.timedelta(days=1)
            cashflowEndDate = cashflowStartDate + datetime.timedelta(days=delta)
            order = order + 1
            correctBondsCashflow.append(cashflowTemp)
        cashflowTemp = []
        cashflowTemp.append(bondID)
        cashflowTemp.append(order)
        cashflowTemp.append(cashflowEndDate.strftime('%Y-%m-%d'))
        yearFraction = (endDate - cashflowStartDate).days / 365.0
        cashflowTemp.append(faceValue * (coupon * yearFraction) + faceValue)
        correctBondsCashflow.append(cashflowTemp)
        print cashflowTemp

print correctBondsCashflow

for line in correctBondsCashflow:
    line = tuple(line)
    correctBondsCashflow1.append(line)

print correctBondsCashflow1
# 将正确数据的现金流写入数据库
conn = sqlite3.connect('BondInfo.db')
c = conn.cursor()
c.execute('''CREATE TABLE BondCashFlow
(BondId text, Orders int, PaymentDate date, CashFlow real)''')
c.executemany('INSERT INTO BondCashFlow VALUES (?,?,?,?)', correctBondsCashflow1)
conn.commit()
