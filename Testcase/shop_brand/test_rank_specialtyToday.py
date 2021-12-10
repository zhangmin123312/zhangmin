# -*- coding: utf-8 -*-
# @Time    : 2021/12/7
# @Author  : chenxubin
# @File    : test_rank_specialtyToday.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('抖音小店榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_SpecialtyToday():

    @allure.story('验证抖音小店榜日榜、周榜、月榜遍历商品大类返回的数据是否大于20条')
    @pytest.mark.parametrize('times',base.return_time_message())
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("抖音小店榜日期:{times},类目：{product_type}")
    def test_rank_specialtyToday_product_type(self,get_token,get_host,times,product_type):
        para = "day_type={}&day={}&big_category={}&first_category=&second_category=&order_by=amount&page=1&size=50".format(times[0],times[1],product_type[0])
        responce = base().return_request(method="get", path=PathMessage.rank_specialtyToday, data=para,tokens=get_token,hosts=get_host, )
        assert len(responce["response_body"]["data"]) > 20




    @allure.story('验证抖音小店榜日榜、周榜、月榜按销量和销售降序排序是否正确')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('sort', ["volume","amount"])
    @allure.title("抖音小店榜日期:{times},排序类型：{sort}")
    def test_rank_specialtyToday_sort(self, get_token, get_host, times, sort):
        print(sort)
        para = "day_type={}&day={}&big_category=&first_category=&second_category=&order_by={}&page=1&size=50".format(times[0], times[1], sort)
        responce = base().return_request(method="get", path=PathMessage.rank_specialtyToday, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]
        total_amount = float("inf")
        total_volume = float("inf")

        if sort == "volume":
            for i in responce:
                assert i["total_volume"] <= total_volume
                total_volume = i["total_volume"]


        elif sort == "amount":
            for i in responce:
                assert i["total_amount"] <= total_amount
                total_amount = i["total_amount"]

        else:
            print("排序传参有误")
            raise False