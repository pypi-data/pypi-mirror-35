# -*- coding:utf-8 -*-
import time, os

from PIL import Image
from common.action.browser_event import Browser
from src.util import global_util as GlobalVar
"""
浏览器元素操作， 页面、元素截图封装
"""
CURRENT_PATH = os.path.abspath(os.path.join("."))

def async_script(script, args):
   """
   异步执行JS代码
   :param script: 被执行的JS代码
   :param args: 
   :return: js代码中的任意参数
   """
   driver = Browser.get_driver()
   driver.execute_async_script(script, args)
  # driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", element, "border:2px solid red;")

def sync_script(emelent, js):
    """
    控制台执行js脚本 同步
    :param js: 脚本
    :return: 执行结果
    """
    result = emelent.execute_script(js)
    return result

def screen_windows():
    """
    全屏截图
    :param driver:
    :return:
    """
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    current_dict = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    if os.path.exists(os.path.join(CURRENT_PATH, 'image\\') + current_dict) == False:
        os.mkdir(os.path.join(CURRENT_PATH, 'image\\') + current_dict)
    pic_path = os.path.join(CURRENT_PATH, 'image\\' + current_dict + '\\' + current_time + '.png')
    print("屏幕截图已经保存： " + pic_path)
    driver = Browser.get_driver()
    driver.save_screenshot(pic_path)

def screen_element(element, x=0, y=0):
    """
    元素截图
    :param element:
    :param x: 偏移x
    :param y: 偏移y
    :return:
    """
    driver = Browser.get_driver()
    left = element.location['x'] + x
    top = element.location['y'] + y
    elementWidth = element.location['x'] + element.size['width']
    elementHeight = element.location['y'] + element.size['height']
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    current_dict = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    if os.path.exists(os.path.join(CURRENT_PATH, 'image\\') + current_dict) == False:
        os.mkdir(os.path.join(CURRENT_PATH, 'image\\') + current_dict)
    pic_path = os.path.join(CURRENT_PATH, 'image\\' + current_dict + '\\' + 'el' + current_time + '.png')
    driver_path = os.path.join(CURRENT_PATH, 'image\\' + current_dict + '\\' + current_time + '.png')
    driver.save_screenshot(driver_path)
    picture = Image.open(driver_path)
    picture = picture.crop((left, top, elementWidth, elementHeight))
    picture.save(pic_path)
    os.remove(driver_path)

def screen_location(longitude, latitude):
    """
    坐标截图
    :param longitude:
    :param latitude:
    :return:
    """
    pass



def highlight_element(element):
    """
    实现高亮WebElement对象
    :param element:
    :return:
    """
    driver = GlobalVar.get_value("driver")
    js = """element = arguments[0];
        original_style = element.getAttribute('style');
        element.setAttribute('style', original_style + \";border: 2px solid red;\");
        setTimeout(function(){element.setAttribute('style', original_style);}, 1000);"""
    driver.execute_script(js, element)


def set_element_style(element, style, value):
    """
    修改指定元素的某一style属性
    :param element:
    :param style:
    :param value:
    :return:
    """
    driver = GlobalVar.get_value("driver")
    driver.execute_script("arguments[0]." + style + "=arguments[1]", element, value)


def set_element_attribute(element, attribute, value):
    """
    修改指定元素的某一attribute属性
    :param element:
    :param attribute:
    :param value:
    :return:
    """
    driver = GlobalVar.get_value("driver")
    js = "element.setAttribute('" + attribute + "', " + value + ");"
    driver.execute_script(js, element)
