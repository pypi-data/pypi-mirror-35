#鼠标键盘操作
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from src.util import global_util as GlobalVar


class ActionEvent:

    @staticmethod
    def drag_and_drop(source, target):
        """
        鼠标拖拽动作，将 source 元素拖放到 target 元素的位置
        :param source: 被拖动元素
        :param target: 目标元素
        :return: 
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).drag_and_drop(source, target).perform()

    @staticmethod
    def drag_and_drop_by_offset(source, x_offset, y_offset):
        """
        鼠标拖拽动作，将 source 元素拖放到 (xOffset, yOffset) 位置
        :param source: 要拖拽的元素
        :param x_offset: 为横坐标
        :param y_offset: 为纵坐标
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).drag_and_drop_by_offset(source, x_offset, y_offset).perform()

    @staticmethod
    def click_and_hold(source, x, y):
        """
        鼠标拖拽动作，将 source 元素拖放到movementsString位置
        :param source: 要拖拽的元素
        :param x: 拖拽地址，如:"1.8" 其中1为横坐标，8为纵坐标
        :param y: 
        :return: 
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).click_and_hold(source).move_by_offset(x, y).perform()

    @staticmethod
    def key_down(keycode):
        """
        按下键盘
        :param keycode: 键盘按钮code
        :return: 
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).key_down(keycode, element=None).perform()

    @staticmethod
    def key_up(keycode):
        """
        释放键盘
        :param keycode: 键盘按钮code
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).key_up(keycode, element=None).perform()

    @staticmethod
    def send_keys(keys_to_send):
        """
        发出某个键盘的按键操作
        :param keys_to_send: 按钮code
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).send_keys(keys_to_send).perform()

    @staticmethod
    def send_keys_to_element(element, keys_to_send):
        """
        针对某个元素发出某个键盘的按键操作
        :param element: 被发送的元素
        :param keys_to_send: 按钮code
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).send_keys_to_element(element, keys_to_send).perform()

    @staticmethod
    def click(element):
        """
        鼠标左键点击指定元素
        :param element:
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).click(element).perform()

    @staticmethod
    def click_at(element, x, y):
        """
        鼠标左键点击指定元素的具体coordString位置
        :param element: 指定元素
        :param x: 移动的地址，如:"1.8",1为横坐标，8为纵坐标
        :param y:
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).move_to_element_with_offset(element, x, y).click().perform()

    @staticmethod
    def context_click(element):
        """
        鼠标右键点击指定元素
        :param element:
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).context_click(element).perform()

    @staticmethod
    def context_click_at(element, x, y):
        """
        鼠标右键点击指定元素的具体coordString位置
        :param element: 指定元素
        :param x: 移动的地址，如:"1.8",1为横坐标，8为纵坐标
        :param y:
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).move_to_element_with_offset(element, x, y).context_click(element).perform()

    @staticmethod
    def double_click(element):
        """
        鼠标双击指定元素
        :param element:
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).double_click(element).perform()

    @staticmethod
    def double_click_at(element, x, y):
        """
        鼠标双击指定元素的具体coordString位置
        :param element: 指定元素
        :param x: 移动的地址，如:"1.8",1为横坐标，8为纵坐标
        :param y:
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).move_to_element_with_offset(element, x, y).double_click(element).perform()

    @staticmethod
    def click_and_hold():
        """
        鼠标悬停在当前位置，既点击并且不释放
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).click_and_hold().perform()

    @staticmethod
    def click_and_hold_on(element):
        """
        鼠标悬停在 element元素的位置
        :param element:要悬停的元素
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).click_and_hold(element).perform()

    @staticmethod
    def click_and_hold_at(element, x, y):
        """
        鼠标悬停指定元素的具体coordString位置
        :param element: 指定元素
        :param x: 移动的地址，如:"1.8",1为横坐标，8为纵坐标
        :param y:
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).move_to_element_with_offset(element, x, y).click_and_hold(element).perform()

    @staticmethod
    def release():
        """
        释放鼠标
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).release().perform()

    @staticmethod
    def release_element(element):
        """
        释放指定的元素
        :param element:
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).release(element).perform()

    @staticmethod
    def move_to_element(element):
        """
        将鼠标移到 element元素中点
        :param element: 被移动的元素
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).move_to_element(element).perform()

    @staticmethod
    def move_to_element_by_xy(element, x_offset, y_offset):
        """
        将鼠标移到元素 element的 (xOffset, yOffset)位置,这里的 (xOffset, yOffset)是以元素 element
        的左上角为 (0,0) 开始的 (x, y) 坐标轴。
        :param element: 被移动的元素
        :param x_offset:
        :param y_offset:
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).move_to_element_with_offset(element, x_offset, y_offset).perform()

    @staticmethod
    def move_to_element_xy(x_offset, y_offset):
        """
        以鼠标当前位置或者 (0,0)为中心开始移动到 (xOffset, yOffset)坐标轴
        :param x_offset:
        :param y_offset:
        :return:
        """
        driver = GlobalVar.get_value('driver')
        ActionChains(driver).move_by_offset(x_offset, y_offset).perform()
