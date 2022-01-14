# -*- coding: utf-8 -*-
# @Time    : 2021/12/21
# @Author  : linchenzhen
# @File    : test_rank_product.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath


@allure.feature('直播商品榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_Product():

    sort=['sales','sales_volume','price','commission_rate','room_num']

    @allure.description("""验证直播商品榜单日榜、周榜、月榜是否会排序规则排序""")
    @pytest.mark.parametrize('sort', sort)
    @pytest.mark.parametrize('times',base.return_time_message())
    @allure.title("直播商品榜日期：{times}，按{sort}排序")
    def test_product_orderby(self,get_token,get_host,sort,times):
        para=f"keyword=&day_type={times[0]}&platform=&day={times[1]}&big_category=&first_category=&second_category=&sort={sort}&page=1&size=50"
        response = base().return_request(method="get", path=PathMessage.rank_product, data=para,tokens=get_token,hosts=get_host, )
        if sort=='room_num':
            sort_list=jsonpath.jsonpath(response["response_body"], f'$.data.list[*].live_show_count')
        else:
            sort_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].{sort}')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]['list']) > 0
        assert all(sort_list[i] >= sort_list[i+1] for i in range(len(sort_list)-1))

    @allure.description("""验证直播商品榜日榜、周榜、月榜遍历商品一级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("直播商品榜日期：{times}，按商品一级分类：{product_type}")
    def test_product_big_category(self,get_token,get_host,product_type,times):
        para=f"keyword=&day_type={times[0]}&platform=&day={times[1]}&big_category={product_type[0]}&first_category=&second_category=&sort={self.sort[0]}&page=1&size=50"
        response = base().return_request(method="get", path=PathMessage.rank_product, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    # @allure.description("""验证直播商品榜日榜、周榜、月榜遍历商品二级分类是否有返回数据""")
    # @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2))
    # @pytest.mark.parametrize('times', base.return_time_message())
    # @allure.title("直播商品榜日期：{times}，商品二级分类：{product_type}")
    # def test_product_first_category(self,get_token,get_host,product_type,times):
    #     para=f"keyword=&day_type={times[0]}&platform=&day={times[1]}&big_category={product_type[0]}&first_category={product_type[1]}&second_category=&sort={self.sort[0]}&page=1&size=50"
    #     response = base().return_request(method="get", path=PathMessage.rank_product, data=para,tokens=get_token,hosts=get_host, )
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]["list"]) > 0



