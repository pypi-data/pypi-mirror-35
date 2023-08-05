# -*- coding:utf-8 -*-
import traceback, cx_Oracle, pymysql, json, logging, time
from datetime import date, datetime
from decimal import Decimal
from config.read_ini import Read
CONF = Read()


class CJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return str(obj)
        elif isinstance(obj, cx_Oracle.LOB):
            return str(obj.read())
        else:
            return json.JSONEncoder.default(self, obj)


class Oracle:
    conn = ''
    cursor = ''

    def __init__(self, db_map):
        """
        初始化类，获得Mysql的实例
        :param db_map:
        """
        # noinspection PyBroadException
        try:
            self.conn = cx_Oracle.connect(db_map.db_user, db_map.db_pwd, db_map.db_host)
            self.cursor = self.conn.cursor()
        except Exception:
            logging.error("Error: 数据库连接失败~")
            print(traceback.format_exc())

    def query(self, sql, time_out):
        """
        查询sql的一个字段返回单个值
        :param sql:
        :param time_out:最大查询时间
        :return:‘’
        """
        try:
            for i in range(time_out):
                rs = self.cursor.execute(sql).fetchone()
                if rs is not None:
                    break
                time.sleep(1)
            if rs is None:
                return ''
            rtn = json.loads(json.dumps(rs, cls=CJsonEncoder, ensure_ascii=False, sort_keys=False))
            if rtn[0] is None:
                return ''
        except Exception as e:
            logging.error(e)
        return rtn[0]

    def query_list(self, sql, time_out):
        """
        查询sql的一个字段返回多个值,以列表展示
        :param sql:
        :param time_out:最大查询时间
        :return:[]
        """
        arr = []
        try:
            for i in range(time_out):
                rs = self.cursor.execute(sql).fetchall()
                if len(rs) > 0:
                    break
                time.sleep(1)
            for data in rs:
                rtn = json.loads(json.dumps(data, cls=CJsonEncoder, ensure_ascii=False, sort_keys=False))
                if rtn[0] is None:
                    arr.append('')
                else:
                    arr.append(rtn[0])
        except Exception as e:
            logging.error(e)
        return arr

    def select(self, sql, time_out):
        """
        查询sql的返回查询的所有字段
        :param sql:
        :param time_out:最大查询时间
        :return:‘’
        """
        dic = {}
        try:
            for i in range(time_out):
                rs = self.cursor.execute(sql).fetchone()
                if rs is not None:
                    break
                time.sleep(1)
            desc = self.cursor.description
            if rs is None:
                return dic
            rtn = json.loads(json.dumps(rs, cls=CJsonEncoder, ensure_ascii=False, sort_keys=False))
            for i in range(len(desc)):
                if rtn[i] is None:
                    dic[desc[i][0]] = ''
                else:
                    dic[desc[i][0]] = rtn[i]
        except Exception as e:
            logging.error(e)
        return dic

    def select_list(self, sql, time_out):
        """
        查询sql的返回多行结果的所有字段,以列表展示
        :param sql:
        :param time_out:最大查询时间
        :return:[]
        """
        arr = []
        try:
            for i in range(time_out):
                rs = self.cursor.execute(sql).fetchall()
                if len(rs) > 0:
                    break
                time.sleep(1)
            desc = self.cursor.description
            for data in rs:
                dic = {}
                rtn = json.loads(json.dumps(data, cls=CJsonEncoder, ensure_ascii=False, sort_keys=False))
                for i in range(len(desc)):
                    if rtn[i] is None:
                        dic[desc[i][0]] = ''
                    else:
                        dic[desc[i][0]] = rtn[i]
                arr.append(dic)
        except Exception as e:
            logging.error(e)
        return arr

    def execute(self, *sqls):
        """
        执行批量插入、删除或更新sql操作，若其中一条失败，则全部执行失败
        :param sqls:
        :return:
        """
        try:
            for sql in sqls:
                self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            logging.error(e)

    def close(self):
        """
        操作数据库后，关闭数据库连接
        :return:
        """
        if self.conn is not None:
            try:
                self.cursor.close()
                self.conn.close()
            except Exception as e:
                logging.error(e)


