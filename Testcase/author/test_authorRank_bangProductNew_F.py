# -*- coding: utf-8 -*-
# @Time    : 2022/08/09
# @Author  : youjiangyong
# @File    : test_authorRank_bangProductNew_F.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os
import time


@allure.feature('地区达人榜-带货达人')
@pytest.mark.flaky(reruns=2, reruns_delay=1)
class TestCase_AuthorRank_BangProductNew_F():

    @allure.story('验证地区达人榜-带货达人日榜、周榜、月榜遍历商品大类是否有数据 ')
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("地区达人榜-带货达人日期:{times},地区类目：{city}")
    @pytest.mark.parametrize('city', base.return_city_4(os.getenv("host"), 2, "河北省"))
    def test_authorRank_bangProductNew_F_city_type(self, get_token, get_host, city, times):
        data = {"bang_type": "F", "province": city, "city": "", "day_type": times[0], "day": times[1], "page": 1}
        responce = base().return_request(method="post", path=PathMessage.authorRank_bangProductNew, data=data,
                                             tokens=get_token, hosts=get_host, )
        time.sleep(0.1)
        # print(responce)
        assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["rank_result"]) > 0

