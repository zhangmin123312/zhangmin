# -*- coding: utf-8 -*-
# @Time    : 2021/12/6
# @Author  : chenxubin
# @File    : test_brand_rank.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('热门品牌榜')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Brand_Rank():

    @allure.story('验证热门品牌榜日榜、周榜、月榜遍历商品大类返回的数据是否大于20条')
    @pytest.mark.parametrize('times',base.return_time_message())
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("热门品牌榜日期:{times},类目：{product_type}")
    def test_brand_rank_product_type(self,get_token,get_host,times,product_type):
        para = "day_type={}&day={}&big_category={}&first_category=&second_category=&sort=amount&order_by=desc&page=1&size=50".format(times[0],times[1],product_type[0])
        responce = base().return_request(method="get", path=PathMessage.brand_rank, data=para,tokens=get_token,hosts=get_host, )
        assert len(responce["response_body"]["data"]["list"]) > 20




    # @allure.story('验证商品品牌榜日榜、周榜、月榜遍历商品一级分类返回的数据是否大于0条')
    # @pytest.mark.parametrize('times',base.return_time_message())
    # @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2))
    # @allure.title("商品品牌榜日期:{times},类目：{product_type}")
    # def test_brand_rank_product_type(self,get_token,get_host,times,product_type):
    #     para = "day_type={}&day={}&big_category={}&first_category={}&second_category=&sort=amount&order_by=desc&page=1&size=50".format(times[0],times[1],product_type[0],product_type[1])
    #     print(para)
    #     responce = base().return_request(method="get", path=PathMessage.brand_rank, data=para,tokens=get_token,hosts=get_host, )
    #
    #     if product_type[1] != "其他":
    #         assert len(responce["response_body"]["data"]["list"]) > 0




    @allure.story('验证热门品牌榜日榜、周榜、月榜按销量和销售降序排序是否正确')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('sort', ["volume","amount"])
    @allure.title("热门品牌榜日期:{times},排序类型：{sort}")
    def test_brand_rank_sort(self, get_token, get_host, times, sort):
        print(sort)
        para = "day_type={}&day={}&big_category=&first_category=&second_category=&sort={}&order_by=desc&page=1&size=50".format(times[0], times[1], sort)
        responce = base().return_request(method="get", path=PathMessage.brand_rank, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
        amount = float("inf")
        day_order_count = float("inf")
        if sort == "volume":
            for i in responce:
                assert i["day_order_count"] <= day_order_count
                day_order_count = i["day_order_count"]


        elif sort == "amount":
            for i in responce:
                assert i["amount"] <= amount
                amount = i["amount"]

        else:
            print("排序传参有误")
            raise False



    @allure.story('验证热门品牌榜带货方式筛选')
    @pytest.mark.parametrize('sale_way',[0,1,2])
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("热门品牌榜{times}带货方式筛选:{sale_way}")
    def test_brand_rank_sale_way(self,get_token,get_host,times,sale_way):
        para="day_type={}&day={}&big_category=&first_category=&second_category=&sort=amount&is_quick_position=0&brand_code=&order_by=desc&page=1&size=50&sale_way={}&channel_brand=0&channel_shop=0&channel_author=0".format(times[0],times[1],sale_way)
        responce = base().return_request(method="get", path=PathMessage.brand_rank, data=para,tokens=get_token,hosts=get_host)
        assert len(responce["response_body"]["data"]["list"]) > 10

    @allure.story('验证热门品牌榜带品牌自播筛选')
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("热门品牌榜{times}品牌自播筛选")
    def test_brand_rank_channel_brand(self,get_token,get_host,times):
        para="day_type={}&day={}&big_category=&first_category=&second_category=&sort=amount&is_quick_position=0&brand_code=&order_by=desc&page=1&size=50&sale_way=0&channel_brand=1&channel_shop=0&channel_author=0".format(times[0],times[1])
        responce = base().return_request(method="get", path=PathMessage.brand_rank, data=para,tokens=get_token,hosts=get_host)
        assert len(responce["response_body"]["data"]["list"]) > 10


    @allure.story('验证热门品牌榜带小店播筛选')
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("热门品牌榜{times}品牌自播筛选")
    def test_brand_rank_channel_shop(self,get_token,get_host,times):
        para="day_type={}&day={}&big_category=&first_category=&second_category=&sort=amount&is_quick_position=0&brand_code=&order_by=desc&page=1&size=50&sale_way=0&channel_brand=0&channel_shop=1&channel_author=0".format(times[0],times[1])
        responce = base().return_request(method="get", path=PathMessage.brand_rank, data=para,tokens=get_token,hosts=get_host)
        assert len(responce["response_body"]["data"]["list"]) > 10

    @allure.story('验证热门品牌榜带达人播筛选')
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("热门品牌榜{times}品牌自播筛选")
    def test_brand_rank_channel_author(self,get_token,get_host,times):
        para="day_type={}&day={}&big_category=&first_category=&second_category=&sort=amount&is_quick_position=0&brand_code=&order_by=desc&page=1&size=50&sale_way=0&channel_brand=0&channel_shop=0&channel_author=1".format(times[0],times[1])
        responce = base().return_request(method="get", path=PathMessage.brand_rank, data=para,tokens=get_token,hosts=get_host)
        assert len(responce["response_body"]["data"]["list"]) > 10



