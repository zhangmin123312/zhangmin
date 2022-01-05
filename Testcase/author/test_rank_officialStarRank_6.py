# -*- coding: utf-8 -*-
# @Time    : 2021/12/19
# @Author  : chenzilin
# @File    : test_rank_officialStarRank_6.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage

@allure.feature('视频传播指数榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_OfficialStarRank_6():

    @allure.description("""验证视频达人指数榜返回的数据是否大于20条""")
    def test_rank_officialStarRank_6(self,get_token,get_host):
        para = "hot_list_type=6&page=1&size=50"
        responce = base().return_request(method="get", path=PathMessage.rank_officialStarRank, tokens=get_token,hosts=get_host, data=para)
        assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["list"]) > 20