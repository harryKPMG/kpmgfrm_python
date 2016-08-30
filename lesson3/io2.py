# !/usr/bin/env python
# -*- coding:utf-8 -*-
import csv

__author__ = 'frm.kpmg'


csv1=csv.reader(file('csv1.csv'))

csv2=csv.writer(file('csv2.csv','w'))

for i in csv1:
    print i
    csv2.writerow(i)


