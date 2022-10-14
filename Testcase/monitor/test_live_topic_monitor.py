# -*- coding: utf-8 -*-
# @Time    : 2022/9/20
# @Author  : zhangmin
# @File    : test_live_topic_monitor.py

import allure
import jsonpath
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os,json
import datetime
import time
import random
@allure.feature('话术监控')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_live_topic_monitor():
    @allure.description("""验证添加话术监控,监控列表显示是否正确""")
    @allure.title("验证添加话术监控,监控列表显示是否正确")
    def test_live_topic_monitor_create(self, get_token, get_host, add_live_topic_monitor):
        nickname, unique_id, author_id = add_live_topic_monitor
        datatime1 = datetime.datetime.now()+ datetime.timedelta(days=1)
        start_time = int(time.mktime(datatime1.timetuple()))
        datatime2= datetime.datetime.now()+ datetime.timedelta(days=2)
        end_time = int(time.mktime(datatime2.timetuple()))
        #话术监控弹窗搜索
        data = {"keyword": nickname}
        author_response=base().return_request(method="post", path=PathMessage.author_multiSearch, data=data, tokens=get_token,
                                                hosts=get_host)['response_body']["data"]['search_results'][0]["author_info"]["author_id"]
        # print(author_multiSearch_response)
        #话术监控添加
        topic_date={
            'author_id': author_response,
            'end_time': end_time,
            'start_time': start_time,
            'notice':0
        }
        add_live_topic_monitor_response=base().return_request(method="post", path=PathMessage.add_topic_monitor, data=topic_date, tokens=get_token,
                                                hosts=get_host)
        topic_monitor=add_live_topic_monitor_response["response_body"]['data']['monitor_id']
        # 话术监控列表
        para='page=1&size=15&status=-1&keyword='
        topic_monitor_list_response = base().return_request(method="get", path=PathMessage.topic_monitor_list,
                                                                data=para, tokens=get_token,
                                                                hosts=get_host)
        topic_monitor_list=jsonpath.jsonpath(topic_monitor_list_response["response_body"], f'$.data.list[*].id')

        assert add_live_topic_monitor_response["status_code"] == 200
        assert topic_monitor>0
        #判断监控的达人是否在列表里
        assert topic_monitor in topic_monitor_list


    @allure.description("""验证话术监控页面搜索抖音号是否正确""")
    @allure.title("验证话术监控页面搜索抖音号是否正确")
    def test_live_topic_monitor_seach_unique_id(self, get_token, get_host, add_live_topic_monitor):
        nickname, author_id,unique_id = add_live_topic_monitor
        para=f'page=1&size=15&status=-1&keyword={unique_id}'
        response=base().return_request(method="get", path=PathMessage.topic_monitor_list,
                                                                data=para, tokens=get_token,
                                                                hosts=get_host)
        seach_monitor_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].author_info.unique_id')
        assert response["status_code"] == 200
        assert unique_id in seach_monitor_list

    @allure.description("""验证话术监控页面搜索达人名称是否正确""")
    @allure.title("验证话术监控页面搜索达人名称是否正确")
    def test_live_topic_monitor_seach_nickname(self, get_token, get_host, add_live_topic_monitor):
        nickname, unique_id, author_id = add_live_topic_monitor
        para=f'page=1&size=15&status=-1&keyword={nickname}'
        response=base().return_request(method="get", path=PathMessage.topic_monitor_list,
                                                                data=para, tokens=get_token,
                                                                hosts=get_host)
        seach_monitor_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].author_info.nickname')
        assert response["status_code"] == 200
        assert nickname in seach_monitor_list

    @allure.description("""验证删除已监控完成的话术，监控列表是否正确""")
    @allure.title("删除已监控完成的话术")
    def test_live_topic_monitor_finish_delete(self, get_token, get_host):
        delete_para='page=1&size=1&status=2&keyword='
        monitor_finish_response=base().return_request(method="get", path=PathMessage.topic_monitor_list,
                                                                data=delete_para, tokens=get_token,
                                                                hosts=get_host)
        monitor_finish_list=jsonpath.jsonpath(monitor_finish_response["response_body"], f'$.data.list[*].id')
        print(monitor_finish_list)
        for value in monitor_finish_list:
            data = {'monitor_id': value}
            print(data)
            monitor_delete_response = base().return_request(method="post", path=PathMessage.topic_monitor_delete,
                                                            data=data, tokens=get_token,
                                                            hosts=get_host)
            print(monitor_delete_response)
            assert monitor_delete_response["status_code"] == 200
    @allure.description("""验证话术监控置顶，监控列表是否正确""")
    @allure.title("验证话术监控置顶")
    def test_live_topic_monitor_topSwitch(self, get_token, get_host):
        para='page=1&size=15&status=-1&keyword='
        topic_monitor_list_response = base().return_request(method="get", path=PathMessage.topic_monitor_list,
                                                                data=para, tokens=get_token,
                                                                hosts=get_host)
        topic_monitor=jsonpath.jsonpath(topic_monitor_list_response["response_body"], f'$.data.list[*].id')
        data={'monitor_id':topic_monitor[1],'top':1 }
        topic_monitor_topSwitch =base().return_request(method="post", path=PathMessage.topic_monitor_topSwitch,
                                                                data=data, tokens=get_token,
                                                                hosts=get_host)
        topic_monitor_list_response1 = base().return_request(method="get", path=PathMessage.topic_monitor_list,
                                                            data=para, tokens=get_token,
                                                            hosts=get_host)
        topic_monitor1 = jsonpath.jsonpath(topic_monitor_list_response1["response_body"], f'$.data.list[*].id')
        assert topic_monitor_topSwitch["status_code"] == 200
        assert topic_monitor1[0] == topic_monitor[1]
    @allure.description("""验证话术监控取消置顶，监控列表是否正确""")
    @allure.title("验证话术监控取消置顶")
    def test_live_topic_monitor_topSwitch_(self, get_token, get_host):
        para='page=1&size=15&status=-1&keyword='
        topic_monitor_list_response = base().return_request(method="get", path=PathMessage.topic_monitor_list,
                                                                data=para, tokens=get_token,
                                                                hosts=get_host)
        topic_monitor=jsonpath.jsonpath(topic_monitor_list_response["response_body"], f'$.data.list[*].id')
        data={'monitor_id':topic_monitor[0],'top':0 }
        topic_monitor_topSwitch =base().return_request(method="post", path=PathMessage.topic_monitor_topSwitch,
                                                                data=data, tokens=get_token,
                                                                hosts=get_host)
        topic_monitor_list_response1 = base().return_request(method="get", path=PathMessage.topic_monitor_list,
                                                            data=para, tokens=get_token,
                                                            hosts=get_host)
        topic_monitor1 = jsonpath.jsonpath(topic_monitor_list_response1["response_body"], f'$.data.list[*].id')
        assert topic_monitor_topSwitch["status_code"] == 200
        assert topic_monitor1[0] != topic_monitor[0]




















