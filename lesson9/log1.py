# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'

import logging
#http://blog.csdn.net/zyz511919766/article/details/25136485

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./test.log',
                    filemode='w')
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')