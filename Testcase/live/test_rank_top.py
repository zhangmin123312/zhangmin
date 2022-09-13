# -*- coding: utf-8 -*-
# @Time    : 2021/12/16
# @Author  : linchenzhen
# @File    : test_rank_top.py
#榜单名称修改为官方人气榜
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath

@allure.feature('官方人气榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_Top():

    @allure.description("""验证官方人气榜否有数据""")
    @allure.title("官方人气榜否有数据")
    def test_top_timestamp(self,get_token,get_host):
        para = f"star_category=&page=1&size=50"
        response = base().return_request(method="get", path=PathMessage.rank_top, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证官方人气榜遍历达人一级分类是否有返回数据""")
    @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),1))
    @allure.title("官方人气榜达人一级分类：{star_category}")
    def test_top_star_category(self,get_token,get_host,star_category):
        para = f"star_category={star_category[0]}&page=1&size=50"
        response = base().return_request(method="get", path=PathMessage.rank_top, data=para,tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0
        assert all(response["response_body"]["data"]["list"][i]["star_category"]==star_category[0] for i in range(len(response["response_body"]["data"]["list"])))
