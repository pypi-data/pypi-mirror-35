# run 测试
# -*- coding:utf-8 -*-
import os, sys
from src.util.readfile_util import ReadExcel
from config.read_ini import Read

CONF = Read()

def run(case_name, sheet_name):
    case_path = "suite/test/case/" + case_name
    case_data = ReadExcel(case_path, sheet_name).get_key()
    if '分支' in case_data[0].keys():
        run_module(case_name, sheet_name)
    else:
        run_case(case_name, sheet_name)

def run_case(case_name, sheet_name):
    case_path = "suite/test/case/" + case_name
    suffix = os.path.splitext(case_name)
    case_data = ReadExcel(case_path, sheet_name).get_key()
    key = ['对应关键字', '模块关键词', '方法关键词', '备注', '分支', '对应逻辑文件', '方法']
    for data in case_data:
        # 读取realize文件
        path_str = f"suite.test.realize.{data['模块关键词']}"
        keydata = {}
        for i, j in data.items():
            if i not in key:
                keydata[i] = j
        excel_data = get_temp(suffix[0], keydata)
        exec("import " + path_str)
        if excel_data == {}:
            getattr(sys.modules[path_str], data['方法关键词'])()
        else:
            getattr(sys.modules[path_str], data['方法关键词'])(excel_data)

def run_module(case_name, sheet_name):
    case_path ="suite/test/case/" + case_name
    suffix = os.path.splitext(case_name)
    find_module(case_path, sheet_name, suffix)

def find_module(case_path, sheet_name, suffix):
    """
    根据case.xlsx获取module下的关键字.xlsx
    :param case_path: 用例excel路径
    :param sheet_name: 对应的用例excel的sheetname
    :param suffix name+后缀
    :return: 关键字.xlsx
    """
    suffix_name = suffix[1]
    module_data = ReadExcel(case_path, sheet_name).get_key() # 打開case.xlsx
    for data in module_data:
        module_path = "suite/test/module/" + data['对应关键字'] + suffix_name
        find_realize(module_path, data['分支'], suffix[0])

def find_realize(module_path, case_key, case_name):
    """
    获取最终执行的realize下的py文件
    :param module_path: 关键字excel路径
    :param case_key 分支
    :param case_name 用例名
    :return: 执行的py文件路径
    """
    module = ReadExcel(module_path)
    realize_data = module.get_key()  # 打開module.xlsx
    for data in realize_data:
        if case_key == data['分支']:
            realize_path = data['对应逻辑文件']
            excel_data = get_module_data(module, case_key, case_name)
            path_str = f"suite.test.realize.{realize_path}"
            exec("import " + path_str)
            if excel_data == {}:
                getattr(sys.modules[path_str], data['方法'])()
            else:
                getattr(sys.modules[path_str], data['方法'])(excel_data)  # main加载逻辑模块
            break

def get_module_data(module, case_key, case_name):
    """
    获取module层指定的需要获取的参数
    :param mnum: 获取第mnum列参数
    :param case_name 用例名
    :return: result 逻辑页面参数
    """
    mdata = {}
    key = ['对应关键字', '模块关键词', '方法关键词', '备注', '分支', '对应逻辑文件', '方法']
    for data in module.get_key():
        if case_key == data['分支']:
            for i, j in data.items():
                if i not in key:
                    mdata[i] = j
            temp = get_temp(case_name, mdata)
            return temp

def get_temp(case_name, moduleData={}):
    """
    获取data下的excel文件，文件名称从config配置获取
    :param moduleData 参数表头
    :param case_name 用例名
    :return: result 逻辑页面参数
    """
    file = Read('file')
    data_name = file.get('data')
    sheet_name = data_name.sheet_name # 获取data下的配置data文件对应的sheetname
    data_file = data_name.data_file # 获取data下的配置data文件
    data_path = "suite/data/" + data_file
    excel_data = ReadExcel(data_path, sheet_name, case_name).get_key()
    result = {}
    for data in excel_data:
        for i, j in moduleData.items():
            if j is not '': # 如果没有写定义的参数就不会赋值
                result[j] = data[i]
    return result