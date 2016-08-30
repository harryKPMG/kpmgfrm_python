# !/usr/bin/env python
# -*- coding:utf-8 -*-
import json

__author__ = 'frm.kpmg'

a={'a':'b','1':'2','dict':{'c':[12,23]}}
abd=json.dumps(a,indent=4)
# abd=json.dumps(a)
print abd
print type(abd)

ccc='{"a": "b", "1": "2", "dict": {"c": [12, 23]}}'
print json.loads(ccc)
# a="{'a':'b','1':'2','dict':{'c':'asdf'}}"
# print json.loads(a)
