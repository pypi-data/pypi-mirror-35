from src.util.http import Webhttp


def boss_data_apply(userid, data_type):
    dict = {"短信": "sms", "通讯录": "address", "通话记录": "record_search", "通话统计": "recordsum_search"}
    type = dict[data_type]
    url = "https://data.boss.dafy.com/%s_search.svl"%(type)
    para = {"userId": userid}
    data_return = Webhttp().get(url, para)
    print(data_return)
    #调用示例：data_boss_apply("2289318","短信")


def es_data_apply(userid, data_type):
    dict = {"短信": "message", "通讯录":"address", "通话记录": "record", "安装的app": "app", "gps": "gps", "登录信息": "login", "行为数据": "behavior"}
    type = dict[data_type]
    url = "http://10.20.10.182/customer/%s/_search" % type
    q = "custId:%s" % userid
    para = {"q": q, "from": 0, "size": 50000}
    print(url, para)
    data_return = Webhttp().get_need_pwd(url, para, username='yeliting', password='ylt@ADMIN$2017')
    print(data_return)
    #调用示例：es_data_apply("2289318","安装的app")