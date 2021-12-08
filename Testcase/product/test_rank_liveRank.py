# -*- coding: utf-8 -*-
# @Time    : 2021/12/8
# @Author  : linchenzhen
# @File    : test_rank_liveRank.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
from Config.Consts import commission_rate
import os,jsonpath


@allure.feature('实时销量榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_LiveRank():

    @allure.description("""验证实时销量榜遍历商品一级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("实时销量榜商品一级分类：{product_type}")
    def test_liveRank_big_category(self,get_token,get_host,product_type):
        para=f"big_category={product_type[0]}&first_category=&second_category=&page=1&size=50&commission_rate="
        response = base().return_request(method="get", path=PathMessage.rank_liveRank, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]) > 0

    @allure.description("""验证实时销量榜遍历商品二级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2))
    @allure.title("实时销量榜商品二级分类：{product_type}")
    def test_liveRank_first_category(self,get_token,get_host,product_type):
        para=f"big_category={product_type[0]}&first_category={product_type[1]}&second_category=&page=1&size=50&commission_rate="
        response = base().return_request(method="get", path=PathMessage.rank_liveRank, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]) > 0

    @allure.description("""验证实时销量榜日榜、周榜、月榜，按佣金比例筛选""")
    @pytest.mark.parametrize('commission_rate',commission_rate)
    @allure.title("实时销量榜佣金比例：{commission_rate}")
    def test_liveRank_commission_rate(self,get_token,get_host,commission_rate):
        para=f"big_category=&first_category=&second_category=&page=1&size=50&commission_rate={commission_rate}"
        response = base().return_request(method="get", path=PathMessage.rank_liveRank, data=para,tokens=get_token,hosts=get_host, )
        commission_list=jsonpath.jsonpath(response["response_body"],'$.data[*].rate')
        commission_rate=int(commission_rate.replace('-',''))
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]) > 0
        assert all(value >= commission_rate for value in commission_list)
