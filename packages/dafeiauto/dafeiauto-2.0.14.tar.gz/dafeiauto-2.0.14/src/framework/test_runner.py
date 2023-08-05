import unittest, os, time
from src.util import global_util as GlobalVar
from src.util.sendemail_util import Send
from lib import HTMLTestRunner
from config.read_ini import Read
from src.framework.fail_reload import Suit
from src.framework.run_case import RunUICase


test_begin_time = ''
test_end_time = ''
CONF = Read()
CURRENT_PATH = os.path.abspath(os.path.join("."))


class TestRunner(unittest.TestCase):

    global test_begin_time
    global test_end_time
    case_list = []
    case_name_list = {}

   # 加载函数
    for case_name in os.listdir(os.path.join(CURRENT_PATH, 'suite\\test\\case')):
        case_name = case_name.split('.')
        a = case_name[0]  # 选取所要执行的用例
        s = case_name[1]
        if a[0:2] != '~$' and s == 'xlsx':
            fun = "def {func}(self):  RunUICase(self.case_list[0], '测试用例')"
            exec(fun.format(func=a))
            case_name_list[a] = a

    @classmethod
    def setUpClass(cls):
        print('批量执行用例：开始')
        TestRunner.test_begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('开始时间：', TestRunner.test_begin_time)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        print()
        print('批量执行用例：结束')
        TestRunner.test_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('结束时间：' + TestRunner.test_end_time)

    def setUp(self):
        time.sleep(2)
        GlobalVar.set_value('driver', 'Null_')
        print()
        print('------------------------------------------------')

    def tearDown(self):
        del TestRunner.case_list[0]
        driver = GlobalVar.get_value("driver")
        if driver != 'Null_':
            driver.quit()

    @staticmethod
    def run_cases():
        # suite = unittest.TestSuite()
        suite = Suit()  # Suit()覆盖unittest.TestSuite()，添加加失败重跑机制
        for case_name in TestRunner.case_name_list:
            TestRunner.case_list.append(case_name + '.xlsx')
            suite.addTest(TestRunner(case_name))
        # 批量执行测试
        runner = unittest.TextTestRunner()
        report_path = os.path.join(CURRENT_PATH, 'report')
        if os.path.exists(os.path.join(report_path, 'report.html')): # report下永远只有一个测试报告
            os.remove(os.path.join(report_path, 'report.html'))
        report_title = CONF.get('project').project_name + u'测试报告'
        fb = open(os.path.join(report_path, 'report.html'), 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title=report_title, verbosity=2)
        runner.run(suite)
        fb.close()
        if Read('email').get('mail').mail_send:
            Send({
                "test_begin_time": TestRunner.test_begin_time,
                "test_end_time": TestRunner.test_end_time,
                "to_addr_in": None, # 发动邮箱 默认读取emial配置
                "filepath_in": None, # 发送附件文件夹，默认发送report
                "content": None # 内容
            })
