# -*- coding: utf-8 -*-
# @Time    : 2021/12/27
# @Author  : chenxubin
# @File    : test_authorRank_bangNew_D.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('地区达人榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_AuthorRank_BangNew_D():

    @allure.story('验证地区达人榜日榜、周榜、月榜遍历商品大类返回的数据是否大于20条')
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("地区达人榜日期:{times},地区类目：{city}")
    @pytest.mark.parametrize('city', base.return_city(os.getenv("host"), 1))
    def test_authorRank_bangNew_D_city_type(self, get_token, get_host, city, times):
        data = {"bang_type":"D","province":city,"city":"","day_type":times[0],"day":times[1],"page":1}
        responce = base().return_request(method="post", path=PathMessage.authorRank_bangNew, data=data,
                                             tokens=get_token, hosts=get_host, )
        assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["rank_result"]) > 20

