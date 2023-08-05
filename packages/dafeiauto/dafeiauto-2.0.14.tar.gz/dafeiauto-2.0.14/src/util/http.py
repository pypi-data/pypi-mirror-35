#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json

class Webhttp:
    def __init__(self, headers={}):
        self.set_header(headers)

    # 设置http头
    def set_header(self, headers):
        self.headers = headers

    def get(self, url, para):
        """
        :param url:  链接
        :param para: 参数 {user: 111, psd: 2222}
        :return:
        """
        try:
            r = requests.get(url, params=para, headers=self.headers)
            json_r = r.json()
            result = {
                'status': r.status_code,
                'data': json_r
            }
            return result
        except BaseException as e:
            print("请求失败！", str(e))

    def get_need_pwd(self, url, para , username , password):
        """
        :param url:  链接
        :param para: 参数 {user: 111, psd: 2222}
        :return:
        """
        try:
            r = requests.get(url, params=para, headers=self.headers,auth=(username, password))
            print(r)
            json_r = r.json()
            result = {
                'status': r.status_code,
                'data': json_r
            }
            return result
        except BaseException as e:
            print("请求失败！", str(e))

    def post(self, url, para):
        """
           :param url:  链接
           :param para: 参数 {user: 111, psd: 2222}
           :return:
        """
        try:
            r = requests.post(url, data=para, headers=self.headers)
            json_r = r.json()
            result = {
                'status': r.status_code,
                'data': json_r
            }
            return result
        except BaseException as e:
            print("请求失败！", str(e))

    def post_json(self, url, para):
        """
             :param url:  链接
             :param para: 参数 {user: 111, psd: 2222}
             :return:
        """
        try:
            data = para
            data = json.dumps(data)   # python数据类型转化为json数据类型
            r = requests.post(url, data=data, headers=self.headers)
            json_r = r.json()
            result = {
                'status': r.status_code,
                'data': json_r
            }
            return result
        except BaseException as e:
            print("请求失败！", str(e))
