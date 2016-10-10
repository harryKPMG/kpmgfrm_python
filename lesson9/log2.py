# !/usr/bin/env python
# -*- coding:utf-8 -*-
#http://blog.csdn.net/zyz511919766/article/details/25136485
# logger, handler, filter, format
__author__ = 'frm.kpmg'
import logging
# log factoru
logger=logging.getLogger()

# logger.setLevel(logging.CRITICAL)
logger1=logging.getLogger('myLogger1')
logger1.setLevel(logging.DEBUG)

logger2=logging.getLogger('mylogger2')
logger2.setLevel(logging.INFO)

logger3=logging.getLogger('mylogger.child')
logger3.setLevel(logging.WARNING)

fh=logging.FileHandler('test.log')
ch=logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# filter=logging.Filter('mylogger.child')
# ch.addFilter(filter)
logger.addHandler(fh)
logger.addHandler(ch)
#
# logger1.addHandler(fh)
# logger1.addHandler(ch)

# logger2.addHandler(fh)
# logger2.addHandler(ch)
#
# logger3.addHandler(fh)
# logger3.addHandler(ch)


logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')

# logger3.debug('logger3 debug message')
# logger3.info('logger3 info message')
logger3.warning('logger3 warning message')
# logger3.error('logger3 error message')
# logger3.critical('logger3 critical message')
