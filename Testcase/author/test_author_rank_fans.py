# -*- coding: utf-8 -*-
# @Time    : 2021/12/13
# @Author  : chenxubin
# @File    : test_author_rank_fans.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('涨粉达人榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Author_Rank_Fans():

    @allure.story('验证涨粉达人榜日榜、周榜、月榜遍历商品大类返回的数据是否大于20条')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('product_type', base.return_star_category(os.getenv("host"), 1))
    @allure.title("涨粉达人榜日期:{times},类目：{product_type}")
    def test_author_rank_product_type(self, get_token, get_host, times, product_type):
        para = "star_category={}&day_type={}&day={}&page=1&size=50&is_commerce=0&province=".format(
            product_type[0],times[0], times[1] )
        responce = base().return_request(method="get", path=PathMessage.author_rank_fans, data=para, tokens=get_token,
                                         hosts=get_host, )
        assert len(responce["response_body"]["data"]["list"]) > 20



    @allure.story('验证涨粉达人榜日榜、周榜、月榜带货达人筛选条件验证')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('is_commerce',[0,1])
    @allure.title("涨粉达人榜日期:{times},带货达人状态：is_commerce")
    def test_author_rank_is_commerce(self, get_token,get_host,times,is_commerce):
        para = "star_category=&day_type={}&day={}&page=1&size=50&is_commerce={}&province=".format(times[0], times[1],is_commerce)
        responce = base().return_request(method="get", path=PathMessage.author_rank_fans, data=para, tokens=get_token,
                                         hosts=get_host, )

        assert responce["status_code"] == 200

        for i in responce["response_body"]["data"]["list"]:

            if is_commerce==1:
                assert i["commerce"] == 1


    # @allure.story('验证涨粉达人榜日榜、周榜、月榜地区筛选条件验证')
    # @pytest.mark.parametrize('times', base.return_time_message())
    # @pytest.mark.parametrize('city',base.return_city(os.getenv("host"),2))
    # @allure.title("涨粉达人榜日期:{times},筛选的地区：city")
    # def test_author_rank_is_city(self, get_token,get_host,times,city):
    #     para = "star_category=&day_type={}&day={}&page=1&size=50&is_commerce=0&province={}&city={}".format(times[0], times[1],city[0],city[1])
    #     responce = base().return_request(method="get", path=PathMessage.author_rank_fans, data=para, tokens=get_token,
    #                                      hosts=get_host, )
    #
    #     assert responce["status_code"] == 200
    #     assert responce["data"]["list"] > 0
        # for i in responce["response_body"]["data"]["list"]:
        #     assert i["province"] in city[0]
        #     assert i["city"] in city[1]




























