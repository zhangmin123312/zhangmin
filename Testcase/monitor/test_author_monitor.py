# -*- coding: utf-8 -*-
# @Time    : 2022/8/12
# @Author  : zhangmin
# @File    : test_author_monitor.py

import allure
import jsonpath
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os,json
import datetime
import random

@allure.feature('达人监控')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_author_monitor():
    @allure.description("""验证添加达人监控,切换监控时长，达人监控列表显示是否正确""")
    @allure.title("添加达人监控，切换监控时长，监控列表正确显示")
    @pytest.mark.parametrize('track_time', ["24h", "48h", '72h', '7d'])
    def test_author_monitor_track_create(self, get_token, get_host, add_author_monitor,track_time):
        nickname, unique_id, author_id = add_author_monitor
        datatime1=datetime.datetime.now()+ datetime.timedelta(days=1)
        yuyue_start_time= datatime1.strftime('%Y-%m-%d %H:%M')
        datatime2=datetime.datetime.now()+ datetime.timedelta(days=3)
        yuyue_end_time = datatime2.strftime('%Y-%m-%d %H:%M')
        data={'track_author_id': author_id,
              'track_config_fans': 0,
              'track_config_goods': 0,
              'track_config_likes': 0,
              'track_time': track_time,
              'track_type': 2,
              'yuyue_end_time': yuyue_end_time,
              'yuyue_start_time': yuyue_start_time}
        response1 = base().return_request(method="post", path=PathMessage.track_create, data=data, tokens=get_token,
                                                hosts=get_host)
        # print(response1)
        trackId=response1['response_body']["data"]['trackId']
        data_history={
                'keyword':'',
                'list_type':'author',
                'page':'1',
                'pagesize':15,
                'status':0
            }
        response2 = base().return_request(method="post", path=PathMessage.track_history, data=data_history, tokens=get_token,
                                           hosts=get_host)
        trackId_list = jsonpath.jsonpath(response2["response_body"], f'$.data.track_lists[*].track_info.trackId')
        # print(trackId_list)
        # print(response2)
        #判断监控是否添加成功
        assert response1["status_code"] == 200
        assert trackId>0
        #判断监控的达人是否在列表里
        assert trackId in trackId_list


    @allure.description("""验证筛选达人监控状态，达人监控列表是否正确""")
    @pytest.mark.parametrize("status",[-1,0,1,2])
    @allure.title("筛选达人监控状态{status}，监控列表正确显示")
    def test_author_monitor_track_history_status(self, get_token, get_host,status):
        data={
            'keyword':'',
            'list_type':'author',
            'page':'1',
            'pagesize':15,
            'status':status
        }
        response = base().return_request(method="post", path=PathMessage.track_history, data=data, tokens=get_token,
                                                     hosts=get_host)
        print(response)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["track_lists"]) > 0

    @allure.description("""验证达人监控页面搜索抖音号是否正确""")
    @allure.title("验证达人监控页面搜索抖音号是否正确")
    def test_author_monitor_track_history_uniqueid(self, get_token, get_host, add_author_monitor):
        nickname, unique_id, author_id = add_author_monitor
        data = {"keyword": unique_id,
                'list_type': 'author',
                'page': '1',
                'pagesize': 15,
                'status':-1
                }
        # print(data)
        response = base().return_request(method="post", path=PathMessage.track_history, data=data, tokens=get_token,
                                         hosts=get_host)
        # print(response)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["track_lists"]) > 1
        unique_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.track_lists[*].author_info.unique_id')
        # print(unique_id_list)
        assert unique_id in unique_id_list

    @allure.description("""验证添加达人监控,开启点赞数，监控正确显示""")
    @allure.title("添加达人监控，开启点赞数，监控正确显示")
    @pytest.mark.parametrize('like_number', ['50','500','5000'])
    def test_author_monitor_track_create_like(self, get_token, get_host, add_author_monitor,like_number):
        nickname, unique_id, author_id = add_author_monitor
        datatime1=datetime.datetime.now()+ datetime.timedelta(days=1)
        yuyue_start_time= datatime1.strftime('%Y-%m-%d %H:%M')
        datatime2=datetime.datetime.now()+ datetime.timedelta(days=1)
        yuyue_end_time = datatime2.strftime('%Y-%m-%d %H:%M')
        data={'track_author_id': author_id,
              'track_config_fans': 0,
              'track_config_goods': 0,
              'track_config_likes': 1,
              'track_config_likes_number': like_number,
              'track_time': '24h',
              'track_type': 2,
              'yuyue_end_time': yuyue_end_time,
              'yuyue_start_time': yuyue_start_time}
        response1 = base().return_request(method="post", path=PathMessage.track_create, data=data, tokens=get_token,
                                                hosts=get_host)
        # print(response1)
        trackId=response1['response_body']["data"]['trackId']
        data_history = {
            'keyword': '',
            'list_type': 'author',
            'page': '1',
            'pagesize': 15,
            'status': 0
        }
        response2 = base().return_request(method="post", path=PathMessage.track_history, data=data_history, tokens=get_token,
                                           hosts=get_host)
        trackId_list = jsonpath.jsonpath(response2["response_body"], f'$.data.track_lists[*].track_info.trackId')
        # print(trackId_list)
        # print(response2)
        #判断监控是否添加成功
        assert response1["status_code"] == 200
        assert trackId>0
        #判断监控的达人是否在列表里
        assert trackId in trackId_list



    @allure.description("""验证添加监控弹窗搜索昵称，监控列表是否正确显示""")
    @allure.title("搜索昵称，监控列表正确显示")
    def test_author_monitor_nickname(self, get_token, get_host, add_author_monitor):
        nickname, unique_id,author_id= add_author_monitor
        data = {"keyword":nickname}
        # print(data)
        response = base().return_request(method="post", path=PathMessage.authorSearch, data=data, tokens=get_token,
                                         hosts=get_host)
        # print(response)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["author_info"]) > 10
        nickname_list = response["response_body"]["data"]["author_info"]["nickname"]
        # print(nickname_list)
        assert nickname in nickname_list

    @allure.description("""验证添加监控弹窗搜索抖音号，监控列表是否正确显示""")
    @allure.title("搜索抖音号，监控列表正确显示")
    def test_author_monitor_unique_id(self, get_token, get_host, add_author_monitor):
        nickname, unique_id, author_id = add_author_monitor
        data = {"keyword":unique_id }
        # print(data)
        response = base().return_request(method="post", path=PathMessage.authorSearch, data=data, tokens=get_token,
                                             hosts=get_host)
        # print(response)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["author_info"]) > 10
        unique_id_list = response["response_body"]["data"]["author_info"]["unique_id"]
        # print(unique_id_list)
        assert unique_id in unique_id_list

    @allure.description("""验证删除已监控完成的达人，监控列表是否正确""")
    @allure.title("删除已监控完成的达人")
    def test_author_monitor_delete_finish_id(self, get_token, get_host, delete_author_monitor):
        trackId = delete_author_monitor

        # print(data)
        for  value in trackId:
            data = {"trackId": value}
            delete_response = base().return_request(method="post", path=PathMessage.track_delete, data=data, tokens=get_token,
                                             hosts=get_host)



