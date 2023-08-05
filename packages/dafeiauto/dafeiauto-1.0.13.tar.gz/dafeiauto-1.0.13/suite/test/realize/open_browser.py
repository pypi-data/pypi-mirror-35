from config.read_ini import Read
from common.action.browser_event import Browser
from src.framework.web_element import WebElement
import time
CONF = Read()

def open_chrome(data):
    print(data, "open")
    Browser.open('chrome', CONF.get('urlServer').url_test_login)

def open(data):
    Browser.open('chrome', 'http://10.20.10.74:28089/login')

def login(data):
    Browser.open('chrome', 'http://10.20.10.74:28089/login').maximize_window()
    page = WebElement.page('逾期流程测试控件')
    page.element('登录账号框').send_keys(data.get('$username'))
    page.element('登录密码框').send_keys(data.get('$password'))
    time.sleep(2)
    page.element('登录按钮').click()


def open_google():
    Browser.open('chrome', CONF.get('urlServer').url_audit)
