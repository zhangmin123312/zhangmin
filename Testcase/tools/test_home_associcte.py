# -*- coding: utf-8 -*-
# @Time    : 2022/8/12
# @Author  : zhangmin
# @File    : test_home_associcte.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
from Testcase.tools import conftest
import datetime
import os
@allure.feature('直播商品一键采集')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_home_associcte():
    @allure.description("""验证昨日带货达人库top10达人的直播商品是否正确""")
    @allure.title("搜索抖音号，监控列表正确显示")
    @pytest.mark.parametrize('get_author',conftest.get_author(os.getenv("host")))
    def test_home_associcte_author(self,get_token,get_host,get_author):
        para='author_id={}&is_last_seven_days=false&page=1&size=50&sort_by=live_volume_30&order_by=desc'.format(get_author)
        # print(para)
        responce = base().return_request(method="get", path=PathMessage.test_home_associcte, data=para,
                                         tokens=get_token, hosts=get_host)
        assert len(responce["response_body"]["data"]["list"]) > 1
        # print(responce)
