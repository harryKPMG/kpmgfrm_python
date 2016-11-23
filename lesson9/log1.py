# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'
# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('args')
# logging.info('cal process,result=5')
# logging.warn('warn ,please go ')
# logging.error('error info')
# logging.critical('critical, please stop')
import logging
# http://blog.csdn.net/zyz511919766/article/details/25136485
# output:
# level:DEBUG , INFO, WARNNING,ERROR, CRITICAL;
# format:
# mode:
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING,
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