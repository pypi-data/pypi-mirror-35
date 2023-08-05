import hashlib
from src.util.jar_util import Jar


class HBase:

    @staticmethod
    def select(conn, zk, tablename, query, filterstr, behaviorType):
        """
        链接查询Hbase数据库，返回一个列表存储的字典
        :param conn: 链接参数：hbase.zookeeper.quorum
        :param zk:zookeeper的集群：10.9.14.34:2181,10.9.14.35:2181,10.9.14.36:2181,10.9.14.37:2181,10.9.14.38:2181
        :param tablename:查询的表名
        :param query:查询条件（如查询userID：）
        :param filterstr:是否过滤（Y/N）
        :param behaviorType:查询behavior才需要的字段，不需要改字段则填写N
        :return:
        """
        arr = [{}]
        hbase_event = Jar.get({'hbase-event': 'hbase.event.RunQuery'})
        ret = str(hbase_event['hbase-event'].selectHbase(conn, zk, tablename, query, filterstr, behaviorType))
        Jar.close()
        arr = eval(ret)
        return arr


def md5_encrypt(string):
    """
    d对stringMD5加密
    :param string:
    :return:
    """
    hl = hashlib.md5()
    hl.update(string.encode(encoding='utf-8'))
    return hl.hexdigest()

if __name__ == '__main__':
    conn = "hbase.zookeeper.quorum"
    zk = "10.9.14.34:2181,10.9.14.35:2181,10.9.14.36:2181,10.9.14.37:2181,10.9.14.38:2181"

    # tablename = "customer_ns:behavior"
    # query = "11173319"
    # filterstr = "Y"
    # behaviorType = "applyCredit/borrow_04.htm"

    # tablename = "customer_ns:login"
    # query = "3035596"
    # filterstr = "N"
    # behaviorType = "N"

    tablename = "customer_ns:gps"
    query = "11190637"
    filterstr = "N"
    behaviorType = "N"
    aa = HBase.select(conn, zk, tablename, query, filterstr, behaviorType)
    print(aa)