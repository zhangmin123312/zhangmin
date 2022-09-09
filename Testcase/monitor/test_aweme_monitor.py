# -*- coding: utf-8 -*-
# @Time    : 2022/9/12
# @Author  : zhangmin
# @File    : test_aweme_monitor.py

import allure
import jsonpath
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os,json
import datetime
import random


@allure.feature('视频监控')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_aweme_monitor():


    @allure.description("""验证视频名称搜索，监控列表是否正确""")
    @allure.title("验证监控列表视频名称搜索")

    @allure.description("""验证添加视频监控，切换视频监控时长，监控列表是否正确""")
    @allure.title("验证添加视频监控")
    @pytest.mark.parametrize('timeConfig', ["24h", "48h", '72h', '7d'])
    def test_aweme_monitor_track_create(self, get_token, get_host, add_aweme_monitor,timeConfig):
        nickname,aweme_url,aweme_title=add_aweme_monitor
        data={"keyword":aweme_url}
        response1 = base().return_request(method="post", path=PathMessage.aweme_monitor_search, data=data, tokens=get_token,
                                          hosts=get_host)
        aweme_id=response1["response_body"]["data"]["aweme_info"]["aweme_id"]

        create_data={"track_aweme_id":aweme_id,
                "track_config_fans":0,
                "track_config_goods":0,
                "track_config_likes":0,
                "track_time":timeConfig,
                "track_type":1}
        response2 = base().return_request(method="post", path=PathMessage.track_create, data=create_data, tokens=get_token,
                                          hosts=get_host)
        trackId = response2['response_body']["data"]['trackId']
        # print(trackId)
        data = {
            'keyword': '',
            'list_type': 'aweme',
            'page': '1',
            'pagesize': 15,
            'status': -1
        }
        responce = base().return_request(method="post", path=PathMessage.track_history,
                                         data=json.dumps(data), tokens=get_token,
                                         hosts=os.environ["host"])
        trackId_history = jsonpath.jsonpath(responce["response_body"], f'$.data.track_lists[*].track_info.trackId')
        # print(trackId_history)

        assert response2["status_code"] == 200
        assert trackId in trackId_history



    @allure.description("""验证视频监控状态筛选，监控列表是否正确""")
    @pytest.mark.parametrize("status", [-1, 1, 2])
    @allure.title("筛选视频监控状态{status}，监控列表正确显示")

    def test_aweme_monitor_status(self, get_token, get_host, add_aweme_monitor,status):
        nickname,aweme_url,aweme_title=add_aweme_monitor
        data = {
            'keyword': '',
            'list_type': 'aweme',
            'page': '1',
            'pagesize': 15,
            'status': status
        }
        responce = base().return_request(method="post", path=PathMessage.track_history,
                                         data=json.dumps(data), tokens=get_token,
                                         hosts=os.environ["host"])
        assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["track_lists"]) > 0

    @allure.description("""验证视频链接搜索，监控列表是否正确""")
    @allure.title("验证监控列表视频链接搜索")
    def test_aweme_monitor_aweme_url(self, get_token, get_host, add_aweme_monitor):
            nickname, aweme_url, aweme_title = add_aweme_monitor
            data = {
                'keyword': aweme_url,
                'list_type': 'aweme',
                'page': '1',
                'pagesize': 15,
                'status': -1
            }
            responce = base().return_request(method="post", path=PathMessage.track_history,
                                             data=json.dumps(data), tokens=get_token,
                                             hosts=os.environ["host"])
            assert responce["status_code"] == 200
            assert len(responce["response_body"]["data"]["track_lists"]) > 0

    @allure.description("""验证视频标题搜索，监控列表是否正确""")
    @allure.title("验证监控列表视频标题搜索")
    def test_aweme_monitor_aweme_title(self, get_token, get_host, add_aweme_monitor):
        nickname, aweme_url, aweme_title = add_aweme_monitor
        data = {
            'keyword': aweme_title,
            'list_type': 'aweme',
            'page': '1',
            'pagesize': 15,
            'status': -1
        }
        responce = base().return_request(method="post", path=PathMessage.track_history,
                                         data=json.dumps(data), tokens=get_token,
                                         hosts=os.environ["host"])
        assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["track_lists"]) > 0


    @allure.description("""验证删除已监控完成的视频，监控列表是否正确""")
    @allure.title("删除已监控完成的视频")
    def test_aweme_monitor_delete_finish_id(self, get_token, get_host, delete_aweme_monitor):
        trackId = delete_aweme_monitor

        print(trackId)
        for value in trackId:
            data = {"trackId": value}
            print(data)
            delete_response = base().return_request(method="post", path=PathMessage.track_delete, data=data,
                                                    tokens=get_token,
                                                    hosts=get_host)