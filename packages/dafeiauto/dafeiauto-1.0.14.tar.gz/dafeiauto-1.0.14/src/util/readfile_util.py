# -*- coding:utf-8 -*-
"""
读取文件
"""
import os
import xlrd
import yaml
# from openpyxl import load_workbook
from src.util.logger_util import Logger

CURRENT_PATH = os.path.abspath(os.path.join("."))
def change_path(path):
    if "/" in path:
        path = path.split("/")
        dict_path = ""
        for data in path:
            dict_path = dict_path + "\\" + data
        return dict_path

class ReadExcel(object):
    def __init__(self, excel_path, sheet_name="", case_name=""):
        """
        读取excel
        :param excel_path: excel文件名称
        :param sheet_name: 需要读取的改Excel的sheet名称
        :param case_name: 需要读取的用例名称  默认读取第一条+
        """
        excel_path = os.path.join(CURRENT_PATH, excel_path)
        try:
            self.data = xlrd.open_workbook(excel_path)
            # 如果传入sheetname就读取sheetname对应的excel
        except Exception as e:
            Logger.error("路径不在或者excel不正确: ", e)
        else:
            if sheet_name is not "":
                self.table = self.data.sheet_by_name(sheet_name)
            else:
                self.table = self.data.sheet_by_index(0)  # 默认读取第一个sheet
            # 获取第一行为key
            self.key = self.table.row_values(0)
            # 获取总行数
            self.rowNum = self.table.nrows # 取这个sheet页的所有行数
            # 获取总列数
            self.colNum = self.table.ncols
            self.excelPath = excel_path
            self.case = case_name
            if self.case is not "":
                self.case = self.__get_columnIndex()


    # 获取列值 键值对：[{'数据': 'Case1', '初审账号': 1111.0}]
    def get_data(self, r, rangeLen):
        s = {}
        # 开始读取对应的value值
        values = self.table.row_values(rangeLen)
        for x in range(self.colNum):
            name = values[x]
            if type(name) == "":  # 空
                name = "''"
            elif isinstance(name, str):  # 字符串
                name = name
            elif isinstance(name, int) or name % 1 == 0:  # 整数
                name = int(name)
            elif isinstance(name, float):
                name = float(name)
            elif isinstance(name, bool):  # 布尔
                name = True if name == 1 else False
            else:  # error
                name = "错误字符"
            s[self.key[x]] = name
        return s

    # 根据名称获取对应index
    def __get_columnIndex(self):
        column_index = None
        column = self.table.col_values(0)
        try:
            column_index = column.index(self.case)
            return column_index
        except ValueError as e:
            print("ValueError:", e)

    # 获取列值
    def get_value(self, r, rangeLen):
        s = {}
        # 从第二行开始读取对应的value值
        values = self.table.row_values(rangeLen)
        s[rangeLen] = values
        r.append(s)
        return r

    def get_key(self):
        """
        :return:  格式： [{'数据': 'Case1', '初审账号': 1111.0}]
        """
        if self.rowNum <= 1:
            print("文件" + self.excelPath + "： 无数据")
        else:
            r = []
            if self.case != '':
                rangeLen = self.case
                s = self.get_data(r, rangeLen)
                r.append(s)
            else:
                j = 1 # 从第二行开始读取excel
                rangeLen = self.rowNum
                for i in range(rangeLen - 1):
                    s = self.get_data(r, j)
                    r.append(s)
                    j += 1
            return r

    def set(self):
        """
        写入excel
        :return:
        """
        pass

    def get(self):
        """
        :return: [{1: ['Case1', 1111.0, 123456.0}]
        """
        if self.rowNum <= 1:
            print("文件" + self.excelPath + "： 无数据")
        else:
            r = []
            if self.case != '':
                self.get_value(r, self.case)
            else:
                j = 1
                rangeLen = self.rowNum
                for i in range(rangeLen - 1):
                    self.get_value(r, j)
                    j += 1
            return r

    def edit(self):
        pass

class ReadYaml(object):
    """
    读取yaml 放置元素
    :param yaml_path: 文件名称
    :param name: 读取的key  默认全部读取
    """
    def __init__(self, yaml_path, name=''):
        dict_path = change_path(yaml_path)
        self.path = CURRENT_PATH + dict_path + '.yaml'
        self.name = name

    def get(self):
        yaml_path = self.path
        name = self.name
        f = open(yaml_path, 'r')
        data = yaml.load(open(yaml_path, 'r', encoding='utf-8'))
        if name != '':
            result = data[name]
        else:
            result = data
        f.close()
        return result


