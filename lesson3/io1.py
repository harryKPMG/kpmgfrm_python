# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'

input_file=file('file1.txt')
lines=input_file.readlines()
print lines
input_file.close()
input_file=file('file1.txt')
write_file=file('file2.txt','w')
while True:
    line=input_file.readline()
    if len(line)==0:
        break
    write_file.write('hi '+line)
    print line
input_file.close()
write_file.close()