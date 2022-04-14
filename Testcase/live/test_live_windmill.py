# -*- coding: utf-8 -*-
# @Time    : 2021/12/22
# @Author  : linchenzhen
# @File    : test_live_windmill.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath


@allure.feature('直播风车榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_Windmill():


    @allure.description("""验证直播风车榜日榜、周榜、月榜遍历达人分类是否有返回数据""")
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("直播风车榜日期：{times}，按达人分类{star_category}")
    def test_windmill_category(self,get_token,get_host,star_category,times):
        para=f"category={star_category}&day_type={times[0]}&date={times[1]}&page=1&size=50"
        response = base().return_request(method="get", path=PathMessage.rank_windmill, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) >= 0



