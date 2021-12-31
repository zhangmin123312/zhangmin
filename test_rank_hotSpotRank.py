# -*- coding: utf-8 -*-
# @Time    : 2021/12/31
# @Author  : zhangmin
# @File    : test_rank_hotSpotRank.py


import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
from Testcase.live.conftest import soundbyte_timestamps
import os,jsonpath
import datetime
@allure.feature('热点榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)


class TestCase_Rank_hotSpotRank():

    @allure.story('验证今日实时热点榜返回的数据是否大于0条')
    @allure.title("榜点：{soundbyte_timestamps}")
    def test_hotSpotRank(self,get_token,get_host,soundbyte_timestamps):
        time = base.return_time_message()[0][1]
        para = "day_type=day&date={}&page=1&size=50&type=1&timestamp={}".format(time,soundbyte_timestamps)
        responce = base().return_request(method="get", path=PathMessage.rank_hotSpotRank, data=para,tokens=get_token,hosts=get_host)
        # print(responce)
        assert len(responce["response_body"]["data"]) > 0

    @allure.story('验证今日飙升热点榜返回的数据是否大于0条')
    @allure.title("榜点：{soundbyte_timestamps}")
    def test_riseAwemeRank(self,get_token,get_host,soundbyte_timestamps):
        time = base.return_time_message()[0][1]
        para = "day_type=day&date={}&page=1&size=50&type=2&timestamp={}".format(time,soundbyte_timestamps)
        responce = base().return_request(method="get", path=PathMessage.rank_hotSpotRank, data=para,tokens=get_token,hosts=get_host)
        # print(responce)
        assert len(responce["response_body"]["data"]) > 0




