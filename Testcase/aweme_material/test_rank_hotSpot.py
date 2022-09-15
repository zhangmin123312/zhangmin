# -*- coding: utf-8 -*-
# @Time    : 2022/9/14
# @Author  : youjiangyong
# @File    : test_hotSpotRank.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath,datetime,random

def get_timestamp():
    timestamp = datetime.datetime.now().replace(hour=9, minute=0, second=0, microsecond=0).timestamp()
    timestamp = int(timestamp)
    return timestamp
print(get_timestamp())

@allure.feature('官方热点榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_hotSpotRank():
    timestamp = get_timestamp()
    @allure.story('验证官方热点榜遍历商品一级级分类返回的数据是否大于10条')
    @pytest.mark.parametrize('times', base.return_time_message_nowday())
    @pytest.mark.parametrize('timestamp', [timestamp])
    @allure.title("官方热点榜查看榜点：{timestamp}")
    def test_rank_promotionAweme_big_type(self, get_token, get_host, timestamp, times):
        para = f'day_type={times[0]}&date={times[1]}&page=1&size=50&type=1&timestamp={timestamp}'
        response = base().return_request(method="get", path=PathMessage.rank_hotSpotRank, data=para, tokens=get_token,hosts=get_host, )
        # print(response)
        assert len(response["response_body"]["data"]["list"]) > 10
        # aweme_id_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_id')
        # print(aweme_id_list)