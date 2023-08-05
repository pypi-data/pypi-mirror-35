# -*- coding:utf-8 -*-
"""
运行单个用例
"""
from src.framework import relation_case as RCase

class RunUICase(object):
    def __init__(self, case_name, sheet_name=None):
        RCase.run(case_name, sheet_name)
