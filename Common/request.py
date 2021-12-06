# -*- coding: utf-8 -*-
# @Time    : 2021/12/01
# @Author  : chenxubin
# @File    : Request.py

"""
封装request

"""

import requests
import os,sys
import uuid
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Common.mylog import Mylog




class Request:

    def __init__(self):
        pass

    @staticmethod
    def get_request(url, data=None,headers=None,cookies=None):
        """
        封装GET方法
        param url 必填
        param header 选填
        param data 选填
        cookies 选填
        """
        # if not url.startswith('http://'):
        #     url = "%s%s" % ("http://",url)
        #     print(url)

        try:
            if data == None:

                responce = requests.get(url,headers=headers,cookies=cookies)

            else:
                responce = requests.get(url,params=data,headers=headers,cookies=cookies)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            Mylog.info(e)

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            Mylog.info(e)


        # time_consuming为响应时间，单位为毫秒
        time_consuming = responce.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = responce.elapsed.total_seconds()

        # Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['status_code'] = responce.status_code

        response_dicts['response_body'] = responce.json()
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts


    @staticmethod
    def post_request(url,data,headers=None,cookies=None):
        """
        封装了post方法
        param url 必填
        param data 选填
        param header 选填
        param cookes  选填

        """
        # if not url.startswith("http://"):
        #     url = "%s%s" % ("http://",url)

        try:

            responce = requests.post(url, data=data,headers=headers, cookies=cookies)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            Mylog.info(e)

        # time_consuming为响应时间，单位为毫秒
        time_consuming = responce.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = responce.elapsed.total_seconds()
        # Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['status_code'] = responce.status_code
        response_dicts['response_body'] = responce.json()

        # response_dicts['text'] = responce.text
        response_dicts['time_consuming'] = str(time_consuming) + ' ms'
        response_dicts['time_total'] = time_total

        return response_dicts


if __name__ == "__main__":

    res = Request()







