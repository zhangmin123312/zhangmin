# -*- coding: utf-8 -*-
# @Time    : 2022/6/13
# @Author  : zhangmin
# @File    : test_rank_authorLiveSelect_potential.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath
@allure.feature('三日潜力榜')
#@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_potential():
    @allure.story('验证三日潜力榜数据是否大于0条')
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("类目：{product_type}")
    def test_rank_potential_big_type(self,get_token,get_host,product_type):
        para = "rank_type=3&page=1&size=50&sort=rank_volume&order_by=&big_category={}&first_category=&is_new_product=0&min_price=&max_price=".format(product_type[0])
        responce = base().return_request(method="get", path=PathMessage.authorLiveSelect_potential, data=para,tokens=get_token,hosts=get_host)
        # print(para)
        # print(responce)
        assert len(responce["response_body"]["data"]['list']) > 0


    @allure.story('验证三日潜力榜价格，关联达人，昨日销量，总销量排序是否正确')
    @pytest.mark.parametrize('sort', ["author_count","rank_volume",'total_volume'])
    @allure.title("三日潜力榜:排序类型：{sort}")
    def test_rank_potential_sort(self, get_token, get_host, sort):

        print(sort)
        para = "rank_type=3&page=1&size=50&sort={}&order_by=desc&big_category=&first_category=&is_new_product=0&min_price=&max_price=".format(
            sort)
        responce = base().return_request(method="get", path=PathMessage.authorLiveSelect_potential, data=para, tokens=get_token,
                              hosts=get_host, )["response_body"]["data"]["list"]

        # total_price = float("inf")
        total_author_count = float("inf")
        total_rank_volume =float("inf")
        total_total_volume = float("inf")
        #页面使用min_price和max_price字段,
        # if sort == "min_price":
        #     for i in responce:
        #         assert i["min_price"] <= total_price
        #         total_price = i["min_price"]


        if sort == "author_count":
            for i in responce:
                assert i["author_count"] <= total_author_count
                total_author_count = i["author_count"]
        elif sort == "rank_volume":
            for i in responce:
                assert i["rank_volume"] <= total_rank_volume
                total_rank_volume = i["rank_volume"]
        elif sort == "total_volume":
            for i in responce:
                assert i["total_volume"] <= total_total_volume
                total_total_volume = i["total_volume"]
        else:
            print("排序传参有误")
            raise False
