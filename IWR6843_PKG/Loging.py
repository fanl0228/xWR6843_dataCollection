# -*- encoding:utf-8 -*-
import logging
import sys
import time
import os
import os.path
from enum import Enum

from colorama import Fore, Style

import colorlog

'''
 %(levelno)s:         打印日志级别的数值
 %(levelname)s:    打印日志级别名称
 %(pathname)s:    打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s:      打印当前执行程序名
 %(funcName)s:    打印日志的当前函数
 %(lineno)d:         打印日志的当前行号
 %(asctime)s:      打印日志的时间
 %(thread)d:        打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d:      打印进程ID
 %(message)s:    打印日志信息
'''

log_colors_config = {
    'DEBUG': 'white',  # cyan white
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}


class Logger(object):

    def __init__(self, logger):
        '''
        指定保存日志的文件，日志级别，调用文件，将日志存入指定文件
        :param logger: 程序模块name
        '''
        self.logger = logging.getLogger(name=logger)
        self.logger.setLevel(logging.DEBUG)

        # create log file
        curTime = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        curPath = os.path.abspath(os.path.dirname(__file__))
        log_path = curPath + "/../logs/"
        log_name = log_path + logger + "_" + curTime + ".log"

        if not self.logger.handlers:
            console_handel = logging.StreamHandler(sys.stdout)
            console_handel.setLevel(logging.DEBUG)
            console_formatter = colorlog.ColoredFormatter(
                fmt='%(log_color)s[%(asctime)s.%(msecs)03d] pid: %(thread)s %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
                datefmt='%Y-%m-%d  %H:%M:%S',
                log_colors=log_colors_config)
            console_handel.setFormatter(console_formatter)
            self.logger.addHandler(console_handel)

            file_handler = logging.FileHandler(filename=log_name, mode='a', encoding='utf8')
            file_handler.setLevel(logging.DEBUG)
            file_formatter = logging.Formatter(
                fmt='[%(asctime)s.%(msecs)03d] pid: %(thread)s %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
                datefmt='%Y-%m-%d  %H:%M:%S')
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)


    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def waring(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    log = Logger("LOGTEST")
    log.debug("debug")
    log.info("info")
    log.waring("waring")
    log.error("error")
    log.critical("critical")



