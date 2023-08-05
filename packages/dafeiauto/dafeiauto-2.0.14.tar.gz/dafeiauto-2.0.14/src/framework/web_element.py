import logging,os
from src.util.readfile_util import ReadYaml
from src.util import global_util as GlobalVar
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EleMethod(WebElement):
    """
    元素的操作方法，主要是方便写代码，可以直接点出方法名
    """
    def __init__(self):
        pass

    # text = ''
    # def __init__(self):
    #     pass
    #
    # def click(self): pass
    #
    # def send_keys(self, keys): pass
    #
    # def clear(self): pass
    #
    # def submit(self): pass
    #
    # def get_attribute(self, key): pass
    #
    # def get_property(self, key): pass
    #
    # def find_element_by_id(self, key): return Element(self, key)
    #
    # def find_element_by_name(self, key): return Element(self, key)
    #
    # def find_element_by_class_name(self, key): return Element(self, key)
    #
    # def find_element_by_link_text(self, key): return Element(self, key)
    #
    # def find_element_by_tag_name(self, key): return Element(self, key)
    #
    # def find_element_by_xpath(self, key): return Element(self, key)
    #
    # def find_element_by_css_selector(self, key): return Element(self, key)
    #
    # def find_element_by_partial_link_text(self, key): return Element(self, key)
    #
    # def find_elements_by_id(self, key): return Element(self, key)
    #
    # def find_elements_by_name(self, key): return Element(self, key)
    #
    # def find_elements_by_class_name(self, key): return Element(self, key)
    #
    # def find_elements_by_link_text(self, key): return Element(self, key)
    #
    # def find_elements_by_tag_name(self, key): return Element(self, key)
    #
    # def find_elements_by_xpath(self, key): return Element(self, key)
    #
    # def find_elements_by_css_selector(self, key): return Element(self, key)
    #
    # def find_elements_by_partial_link_text(self, key): return Element(self, key)


