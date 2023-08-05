# -*- coding:utf-8 -*-
import logging
import os.path
import time
from config.read_ini import Read
from src.util import global_util as GlobalVar

CONF = Read()
CURRENT_PATH = os.path.abspath(os.path.join("."))

class Logger(object):
    def __init__(self, logger):
        """
        保存指定日志文件
        :param logger:
        """
        self.error = logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建logger
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        # 创建handle写入日志
        log_path = os.path.join(CURRENT_PATH, 'logs\\')
        # 生成日志
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建handle 输出到控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)
        # handle的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)

        # 给logger添加handle
        self.logger.addHandler(fh)
        # self.logger.addHandler(ch)

    def getlog(self):
        GlobalVar.set_value("log", self.logger)
        return self.logger

    @classmethod
    def error(cls, *str):
        print(str)

    @classmethod
    def warn(cls, *str):
        print("警告: %s" % str)

    def success(cls, *str):
        print("成功： %s" % str)