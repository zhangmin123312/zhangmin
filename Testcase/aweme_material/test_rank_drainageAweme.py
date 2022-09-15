# -*- coding: utf-8 -*-
# @Time    : 2022/9/14
# @Author  : youjiangyong
# @File    : test_drainageAweme.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath,datetime,random

@allure.feature('引流视频榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_DrainageAweme():


    @allure.story('验证引流视频榜遍历商品一级级分类返回的数据是否大于10条')
    @pytest.mark.parametrize('times', base.return_time_message_lastday())
    @allure.title("引流视频榜日期:{times}")
    def test_rank_promotionAweme_big_type(self, get_token, get_host, times):
        para = f'day_type={times[0]}&order=play_inc&day={times[1]}&big_category=&first_category=&second_category=&order_by=desc&page=1&size=50'
        response = base().return_request(method="get", path=PathMessage.rank_DrainageAweme, data=para, tokens=get_token,hosts=get_host, )
        # print(response)
        assert len(response["response_body"]["data"]["list"]) > 0
        # aweme_id_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_id')
        # print(aweme_id_list)