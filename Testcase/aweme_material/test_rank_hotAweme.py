# -*- coding: utf-8 -*-
# @Time    : 2021/12/23
# @Author  : zhangmin
# @File    : test_rank_hotAweme.py
from time import sleep

import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('热门视频榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_HotAweme():


    @allure.story('验证热门视频日、周、月榜遍历达人大类返回的数据是否大于0条')
    @pytest.mark.parametrize('times',base.return_time_message())
    @pytest.mark.parametrize('star_type',base.return_star_category(os.getenv("host"),1))
    @allure.title("热门视频榜日期:{times},类目：{star_type}")
    def test_rank_hotAweme_big_type(self,get_token,get_host,times,star_type):
        para = "day_type={}&day={}&star_category={}&order_by=synthesize&page=1&size=50".format(times[0],times[1],star_type[0])
        responce = base().return_request(method="get", path=PathMessage.rank_hotAweme, data=para,tokens=get_token,hosts=get_host, )
        assert len(responce["response_body"]["data"]) > 0


    @allure.story('验证热门视频小时榜遍历达人大类返回的数据是否大于0条')
    @pytest.mark.parametrize('times', ["0-6","6-12","12-18","18-24"])
    @pytest.mark.parametrize('star_type', base.return_star_category(os.getenv("host"), 1))
    @allure.title("热门视频榜日期:{times},类目：{star_type}")
    def test_rank_hotAweme_hour_big_type(self, get_token, get_host, times, star_type):
        para = "day_type=hour&day={}&star_category={}&order_by=synthesize&page=1&size=50".format(times,star_type[0])
        responce = base().return_request(method="get", path=PathMessage.rank_hotAweme, data=para, tokens=get_token,
                                         hosts=get_host, )

        assert len(responce["response_body"]["data"]) > 0



    @allure.story('验证热门视频日、周、月榜排序验证')
    @pytest.mark.parametrize('times',base.return_time_message())
    @allure.title("热门视频日期:{times},排序：点赞排序")
    def test_rank_hotAweme_sort(self,get_token,get_host,times):
        para = "day_type={}&day={}&star_category=&order_by=digg&page=1&size=50".format(times[0],times[1])
        responce = base().return_request(method="get", path=PathMessage.rank_hotAweme, data=para,tokens=get_token,hosts=get_host, )["response_body"]["data"]
        total_digg = float("inf")

        for i in responce:
            assert i["digg_count"] <= total_digg
            total_digg = i["digg_count"]


    @allure.story('验证热门视频小时榜排序验证')
    @pytest.mark.parametrize('times', ["0-6","6-12","12-18","18-24"])
    @allure.title("热门视频日期:{times},排序：点赞排序")
    def test_rank_hotAweme_hour_sort(self, get_token, get_host, times):
        para = "day_type=hour&day={}&star_category=&order_by=digg&page=1&size=50".format(times)
        responce = base().return_request(method="get", path=PathMessage.rank_hotAweme, data=para, tokens=get_token,
                                         hosts=get_host, )["response_body"]["data"]

        total_digg = float("inf")

        for i in responce:
            assert i["digg_count"] <= total_digg
            total_digg = i["digg_count"]


