# -*- coding: utf-8 -*-
# @Time    : 2021/12/1
# @Author  : chenxubin
# @File    : Log.py

"""
封装log方法
"""

import logging
import os

LEVELS = {
    "debug":logging.DEBUG,
    "info":logging.INFO,
    "warning":logging.WARNING,
    "error":logging.ERROR,
    "critical":logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'

def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass

def set_handler(levels):
    if levels == 'error':
        logger.addHandler(Mylog.err_handler)
    logger.addHandler(Mylog.handler)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(Mylog.err_handler)
    logger.removeHandler(Mylog.handler)

class Mylog:

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path + '/Log/log.txt'
    err_file = path + '/Log/err.txt'
    create_file(log_file)
    create_file(err_file)
    logger.setLevel(LEVELS.get(level,logging.INFO))
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    err_handler = logging.FileHandler(err_file,encoding='utf-8')
    err_handler.setFormatter(formatter)
    handler = logging.FileHandler(log_file,encoding='utf-8')
    handler.setFormatter(formatter)


    @staticmethod
    def debug(msg):
        set_handler("debug")
        logger.debug(msg)
        remove_handler("debug")

    @staticmethod
    def info(msg):
        set_handler("info")
        logger.info(msg)
        remove_handler("info")


    @staticmethod
    def error(msg):
        set_handler("error")
        logger.error(msg)
        remove_handler("error")


    @staticmethod
    def warning(msg):
        set_handler("warning")
        logger.warning(msg)
        remove_handler("warning")

    @staticmethod
    def critical(msg):
        set_handler("critical")
        logger.critical(msg)
        remove_handler("critical")

if __name__ == "__main__":
    Mylog.error("test")




