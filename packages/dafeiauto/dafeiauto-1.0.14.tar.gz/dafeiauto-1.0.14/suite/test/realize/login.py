from config.read_ini import Read
from src.framework.web_element import WebElement
from common.action.assert_event import Assert
from common.action.action_event import ActionEvent
import time

CONF = Read()


def init_login(data):

    WebElement.page('登录').element('账号输入框').clear()
    WebElement.page('登录').element('账号输入框').send_keys(data.get("$initusername"))
    WebElement.page('登录').element('密码输入框').clear()
    WebElement.page('登录').element('密码输入框').send_keys(data.get("$initpwd"))
    WebElement.page('登录').element('登录按钮').click()
    time.sleep(1)
    myname = WebElement.page('登录').element('我的账号名称').text
    Assert.assert_str_equal("登录用户名", myname, data.get("$initusername"))

def end_login(data):
    WebElement.switch_to_default_content()
    LoginPageObj(driver);
    ActionEvent.click(lp.myname);
    lp.exit.click()
    lvl1 = driver.find_element_by_link_text(level1)
    ActionEvent.move_to_element(lvl1)
    WebElement.page('登录').element('账号输入框').clear()
    WebElement.page('登录').element('账号输入框').send_keys(data.get("终审账号"))
    WebElement.page('登录').element('密码输入框').clear()
    WebElement.page('登录').element('密码输入框').send_keys(data.get("终审密码"))
    WebElement.page('登录').element('登录按钮').click()
    time.sleep(1)
    myname = WebElement.page('登录').element('我的账号名称').text
    Assert.assert_str_equal("登录用户名", myname, data.get("终审账号"))
