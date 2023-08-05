from src.framework.web_element import WebElement
from common.action.assert_event import Assert
import time
from common.action.table_event import Table
from common.action.assert_event import Assert


def search_first(data):  # 第1次搜索
        print(data, "第一次搜索")
        WebElement.page('Helloworld').element('搜索输入框').clear()
        WebElement.page('Helloworld').element('搜索输入框').send_keys(data.get('$text1'))
        WebElement.page('Helloworld').element('搜索按钮').click()
        time.sleep(4)


def search_second(data):  # 第2次搜索
        print(data, "第二次搜索")
        WebElement.page('Helloworld').element('搜索输入框').clear()
        WebElement.page('Helloworld').element('搜索输入框').send_keys(data.get('$text2'))
        WebElement.page('Helloworld').element('搜索按钮').click()
        time.sleep(4)

def search(data):  # 第2次搜索
        time.sleep(2)
        page = WebElement.page('逾期流程测试控件')
        page.element('菜单逾期数据查询').click()
        page.element('菜单流失数据查询').click()
        page.element('客户姓名框').send_keys(data.get('客户姓名'))
        page.element('搜索按钮').click()
        time.sleep(2)
        cell = Table(page.element('搜索列表')).get_cell_text(2, 1)
        Assert.assert_str_equal('查询客户姓名', cell, str(data.get('客户姓名')))
        time.sleep(2)