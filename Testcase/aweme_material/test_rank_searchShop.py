# -*- coding: utf-8 -*-
# @Time    : 2022/9/14
# @Author  : youjiangyong
# @File    : test_searchShop.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath,datetime,random



@allure.feature('探店视频榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_searchShop():

    sort = ["digg_cnt", "comment_cnt", "share_cnt"]

    @allure.story('验证探店视频榜遍历商品一级级分类返回的数据是否大于10条')
    @allure.description("""验证探店视频榜查看任意分类""")
    @pytest.mark.parametrize('times', base.return_time_message_1())
    @pytest.mark.parametrize('city', base.return_city_3(os.getenv("host"), "福建省"))
    @pytest.mark.parametrize('sort', sort)
    @allure.title("探店视频榜日期:{times}")
    def test_rank_promotionAweme_big_type(self, get_token, get_host, sort, times, city):
        para = f'rank_type={times[0]}&date={times[1]}&city={city[0]}&sort={sort}&page=1&size=50'
        response = base().return_request(method="get", path=PathMessage.rank_searchShop, data=para, tokens=get_token,hosts=get_host, )
        # print(response)
        assert len(response["response_body"]["data"]["list"]) > 10
        # aweme_id_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_id')
        # print(aweme_id_list)