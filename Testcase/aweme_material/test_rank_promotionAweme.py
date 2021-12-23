# -*- coding: utf-8 -*-
# @Time    : 2021/12/7
# @Author  : zhangmin
# @File    : test_rank_promotionAweme.py
from time import sleep

import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('带货视频榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_PromotionAweme():

    # @allure.story('验证带货视频榜遍历商品二级分类返回的数据是否有数据')
    # @pytest.mark.parametrize('times',base.return_time_message())
    # @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2))
    # @allure.title("带货视频日期:{times},类目：{product_type}")
    # def test_rank_promotionAweme_first_type(self,get_token,get_host,times,product_type):
    #     para = "day_type={}&day={}&big_category={}&first_category={}&second_category=&order_by=volume&page=1&size=50".format(times[0],times[1],product_type[0],product_type[1])
    #     responce = base().return_request(method="get", path=PathMessage.rank_productAweme, data=para,tokens=get_token,hosts=get_host, )
    #     # print(para)
    #     # print(responce)
    #     assert len(responce["response_body"]["data"]) > 0


    @allure.story('验证带货视频榜遍历商品一级级分类返回的数据是否大于0条')
    @pytest.mark.parametrize('times',base.return_time_message())
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("带货视频日期:{times},类目：{product_type}")
    def test_rank_promotionAweme_big_type(self,get_token,get_host,times,product_type):
        para = "day_type={}&day={}&big_category={}&first_category=&second_category=&order_by=volume&page=1&size=50".format(times[0],times[1],product_type[0])
        responce = base().return_request(method="get", path=PathMessage.rank_productAweme, data=para,tokens=get_token,hosts=get_host, )
        assert len(responce["response_body"]["data"]) > 0



    @allure.story('验证带货视频榜按销量和销售额，点赞数降序排序是否正确')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('sort', ["volume","amount","digg"])
    @allure.title("带货视频榜:{times},排序类型：{sort}")
    def test_rank_promotionAweme_sort(self, get_token, get_host, times, sort):

        print(sort)
        para = "day_type={}&day={}&big_category=&first_category=&second_category=&order_by={}&page=1&size=50".format(
            times[0], times[1], sort)
        responce = base().return_request(method="get", path=PathMessage.rank_productAweme, data=para, tokens=get_token,
                              hosts=get_host, )["response_body"]["data"]

        total_amount = float("inf")
        total_volume = float("inf")
        total_digg =float("inf")

        if sort == "volume":
            for i in responce:
                assert i["volume"] <= total_volume
                total_volume = i["volume"]


        elif sort == "amount":
            for i in responce:
                assert i["amount"] <= total_amount
                total_amount = i["amount"]
        elif sort == "digg":
            for i in responce:
                assert i["digg_count"] <= total_digg
                total_digg = i["digg_count"]
        else:
            print("排序传参有误")
            raise False

