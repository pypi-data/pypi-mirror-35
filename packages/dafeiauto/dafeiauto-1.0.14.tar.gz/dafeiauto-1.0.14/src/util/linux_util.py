#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
import paramiko, ftplib, subprocess, logging, sys, time, os, stat, re
from src.util.logger_util import Logger

class Linux(object):

    def __init__(self, host, username, pwd, port=22):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None
        self.try_times = 3  # 链接失败的重试次数
        self.connect()

    def close(self):
        self.__transport.close()

    def connect(self):
        try:
            transport = paramiko.Transport((self.host, self.port))
            transport.connect(username=self.username, password=self.pwd)
        except Exception as e:
            logging.error("%s\tSSH链接\n" % (e))
        else:
            self.__transport = transport

    def command(self, cmd):
        """
        发送指令  执行命令,不可执行类似vim，top watch命令
        :param cmd:  指令 []
        :return: 命令结果 数组 []
        """
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh._transport = self.__transport
            result = {}
            for m in cmd:
                stdin, stdout, stderr = ssh.exec_command(m)
                out = stdout.readlines()
                out = "".join(out).strip("\n")
                result[cmd.index(m)] = out
            return result
            logging.info("%s\tssh发送指令，OK\n" % (host))
            ssh.close()
        except:
            logging.error("%s\tssh发送指令\n" % (host))
            return "Null_"

    def mkdirs(self, local_path,  power="0777"):
        try:
            sftp = paramiko.SFTPClient.from_transport(self.__transport)
            sftp.mkdir(local_path, int( power))
            logging.info("%s\t\已创建成功\n" % (local_path))
        except IOError:
            logging.info("%s\t\已存在\n" % (local_path))
        else:
            return (1, "OK")

    def __get_all_files_in_local_path(self, local_path):
        """
        获取本地指定目录及其子目录下的所有文件
        :param local_dir: 路径
        :return: 路径下所有文件
        """
        # 保存所有文件的列表
        all_files = list()

        # 获取当前指定目录下的所有目录及文件，包含属性值
        files = os.listdir(local_path)
        for x in files:
            # local_dir目录中每一个文件或目录的完整路径
            filename = os.path.join(local_path, x)
            # 如果是目录，则递归处理该目录
            if os.path.isdir(x):
                all_files.extend(self.__get_all_files_in_local_path(filename))
            else:
                all_files.append(filename)
        return all_files

    def upload(self, local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        __temp_path = os.path.split(local_path)  # 分离文件和文件名
        # 文件单个上传
        print('%s开始上传...' % local_path)
        if os.path.isfile(local_path):
            filename = __temp_path[1]
            remote_filename = remote_path + '/' + filename
            start = time.clock()
            print(u'Put文件%s传输中...' % filename)
            sftp.put(local_path, remote_filename)
            end = time.clock()
            time.sleep(1)
            print('%s上传成功,用时： %fs' % (filename, (end - start)))
            return

        # 目录循环上传
        all_files = self.__get_all_files_in_local_path(local_path) # 获取本地指定目录及其子目录下的所有文件
        # 依次put每一个文件
        if all_files == []:
            print("%s下无文件，无法上传" % local_path)
            return
        if remote_path[-1] == '/':    # 去掉路径字符穿最后的字符'/'，如果有的话
            remote_path = remote_path[0:-1]
        for x in all_files:
            try:
                start = time.clock()
                filename = os.path.split(x)[-1]
                remote_filename = remote_path + '/' + filename
                print(u'Put文件%s传输中...' % filename)
                sftp.put(x, remote_filename)
                end = time.clock()
                time.sleep(1)
                print(' %s上传成功,用时： %fs' % (filename, (end - start)))
            except Exception as e:
                print('%s上传失败:' % filename, e)
                print("日志打印")
                continue  # 上传出错继续进行下一步
            else:
                print("日志打印1111111")

    def __get_all_files_in_remote_path(self, sftp, remote_path):
        """
        获取远端linux主机上指定目录及其子目录下的所有文件
        :param sftp:
        :param remote_dir:
        :return:
        """
        # 保存所有文件的列表
        all_files = list()

        # 去掉路径字符串最后的字符'/'，如果有的话
        if remote_path[-1] == '/':
            remote_path = remote_path[0:-1]

        # 获取当前指定目录下的所有目录及文件，包含属性值
        files = sftp.listdir_attr(remote_path)
        for x in files:
            # remote_patn目录中每一个文件或目录的完整路径
            filename = remote_path + '/' + x.filename
            # 如果是目录，则递归处理该目录
            if stat.S_ISDIR(x.st_mode):
                all_files.extend(self.__get_all_files_in_remote_path(sftp, filename))
            else:
                all_files.append(filename)
        return all_files

    def download(self, remote_path, local_path):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        print('开始下载...')
        __temp_path = os.path.split(remote_path) # 分离文件和文件名
        if __temp_path[1] is not '':
            start = time.clock()
            filename = __temp_path[1]
            local_filename = os.path.join(local_path, filename)
            print(u'Get文件%s传输中...' % filename)
            sftp.get(remote_path, local_filename)
            end = time.clock()
            time.sleep(1)
            print('%s下载成功,用时： %fs' % (filename, (end - start)))
            return
        # 读取目录上传多个文件
        # 获取远端linux主机上指定目录及其子目录下的所有文件
        all_files = self.__get_all_files_in_remote_path(sftp, remote_path)
        # 依次get每一个文件
        if all_files is None:
            logging.error("%s\t\服务器路径下错误\n" % (remote_path))
        else:
            for x in all_files:
                try:
                    start = time.clock()
                    filename = x.split('/')[-1]
                    local_filename = os.path.join(local_path, filename)
                    print(u'Get文件%s传输中...' % filename)
                    sftp.get(x, local_filename)
                    end = time.clock()
                    time.sleep(1)
                    print(' %s下载成功,用时： %fs' % (filename, (end - start)))
                except Exception as e:
                        print('%s下载失败:' % filename, e)
                        print("日志打印")
                        continue  # 下载出错继续进行下一步
                else:
                    print("日志打印1111111")
                    # with open(r'C:\Users\Neil\Desktop\Test\time.log', 'a') as f:
                    #         f.write('success download %s\n' % filename)

    def isexist(self, remote_path):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh._transport = self.__transport
        sftp = ssh.open_sftp()
        try:
            sftp.stat(remote_path)
            print("exist11111")
        except IOError:
            print("not exist")

    def delete(self, remote_path):
        """
        删除文件/文件夹
        :param remote_path: 服务器需要删除路径
        :return:
        """
        __temp_path = os.path.split(remote_path)
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        if __temp_path[1] is not '':
            # 删除单个
            sftp.remove(remote_path)
        else:
            # 删除目录
            if remote_path[-1] == '/':
                remote_path = remote_path[0:-1]
            sftp.command(['rm -rf %s' % remote_path])

# if __name__ == "__main__":
#     host = "10.20.10.115"
#     username = "penglujia"
#     password = "Dafy@123"
#     cmd = ['cal', 'ls', 'cd /home/penglujia/DEV-web;ls', 'cd /home/penglujia/DEV-web/test01/src/router;ls']
#     ssh = Linux(host, username, password)
#     r = ssh.command(cmd)
#   #  ssh.delete('/home/penglujia/tempdel/')
#     # print("0---", r[0])
#     # print("1---", r[1])
#     # print("2---", r[2])
#    #  ssh.upload("D:/Users/zhuojiamin/Desktop/temp/", "/home/penglujia/tempdel")
#     # print("2---", r[2])
#     # ssh.mkdirs("/home/penglujia/DEV-web/tempzjm.docx")
#     # ssh.download("/home/penglujia/DEV-web/test01/src/", "D:/Users/zhuojiamin/Desktop/temp/")
#     #  ssh.isexist("/home/penglujia/DEV-web/tempzjm002111.docx")
#     ssh.close()