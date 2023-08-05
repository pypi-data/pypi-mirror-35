# 定义全局变量
# -*-coding: utf-8-*-
import json, logging as Log

def init():
    global global_dict
    global_dict = {}

# 增加
def set_value(keys, value=''):
    try:
        if (value!=''):
            if (isinstance(value, dict)):
                value = json.dumps(value)
            global_dict[keys] = value
        else:
            for key_, value_ in keys.items():
                global_dict[key_] = str(value_)
    except BaseException as msg:
        Log.error('添加%s失败：' % (keys, msg))
        raise msg

# 删除
def del_value(key):
        try:
            del global_dict[key]
        except KeyError:
            Log.error('key: %s不存在' % str(key))

# 获取
def get_value(*args):
    try:
        dic = global_dict
        if len(args) != 0:
            for key in args:
                if len(args) == 1:
                    dic = global_dict[key]
                else:
                    dic[key] = global_dict[key]
        return dic
    except KeyError:
        Log.error('key: %s不存在' % str(key))
        return 'Null_'
    except TypeError:
        Log.error('key: %s类型错误' % str(key))
        return 'Null_'