class Element(EleMethod):
    page = ''
    driver = ''
    elem = ''

    def __init__(self, page, ele=None):
        self.page = page
        self.elem = ele
        self.driver = GlobalVar.get_value("driver")

    def element(self, ele_name):
        """
        返回对应的元素
        :param ele_name:
        :return:
        """
        ele = EleMethod()  # EleMethod 只是为了可以点出元素的操作方法,定义返回的类型
        get_ele = ReadYaml("suite/test/pageobj/" + self.page, ele_name).get()  # 获取元素定义属性
        if get_ele:
            ele = self.find_ele(get_ele)
            return ele
        else:
            logging.error('('+self.page+')页面没有定义元素属性：' + ele_name)
        return ele

    def find_ele(self, get_ele):
        element = ''
        if self.elem is None:
            driver = self.driver
        else:
            driver = self.elem
        key = str(get_ele.get('key'))
        value = str(get_ele.get('value'))
        if key == 'id':
            element = driver.find_element_by_id(value)
        elif key == 'name':
            element = driver.find_element_by_name(value)
        elif key == 'class':
            element = driver.find_element_by_class_name(value)
        elif key == 'text':
            element = driver.find_element_by_link_text(value)
        elif key == 'tag':
            element = driver.find_element_by_tag_name(value)
        elif key == 'xpath':
            element = driver.find_element_by_xpath(value)
        elif key == 'css':
            element = driver.find_element_by_css_selector(value)
        elif key == 'partial':
            element = driver.find_element_by_partial_link_text(value)
        else:
            logging.error('不存在的元素查找方法：key=', key)
        return element

    def elements(self, ele_name):
        """
        返回对应的元素列表
        :param ele_name:
        :return:
        """
        ele = [EleMethod()]  # EleMethod 只是为了可以点出元素的操作方法,定义返回的类型
        get_ele = ReadYaml("suite/test/pageobj/" + self.page, ele_name).get()  # 获取元素定义属性
        if get_ele:
            ele = self.find_eles(get_ele)
            return ele
        else:
            logging.error('(' + self.page + ')页面没有定义元素属性：' + ele_name)
        return ele

    def find_eles(self, get_ele):
        elements = []
        if self.elem is None:
            driver = self.driver
        else:
            driver = self.elem
        key = str(get_ele.get('key'))
        value = str(get_ele.get('value'))
        if key == 'id':
            elements = driver.find_elements_by_id(value)
        elif key == 'name':
            elements = driver.find_elements_by_name(value)
        elif key == 'class':
            elements = driver.find_elements_by_class_name(value)
        elif key == 'text':
            elements = driver.find_elements_by_link_text(value)
        elif key == 'tag':
            elements = driver.find_elements_by_tag_name(value)
        elif key == 'xpath':
            elements = driver.find_elements_by_xpath(value)
        elif key == 'css':
            elements = driver.find_elements_by_css_selector(value)
        elif key == 'partial':
            elements = driver.find_elements_by_partial_link_text(value)
        else:
            logging.error('不存在的元素查找方法：key=' + key)
        return elements

    def wait_element_load(self, ele_name, time):
        """
        显式等待：在指定的时间time（秒）内查找元素ele_name，若成功返回True，失败返回False
        :param ele_name:
        :param time:
        :return:
        """
        get_ele = ReadYaml("suite/test/pageobj/" + self.page, ele_name).get()  # 获取元素定义属性
        if get_ele:
            key = str(get_ele.get('key'))
            value = str(get_ele.get('value'))
            locator = ''
            if key == 'id':
                locator = (By.ID, value)
            elif key == 'name':
                locator = (By.NAME, value)
            elif key == 'class':
                locator = (By.CLASS_NAME, value)
            elif key == 'text':
                locator = (By.LINK_TEXT, value)
            elif key == 'tag':
                locator = (By.TAG_NAME, value)
            elif key == 'xpath':
                locator = (By.XPATH, value)
            elif key == 'css':
                locator = (By.CSS_SELECTOR, value)
            elif key == 'partial':
                locator = (By.PARTIAL_LINK_TEXT, value)
            else:
                logging.error('不存在的元素查找方法：key=' + key)
                return False
            try:
                WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
                return True
            except Exception :
                    return False
        else:
            logging.error('(' + self.page + ')页面没有定义元素属性：' + ele_name)
        return False


class Alert:

    def __init__(self):
        """
        Alert、Confirm、promp三种弹出框的通用类
        """
        driver = GlobalVar.get_value("driver")
        self.alert = driver.switch_to_alert()

    def text(self):
        """
        获取弹出框内容
        :return:
        """
        return self.alert.text

    def send_keys(self, inputs):
        """
        往promp输入框输入文本信息，只有promp类型才有输入框
        :param inputs:
        :return:
        """
        return self.alert.send_keys(inputs)

    def accept(self):
        """
        点击弹出框里面的确定按钮
        """
        self.alert.accept()

    def dismiss(self):
        """
        点击弹出框里面的取消按钮（关闭弹出框）
        """
        self.alert.dismiss()


class WebElement:
    page_name = ''

    @staticmethod
    def page(page):
        """
        :param page:pageobj的模块名称
        :return:Element的实例名
        """
        ele = Element(page)
        WebElement.page_name = page
        return ele

    @staticmethod
    def father_element(ele, page=None):
        """
        传入一个元素（ele），把该元素转化为对应页面（page）下面的一个父级元素，如果不传page参数，
        则默认为上一次查找元素所在的page
        :param ele:元素实例
        :param page:pageobj的模块名称
        :return:Element的实例(父级元素)
        """
        if page is None:
            ele = Element(WebElement.page, ele)
        else:
            ele = Element(page, ele)
        return ele

    @staticmethod
    def switch_to_default_content():
        driver = GlobalVar.get_value("driver")
        driver.switch_to.default_content()

    @staticmethod
    def switch_to_frame(element):
        driver = GlobalVar.get_value("driver")
        driver.switch_to.frame(element)

    @staticmethod
    def switch_to_alert():
        """
        切换到弹出框（Alert、Confirm、promp）上
        :return:Alert的实例名
        """
        return Alert()
