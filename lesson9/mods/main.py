# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'frm.kpmg'

import logging
import logging.config

logging.config.fileConfig('logging.conf')
root_logger=logging.getLogger('root')
root_logger.debug('test root logger ...')

logger=logging.getLogger('main')
logger.info('test main logger')
logger.info('start import module ')
import mod
logger.debug('test mod.testlogger()')
mod.testLogger()
root_logger.info('finish test ...')