

class Table:

    def __init__(self, table_element):
        self.table = table_element

    def row_count(self):
        """
        获取表格的总行数（包括表头）
        :return:
        """
        rows = []
        rows = self.table.find_elements_by_tag_name("tr")
        return len(rows)

    def column_count(self, row):
        """
        获取表格的总列数（包括表头）
        :return:
        """
        theRow = self.table.find_elements_by_tag_name("tr")[row]
        thcols = theRow.find_elements_by_tag_name("th")
        tdcols = theRow.find_elements_by_tag_name("td")
        cols = 0
        if len(thcols) > 0:
            cols = len(thcols)
        if len(tdcols) > 0:
            cols = len(tdcols)
        return cols

    def get_cell_text(self, x, y):
        """
        获取单元格的值（包括表头）,单元格地址(x,y)，如："1.8"表示第一行第八列
        :param x:
        :param y:
        :return:
        """
        text = ''
        cell = self.get_cell_object(x, y)
        if cell is not None:
            text = cell.text
        return text

    def get_index_text(self, texts, x , y):
        """
        传入表格所有单元格的值（包括表头）的二维列表
        获取单元格的值,单元格地址(x,y)，如："1.8"表示第一行第八列
        :param texts:
        :param x:
        :param y:
        :return:
        """
        return texts[x - 1][y - 1]

    def get_cell_texts(self):
        """
        读取table全部数据一次性存在二位数组里（包括表头）
        :return:
        """
        # theRow = null
        rows = self.table.find_elements_by_tag_name("tr")
        datas = []
        for i in range(len(rows)):
            theRow = rows[i]
            thcols = theRow.find_elements_by_tag_name("th")
            tdcols = theRow.find_elements_by_tag_name("td")
            if len(thcols) > 0:
                list = []
                for j in range(len(thcols)):
                    cell = thcols[j]
                    if cell is not None:
                        list.append(cell.text)
                    else:
                        list.append('')
                datas.append(list)
            if len(tdcols) > 0:
                list = []
                for j in range(len(tdcols)):
                    cell = tdcols[j]
                    if cell is not None:
                        list.append(cell.text)
                    else:
                        list.append('')
                datas.append(list)
        return datas

    def get_cell_object(self, x, y):
        """
        获取单元格的对象（包括表头）,单元格地址(x,y)，如："1.8"表示第一行第八列
        :param x:
        :param y:
        :return:
        """
        theRow = self.table.find_elements_by_tag_name("tr")[x - 1]
        thcols = theRow.find_elements_by_tag_name("th")
        tdcols = theRow.find_elements_by_tag_name("td")
        if len(thcols) > 0:
            target = thcols[y - 1]
        if len(tdcols) > 0:
            target = tdcols[y-1]
        return target

# from config.read_ini import Read
# from common.action.browser_event import Browser
# from src.util import global_util as GlobalVar
# from selenium import webdriver
# from src.util import get_root_path
#
# CONF = Read()
# if __name__ == '__main__':
#     GlobalVar.init()  # 初始化公共变量
#     # driver = Browser.open('chrome', 'http://10.20.10.128:28080/audit-workflow/login')
#     url = get_root_path.get_root_path()+'\\lib\\driver\\chromedriver2_29.exe'
#     driver = webdriver.Chrome(url)
#     driver.get('http://10.20.10.128:28080/audit-workflow/login')
#     driver.find_element_by_id('username').send_keys('autotest0001@dafy.com')
#     driver.find_element_by_id('password').send_keys('Lg1989!st&dw.qh')
#     driver.find_element_by_id('loginSub').click()
#     a = driver.find_elements_by_class_name('default-frame')
#     for i in a:
#         if i.get_attribute('style')=='display: block;':
#             driver.switch_to.frame(i.find_element_by_tag_name("iframe"))
#             break
#     t = driver.find_element_by_class_name('table')
#     table = Table(t)
#     print(table.get_cell_texts())


