# -*- coding: utf-8 -*-
# @Time    : 2021/12/31
# @Author  : zhangmin
# @File    : test_rank_subject.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os

@allure.feature('话题榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_subject():

    @allure.story('验证昨日话题榜返回的数据是否大于0条')
    # @pytest.mark.parametrize('times',str(base.return_time_message()[0][1]))
    # @allure.title("话题榜日期:{times}")
    def test_rank_subject_day(self,get_token,get_host):
        times=base.return_time_message()[0][1]
        para="day_type=day&date={}&order=aweme_count_inc&page=1&size=50".format(times)
        responce = base().return_request(method="get", path=PathMessage.rank_subject, data=para,tokens=get_token,hosts=get_host)
        assert len(responce["response_body"]["data"]["list"]) > 0


    @allure.story('验证昨日话题榜排序')
    @pytest.mark.parametrize('sort', ["aweme_count_inc", "interact_inc"])
    @allure.title("热门话题榜排序：{sort}")
    def test_rank_subject_sort(self, get_token, get_host, sort):
        times = base.return_time_message()[0][1]
        para="day_type=day&date={}&order={}&page=1&size=50".format(times,sort)
        responce = base().return_request(method="get", path=PathMessage.rank_subject, data=para, tokens=get_token,
                                         hosts=get_host, )["response_body"]["data"]["list"]
        interact_inc = float("inf")
        aweme_count_inc = float("inf")
        if sort =="aweme_count_inc":
            for i in responce:
                assert i["aweme_count_inc"] <= aweme_count_inc
                aweme_count_inc = i["aweme_count_inc"]
        elif sort == "interact_inc":
            for i in responce:
                assert i["interact_inc"] <= interact_inc
                interact_inc = i["interact_inc"]

