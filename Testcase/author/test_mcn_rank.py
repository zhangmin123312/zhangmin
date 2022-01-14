# -*- coding: utf-8 -*-
# @Time    : 2022/01/13
# @Author  : chenxubin
# @File    : test_mcn_rank.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import jsonpath


@allure.feature('mcn榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Mcn_Rank():

    @allure.story('验证mcn榜日榜、周榜、月榜是否返回的数据是否大于10条')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('sort', ["author_count", "fans_increment","fans_count","mcn_amount"])
    @allure.title("涨粉达人榜日期:{times},降序排序为：{sort}")
    def test_mcn_rank_date_sort(self, get_token, get_host, times,sort):
        para = "day_type={}&date={}&sort_type={}&page=1&size=50".format(times[0], times[1],sort)
        responce = base().return_request(method="get", path=PathMessage.mcn_rank, data=para, tokens=get_token,
                                         hosts=get_host, )
        sort_list = jsonpath.jsonpath(responce["response_body"], f'$.data.list[*].{sort}')
        assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]['list']) > 0
        assert all(float(sort_list[i]) >= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))