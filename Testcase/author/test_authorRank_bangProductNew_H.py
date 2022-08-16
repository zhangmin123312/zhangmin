# -*- coding: utf-8 -*-
# @Time    : 2022/08/09
# @Author  : youjiangyong
# @File    : test_authorRank_bangNew_H.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('黑马达人榜-带货达人')
@pytest.mark.flaky(reruns=1, reruns_delay=1)
class TestCase_AuthorRank_BangNew_H():

    @allure.story('验证黑马达人榜-带货达人日榜、周榜、月榜遍历大类返回的数据是否大于20条')
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("黑马达人榜-带货达人日期:{times},类目：{star_type}")
    @pytest.mark.parametrize('star_type', base.return_star_category(os.getenv("host"), 1))
    def test_authorRank_bangNew_G_star_type(self, get_token, get_host, star_type, times):
        data = {"bang_type": "H", "star_category": star_type, "day_type": times[0], "day": times[1], "page": 1}
        responce = base().return_request(method="post", path=PathMessage.authorRank_bangProductNew, data=data,
                                             tokens=get_token, hosts=get_host, )
        print(responce)
        assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["rank_result"]) > 0