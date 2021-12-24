# -*- coding: utf-8 -*-
# @Time    : 2021/12/13
# @Author  : chenxubin
# @File    : test_authorRank_bangNew_A.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('行业达人榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_AuthorRank_BangNew_A():

    @allure.story('验证行业达人榜日榜、周榜、月榜遍历商品大类返回的数据是否大于20条')
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("行业达人榜日期:{times},类目：{star_type}")
    @pytest.mark.parametrize('star_type', base.return_star_category(os.getenv("host"), 1))
    def test_authorRank_bangNew_A_product_type(self, get_token, get_host, star_type, times):
        data = {"bang_type": "A", "star_category": star_type, "day_type": times[0], "day": times[1], "page": 1}
        responce = base().return_request(method="post", path=PathMessage.authorRank_bangNew, data=data,
                                             tokens=get_token, hosts=get_host, )
        assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["rank_result"]) > 20

