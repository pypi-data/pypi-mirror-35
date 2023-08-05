# -*- coding:utf-8 -*-
"""
入口文件
"""
from src.framework.run_case import RunUICase
from src.framework.test_runner import TestRunner
from src.util import global_util as GlobalVar


def run_one():
    RunUICase("逾期流程测试分层.xlsx", "测试用例")


def run_all():
    TestRunner.run_cases()


if __name__ == "__main__":
    GlobalVar.init()  # 初始化公共变量
    run_all()