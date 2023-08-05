# 发送邮件 包含发送多人，附件
# -*- coding:utf-8 -*-
import os, datetime, smtplib, traceback, logging as Log, time
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
from email.mime.multipart import MIMEMultipart
from config.read_ini import Read

CURRENT_PATH = os.path.dirname(os.path.realpath('.'))
READEMAIL = Read('email').get('mail')

class Send:
    """
    # 发送配置
    # :param to_addr_in 接收方 多人下用分号分割
    # :param filepath_in 发送附件路径
    """
    def __init__(self, params):
        test_begin_time = params['test_begin_time']
        test_end_time = params['test_end_time']
        to_addr_in = params['to_addr_in']
        filepath_in = params['filepath_in']
        content = params['content']
        if content is None or content == '':
            content = ''
        msg = MIMEMultipart()
        # 第一个为文本内容,第二个设置文本格式,第三个编码格式
        # msg = MIMEText('多人发送', 'plain', 'utf-8')
        # 发件人栏目显示
        msg['From'] = _format_addr(READEMAIL.mail_account)
        # 收件人栏目显示
        if to_addr_in == '' or to_addr_in is None:
            to_addr_in = READEMAIL.mail_reaccounts
        msg['To'] = to_addr_in
        # 标题
        nowtime = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
        msg['Subject'] = Header(READEMAIL.mail_subject + nowtime, 'utf-8')
        # 附件
        if filepath_in == '' or filepath_in is None:
            filepath_in = os.path.join(CURRENT_PATH, 'output\\report\\')
        send_file(test_begin_time, test_end_time, msg, filepath_in, content)
        # 图片
        imgpath_in = ''
        # 发送方
        from_addr = READEMAIL.mail_account
        # 发送邮箱的授权码
        password = READEMAIL.mail_password

        # qq的smtp服务器
        smtp_server = READEMAIL.mail_host
        # 接收方
        to_addr_in = READEMAIL.mail_reaccounts

        try:
            # 使用了ssl模式
            server = smtplib.SMTP_SSL(smtp_server, 465)
            # 设置为调试模式
            server.set_debuglevel(1)
            # 登陆ssl服务器
            server.login(from_addr, password)
            # 发送邮件
            server.sendmail(from_addr, to_addr_in.split(';'), msg.as_string())
            # 退出
            server.quit()
        except AttributeError as e:
            Log.error("Error: 邮件发送失败哦~", traceback.format_exc())


def getTimeDiff(timeStra,timeStrb):
    """
    #时间a减去时间b，获得二者的时间差,参数为时间字符串，例如：2017-03-30 16:54:01.660
    :param self:
    :param timeStra:
    :param timeStrb:
    :return:
    """
    if timeStra<=timeStrb:
        return 0
    ta = time.strptime(timeStra, "%Y-%m-%d %H:%M:%S")
    tb = time.strptime(timeStrb, "%Y-%m-%d %H:%M:%S")
    y,m,d,H,M,S = ta[0:6]
    dataTimea=datetime.datetime(y,m,d,H,M,S)
    y,m,d,H,M,S = tb[0:6]
    dataTimeb=datetime.datetime(y,m,d,H,M,S)
    secondsDiff=(dataTimea-dataTimeb).seconds
    #两者相加得转换成分钟的时间差
    daysDiff = (dataTimea - dataTimeb).days
    minutesDiff = daysDiff * 1440 + round(secondsDiff / 60, 1)
    hour = str(int(minutesDiff / 60)).rjust(2,'0')
    minute = str(int(minutesDiff % 60)).rjust(2,'0')
    second = str(secondsDiff).rjust(2,'0')
    return hour + "小时" +minute + "分钟" + second + '秒'

def _format_addr(s):
    """
    # 中文处理
    :param s:
    :return: 返回中文字符
    """
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 发送的附件
def send_file(test_begin_time, test_end_time, msg, filepath_in, content):
    filepath = filepath_in
    r = os.path.exists(filepath)
    if r is False:
        msg.attach(MIMEText("""
        ****************这是一封自动发送的邮件，请勿回复****************
        \n\n\n
        """ + content, 'plain', 'utf-8'))
    else:
        total_time = getTimeDiff(test_end_time, test_begin_time)
        # 邮件正文是IMEText:
        msg.attach(MIMEText("""
        ****************这是一封自动发送的邮件，请勿回复****************
        \n\n\n
        <br/>
        """ + content + """
        \n\n\n
        <br/>
        本次测试开始时间 """ + test_begin_time +
        """
        <br/>
        测试结束时间：""" + test_end_time + """
        <br/>
        测试花费时间：""" + total_time + """
        <br/>
        测试运行结果: <a style="color: rgb(17, 85, 204);" href='http://localhost:63342/aotutest/src/report/report.html?_ijt=p8ugflmrl8g6cj43prdmsdafkh'>测试报告</a>"""
         , 'html', 'utf-8'))
        # 遍历指定目录，显示目录下的所有文件名
        pathDir = os.listdir(filepath)
        for allDir in pathDir:
            child = os.path.join(filepath, allDir)
            child.encode().decode("utf-8")  # .decode('gbk') 解决乱码
            # 添加附件， 就是加上一个MINEBase，读取文件
            with open(child, 'rb') as f:
                # 设置附件的MIME类型和文件名
                mime = MIMEBase('file', 'xls', filename=allDir)
                # 头信息
                mime.add_header('Content-Disposition', 'attachment', filename=allDir)
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                # 读取附件内容
                mime.set_payload(f.read())
                # Base64编码
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart 多个
                msg.attach(mime)
        return msg

# if __name__ == "__main__":
# 开始时间，结束时间，接收方(email.ini读取)
#   Send('2018-04-09 11:29:22', '2018-04-09 12:19:18', read_email.mail_reaccounts)