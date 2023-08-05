# -*- coding:utf-8 -*-
"""
  @desc: 浏览器引擎 目前仅支持Chrome/Firefox
  @file: browser_event.py
"""
import logging as Log
from config.read_ini import Read
from src.util import browser_util

CONF = Read()

class Browser(object):

    def __init__(self, driver=None):
        self.driver = driver

    @classmethod
    def open(cls, driver_type, url=None):
        cls.driver = browser_util.open_browser(driver_type, url)
        Log.info("打开浏览器：%s" % url)
        return cls.driver

    @classmethod
    def get_driver(cls):
        return cls.driver

    @classmethod
    def quit(cls):
        # 退出浏览器
        cls.driver.quit()

    @classmethod
    def dispose(cls):
        # 关闭所有窗口并关闭session
        cls.driver.dispose()

    @classmethod
    def maximize(cls):
        # 浏览器最大化
        cls.driver.maximize_window()

    @classmethod
    def curhandle(cls):
        # 获取当前窗口句柄
        curhandle = cls.driver.current_window_handle()
        return curhandle

    @classmethod
    def handles(cls):
        #  获取当前窗口句柄集合（列表类型）
        handles = cls.driver.window_handles
        return handles

    def switctowindow(cls, hander):
        # 切换窗口
        for i in cls.handles:  # 切换窗口
            if i != cls.driver.current_window_handle and i == hander:
                cls.driver.close()  # 关闭第一个窗口
                cls.driver.switch_to.window(i)  # 切换窗口

    # @classmethod
    # def window(cls, url):
    #     path = 'window.open("%s");' % url
    #     cls.driver.execute_script(path)

    @classmethod
    def close(cls):
        cls.driver.close()
        Log.info("关闭当前窗口")

    # 浏览器前进操作
    @classmethod
    def forward(cls):
        cls.driver.forward()
        Log.info("浏览器点击页面")

    # 浏览器后退操作
    @classmethod
    def back(cls):
        cls.driver.back()
        Log.info("浏览器后退")

    @classmethod
    def get_html(cls, url):
        """获取网页文件
        :param url: {str} 网页链接
        :return:  {str} 网页文本
        """
        cls.browser.get(url)
        return cls.browser.page_source

