"""
定义一个浏览器引擎类，根据browser_type的值去，控制启动不同的浏览器，这里主要是Firefox, Chrome
"""

import os, logging as Log
from selenium import webdriver
from config.read_ini import Read
from src.util import global_util as GlobalVar

CONF = Read()
CURRENT_PATH = os.path.abspath(os.path.join("."))
DRIVER_TYPE = CONF.get("driverType") # 获取驱动类型
CHROME_DRIVER = os.path.join(CURRENT_PATH, 'lib\\driver\\' + DRIVER_TYPE.chrome_version)
FIREFOX_DRIVER = os.path.join(CURRENT_PATH, DRIVER_TYPE.firefox_version)

def get_driver(browser_type):
    if browser_type == 'firefox':
        driver = webdriver.Firefox()
    elif browser_type == 'chrome':
        driver = webdriver.Chrome(CHROME_DRIVER)
    else:
        driver = 'Null_'
    GlobalVar.set_value('driver', driver)
    return driver

def open_browser(browser_type, url=None):
    """
    通过if语句，来控制初始化不同浏览器的启动，默认是启动Chrome
    :param type:
    :param url:
    :return: driver
    """
    try:
        driver = get_driver(browser_type)
        driver.get(url)
        # 对象识别超时时间
        driver.implicitly_wait(CONF.get('driverType').timeout)
        return driver
    except Exception as e:
        Log.error('传入的浏览器类型错误或URL为空,目前仅支持Chrome/Firefox: %s' % e)
        GlobalVar.get_value('driver').close()