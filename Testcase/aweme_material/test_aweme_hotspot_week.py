# -*- coding: utf-8 -*-
# @Time    : 2022/1/7
# @Author  : linchenzhen
# @File    : test_aweme_hotspot_week.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os
@allure.feature('七日探测榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Aweme_Hotspot_week():


    @allure.description("""验证七日探测榜是否有返回数据""")
    @allure.title("七日探测榜查看数据")
    def test_hotspot_week_list_date(self,get_token,get_host):
        para="size=50&page=1"
        response = base().return_request(method="get", path=PathMessage.aweme_hotspot_week, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0



