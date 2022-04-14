# -*- coding: utf-8 -*-
# @Time    : 2021/12/8
# @Author  : linchenzhen
# @File    : test_rank_yesterdayHotRank.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
from Config.Consts import commission_rate,platform
import os,jsonpath


@allure.feature('抖音热推榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_YesterdayHotRank():

    @allure.description("""验证抖音热推榜单是否按昨日达人带货排序""")
    @allure.title("抖音热推榜按昨日达人带货排序")
    def test_yesterdayHotRank_author_number(self,get_token,get_host):
        para=f"big_category=&first_category=&second_category=&page=1&size=50&commission_rate="
        response = base().return_request(method="get", path=PathMessage.rank_yesterdayHotRank, data=para,tokens=get_token,hosts=get_host, )
        author_number_list = jsonpath.jsonpath(response["response_body"], '$.data[*].author_number')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]) > 0
        assert all(author_number_list[i] >= author_number_list[i+1] for i in range(len(author_number_list)-1))


    @allure.description("""验证抖音热推榜日榜、周榜、月榜遍历商品一级分类返回的数据是否大于20条""")
    @pytest.mark.parametrize('times',base.return_time_message())
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("抖音热推榜日期:{times[1]},类目：{product_type}")
    def test_yesterdayHotRank_big_category(self,get_token,get_host,times,product_type):
        para=f"big_category={product_type[0]}&first_category=&second_category=&platform={platform[0]}&page=1&size=50&commission_rate=&date={times[1]}&day_type={times[0]}"
        response = base().return_request(method="get", path=PathMessage.rank_yesterdayHotRank, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]) > 20

    # @allure.description("""验证抖音热推榜日榜、周榜、月榜遍历商品二级分类是否有返回数据""")
    # @pytest.mark.parametrize('times',base.return_time_message())
    # @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2))
    # @allure.title("抖音热推榜日期:{times[1]},类目：{product_type}")
    # def test_yesterdayHotRank_first_category(self,get_token,get_host,times,product_type):
    #     para=f"big_category={product_type[0]}&first_category={product_type[1]}&second_category=&platform={platform[0]}&page=1&size=50&commission_rate=&date={times[1]}&day_type={times[0]}"
    #     response = base().return_request(method="get", path=PathMessage.rank_yesterdayHotRank, data=para,tokens=get_token,hosts=get_host, )
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]) > 0

    # @allure.description("""验证抖音热推榜日榜、周榜、月榜，按佣金比例筛选""")
    # @pytest.mark.parametrize('commission_rate',commission_rate)
    # @pytest.mark.parametrize('times',base.return_time_message())
    # @allure.title("抖音热推榜日期:{times[1]},佣金比例：{commission_rate}")
    # def test_yesterdayHotRank_commission_rate(self,get_token,get_host,times,commission_rate):
    #     para=f"big_category=&first_category=&second_category=&platform={platform[0]}&page=1&size=50&commission_rate={commission_rate}&date={times[1]}&day_type={times[0]}"
    #     response = base().return_request(method="get", path=PathMessage.rank_yesterdayHotRank, data=para,tokens=get_token,hosts=get_host, )
    #     commission_list=jsonpath.jsonpath(response["response_body"],'$.data[*].rate')
    #     commission_rate=int(commission_rate.replace('-',''))
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]) > 0
        # assert all(value >= commission_rate for value in commission_list)