class Mysql:
    conn = ''
    cursor = ''

    def __init__(self, db_map):
        """
        初始化类，获得Mysql的实例
        :param db_map:
        """
        # noinspection PyBroadException
        try:
            self.conn = pymysql.connect(host=db_map.db_host,
                                        user=db_map.db_user,
                                        password=db_map.db_pwd,
                                        port=db_map.db_post,
                                        charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception:
            logging.error("Error: 数据库连接失败~")
            print(traceback.format_exc())

    def query(self, sql, time_out):
        """
        查询sql的一个字段返回单个值
        :param sql:
        :param time_out:最大查询时间
        :return:‘’
        """
        cursor = ''
        try:
            cursor = self.conn.cursor()
            for i in range(time_out):
                cursor.execute(sql)
                rs = cursor.fetchone()
                if rs is not None:
                    break
                time.sleep(1)
            if rs is None:
                return ''
            rtn = json.loads(json.dumps(rs, cls=CJsonEncoder, ensure_ascii=False, sort_keys=False))
        except Exception as e:
            logging.error(e)
        return rtn[0]

    def query_list(self, sql, time_out):
        """
        查询sql的一个字段返回多个值,以列表展示
        :param sql:
        :param time_out:最大查询时间
        :return:[]
        """
        cursor = ''
        datalist = []
        flag = ''
        try:
            cursor = self.conn.cursor()
            for i in range(time_out):
                cursor.execute(sql)
                rs = cursor.fetchall()
                flag = len(rs)
                print(flag)
                if flag > 0:
                    break
                time.sleep(1)
            for data in rs:
                rtn = json.loads(json.dumps(data, cls=CJsonEncoder, ensure_ascii=False, sort_keys=False))
                if rtn[0] is None:
                    datalist.append('')
                else:
                    datalist.append(rtn[0])
        except Exception as e:
            logging.error(e)
        return datalist

    def select(self, sql, time_out):
        """
        查询sql的返回单行结果的所有字段
        :param sql:
        :param time_out:最大查询时间
        :return:‘’
        """
        cursor = ''
        dic = {}
        try:
            cursor = self.conn.cursor()
            for i in range(time_out):
                cursor.execute(sql)
                rs = cursor.fetchone()
                if rs is not None:
                    break
                time.sleep(1)
            desc = cursor.description
            if rs is None:
                return dic
            rtn = json.loads(json.dumps(rs, cls=CJsonEncoder, ensure_ascii=False, sort_keys=False))
            for i in range(len(desc)):
                if rtn[i] is None:
                    dic[desc[i][0]] = ''
                else:
                    dic[desc[i][0]] = rtn[i]
        except Exception as e:
            logging.error(e)
        return dic

    def select_list(self, sql, time_out):
        """
        查询sql的返回多行结果的所有字段,以列表展示
        :param sql:
        :param time_out:最大查询时间
        :return:[]
        """
        cursor = ''
        arr = []
        try:
            cursor = self.conn.cursor()
            for i in range(time_out):
                cursor.execute(sql)
                rs = cursor.fetchall()
                if len(rs) > 0:
                    break
                time.sleep(1)
            desc = cursor.description
            for data in rs:
                dic = {}
                rtn = json.loads(json.dumps(data, cls=CJsonEncoder, ensure_ascii=False, sort_keys=False))
                for i in range(len(desc)):
                    if rtn[i] is None:
                        dic[desc[i][0]] = ''
                    else:
                        dic[desc[i][0]] = rtn[i]
                arr.append(dic)
        except Exception as e:
            logging.error(e)
        return arr

    def execute(self, *sqls):
        """
        执行批量插入、删除或更新sql操作，若其中一条失败，则全部执行失败
        :param sqls:
        """
        cursor = ''
        try:
            cursor = self.conn.cursor()
            for sql in sqls:
                cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            logging.error(e)

    def close(self):
        """
        操作数据库后，关闭数据库连接
        :return:
        """
        if self.conn is not None:
            try:
                self.cursor.close()
                self.conn.close()
            except Exception as e:
                logging.error(e)

