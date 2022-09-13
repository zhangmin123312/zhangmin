# -*- coding: utf-8 -*-
# @Time    : 2021/12/15
# @Author  : linchenzhen
# @File    : test_rank_official_daily.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath


@allure.feature('今日带货榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_Official_Daily():

    orderby=['amount','volume','score','user_peak','follower_count']

    @allure.description("""验证今日带货榜单是否会排序规则排序""")
    @pytest.mark.parametrize('orderby', orderby)
    @allure.title("今日带货榜按{orderby}排序")
    def test_official_daily_orderby(self,get_token,get_host,orderby):
        para=f"star_category=&big_category=&first_category=&second_category=&order=desc&orderby={orderby}&page=1&size=50&dark_horse=0&first_on_list=0&is_brand_self=0&low_fans=0"
        response = base().return_request(method="get", path=PathMessage.rank_official_daily, data=para,tokens=get_token,hosts=get_host, )
        orderby_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].{orderby}')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]['list']) > 0
        assert all(orderby_list[i] >= orderby_list[i+1] for i in range(len(orderby_list)-1))

    @allure.description("""验证今日带货榜遍历商品一级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1,'sales'))
    @allure.title("今日带货榜商品一级分类：{product_type}")
    def test_official_daily_big_category(self,get_token,get_host,product_type):
        para=f"star_category=&big_category={product_type[0]}&first_category=&second_category=&order=desc&orderby={self.orderby[0]}&page=1&size=50&dark_horse=0&first_on_list=0&is_brand_self=0&low_fans=0"
        response = base().return_request(method="get", path=PathMessage.rank_official_daily, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]) > 0

    # @allure.description("""验证今日带货榜遍历商品二级分类是否有返回数据""")
    # @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2,'sales'))
    # @allure.title("今日带货榜商品二级分类：{product_type}")
    # def test_official_daily_first_category(self,get_token,get_host,product_type):
    #     para=f"star_category=&big_category={product_type[0]}&first_category={product_type[1]}&second_category=&order=desc&orderby={self.orderby[0]}&page=1&size=50&dark_horse=0&first_on_list=0&is_brand_self=0&low_fans=0"
    #     response = base().return_request(method="get", path=PathMessage.rank_official_daily, data=para,tokens=get_token,hosts=get_host, )
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]) > 0

    @allure.description("""验证今日带货榜遍历达人一级分类是否有返回数据""")
    @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),1))
    @allure.title("今日带货榜达人一级分类：{star_category}")
    def test_official_daily_star_category(self,get_token,get_host,star_category):
        para=f"star_category={star_category[0]}&big_category=&first_category=&second_category=&order=desc&orderby={self.orderby[0]}&page=1&size=50&dark_horse=0&first_on_list=0&is_brand_self=0&low_fans=0"
        response = base().return_request(method="get", path=PathMessage.rank_official_daily, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0


    @allure.description("""验证今日带货榜新秀筛选，数据是否正确""")
    @allure.title("今日带货榜按新秀筛选")
    def test_official_daily_dark_horse(self,get_token,get_host):
        para='star_category=&big_category=&first_category=&second_category=&order=desc&orderby=follower_count&page=1&size=50&dark_horse=1&first_on_list=0&is_brand_self=0&low_fans=0'
        response = base().return_request(method="get", path=PathMessage.rank_official_daily, data=para,tokens=get_token,hosts=get_host, )
        follower_count_list = jsonpath.jsonpath(response["response_body"], '$.data.[list][*].follower_count')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证今日带货榜首次上榜筛选，数据是否正确""")
    @allure.title("今日带货榜按首次上榜筛选")
    def test_official_daily_first_on_list(self,get_token,get_host):
        para='star_category=&big_category=&first_category=&second_category=&order=desc&orderby=follower_count&page=1&size=50&dark_horse=0&first_on_list=1&is_brand_self=0&low_fans=0'
        response = base().return_request(method="get", path=PathMessage.rank_official_daily, data=para,tokens=get_token,hosts=get_host, )
        follower_count_list = jsonpath.jsonpath(response["response_body"], '$.data.[list][*].follower_count')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证今日带货榜品牌自播筛选，数据是否正确""")
    @allure.title("今日带货榜按品牌自播筛选")
    def test_official_daily_is_brand_self(self,get_token,get_host):
        para="star_category=&big_category=&first_category=&second_category=&order=desc&orderby=follower_count&page=1&size=50&dark_horse=0&first_on_list=0&is_brand_self=1&low_fans=0"
        response = base().return_request(method="get", path=PathMessage.rank_official_daily, data=para,tokens=get_token,hosts=get_host, )
        follower_count_list = jsonpath.jsonpath(response["response_body"], '$.data.[list][*].follower_count')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0
