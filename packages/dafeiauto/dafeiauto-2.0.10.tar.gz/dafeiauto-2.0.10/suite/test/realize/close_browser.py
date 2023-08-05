# 关闭浏览器
from common.action.browser_event import Browser
from common.action import element_event as ElemtEvent
from src.framework.web_element import WebElement
from src.util.http import Webhttp
import time

def close_first(data):
    print(data, "close")
    driver = Browser.get_driver()
    cookies = driver.get_cookies()
    print(cookies)
  #  ElemtEvent.screen_windows()
    element = WebElement.page('Helloworld').element('搜索输入框')
    ElemtEvent.screen_element(element, 100, 10)
    url = "http://v.juhe.cn/laohuangli/d"
    para = {"key": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "date": "2017-3-22"}
    headers = {}
    q = Webhttp()
    c = q.get(url, para)
    print(c)
    c1 = q.post(url, para)
    print(c1)
    c2 = q.post_json(url, para)
    print(c2)
    Browser.close()

def close(data):
    print(data, 'close')

def close_chorme():
    time.sleep(2)
    Browser.close()