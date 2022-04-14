# -*- coding: utf-8 -*-
# @Time    : 2021/12/7
# @Author  : linchenzhen
# @File    : test_rank_yesterdaySaleRank.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
from Config.Consts import commission_rate,platform
import os,jsonpath


@allure.feature('抖音销量榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_YesterdaySaleRank():

    @allure.description("""验证抖音销量榜单日榜、周榜是否按昨日/周销量排序""")
    @pytest.mark.parametrize('times', base.return_time_message()[:2])
    @allure.title("抖音销量榜日期:{times[1]}，按昨日/周销量排序")
    def test_yesterdaySaleRank_day_order_count(self,get_token,get_host,times):
        para=f"big_category=&first_category=&second_category=&platform={platform[0]}&page=1&size=50&commission_rate=&date={times[1]}&day_type={times[0]}"
        response = base().return_request(method="get", path=PathMessage.rank_yesterdaySaleRank, data=para,tokens=get_token,hosts=get_host, )
        day_order_count_list = jsonpath.jsonpath(response["response_body"], '$.data[*].day_order_count')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]) > 0
        assert all(day_order_count_list[i] >= day_order_count_list[i+1] for i in range(len(day_order_count_list)-1))

    @allure.description("""验证抖音销量榜日榜、周榜、月榜遍历商品一级分类返回的数据是否大于20条""")
    @pytest.mark.parametrize('times',base.return_time_message())
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("抖音销量榜日期:{times[1]},类目：{product_type}")
    def test_yesterdaySaleRank_big_category(self,get_token,get_host,times,product_type):
        para=f"big_category={product_type[0]}&first_category=&second_category=&platform={platform[0]}&page=1&size=50&commission_rate=&date={times[1]}&day_type={times[0]}"
        response = base().return_request(method="get", path=PathMessage.rank_yesterdaySaleRank, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]) > 20

    # @allure.description("""验证抖音销量榜日榜、周榜、月榜遍历商品二级分类是否有返回数据""")
    # @pytest.mark.parametrize('times',base.return_time_message())
    # @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2))
    # @allure.title("抖音销量榜日期:{times[1]},类目：{product_type}")
    # def test_yesterdaySaleRank_first_category(self,get_token,get_host,times,product_type):
    #     para=f"big_category={product_type[0]}&first_category={product_type[1]}&second_category=&platform={platform[0]}&page=1&size=50&commission_rate=&date={times[1]}&day_type={times[0]}"
    #     response = base().return_request(method="get", path=PathMessage.rank_yesterdaySaleRank, data=para,tokens=get_token,hosts=get_host, )
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]) > 0
    #
    # @allure.description("""验证抖音销量榜日榜、周榜、月榜，按佣金比例筛选""")
    # @pytest.mark.parametrize('commission_rate',commission_rate)
    # @pytest.mark.parametrize('times',base.return_time_message())
    # @allure.title("抖音销量榜日期:{times[1]},佣金比例：{commission_rate}")
    # def test_yesterdaySaleRank_commission_rate(self,get_token,get_host,times,commission_rate):
    #     para=f"big_category=&first_category=&second_category=&platform={platform[0]}&page=1&size=50&commission_rate={commission_rate}&date={times[1]}&day_type={times[0]}"
    #     response = base().return_request(method="get", path=PathMessage.rank_yesterdaySaleRank, data=para,tokens=get_token,hosts=get_host, )
    #     commission_list=jsonpath.jsonpath(response["response_body"],'$.data[*].rate')
    #     commission_rate=int(commission_rate.replace('-',''))
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]) > 0
        # assert all(value >= commission_rate for value in commission_list)

    # @allure.description("""验证抖音销量榜日榜、周榜、月榜，按商品来源筛选""")
    # @pytest.mark.parametrize('platform',platform)
    # @pytest.mark.parametrize('times',base.return_time_message())
    # @allure.title("抖音销量榜日期:{times[1]},商品来源：{platform}")
    # def test_yesterdaySaleRank_platform(self,get_token,get_host,times,platform):
    #     para=f"big_category=&first_category=&second_category=&platform={platform}&page=1&size=50&commission_rate=&date={times[1]}&day_type={times[0]}"
    #     response = base().return_request(method="get", path=PathMessage.rank_yesterdaySaleRank, data=para,tokens=get_token,hosts=get_host, )
    #     platform_list = jsonpath.jsonpath(response["response_body"], '$.data[*].platform')
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]) > 0
    #     assert all(value == platform for value in platform_list)







