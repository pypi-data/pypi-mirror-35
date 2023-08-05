import logging


class CustomException(Exception):
    code_001 = '001'  # 001表示网络异常
    code_002 = '002'  # 002表示非人为抛出的异常，定位为环境异常

    def __init__(self, code, msg=None):
        super().__init__(self)  # 初始化父类
        self.code = code
        self.msg = msg
        if code == self.code_001:
            self.errInfo = '网络异常'
        else:
            self.errInfo = '环境异常'

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_msg(self):
        return self.msg

    def set_msg(self, msg):
        self.msg = msg


if __name__ == '__main__':
    try:
        raise CustomException(CustomException.code_002, '查找元素')
    except CustomException as e:
        if e.code == e.code_001:
            logging.error(e.errInfo+':\n'+e.msg)
            pass  # 预留接口
        else:
            logging.error(e.errInfo + ':\n' + e.msg)
            exit()  # 异常退出

