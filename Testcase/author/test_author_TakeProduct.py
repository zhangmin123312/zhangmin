# -*- coding: utf-8 -*-
# @Time    : 2022/08/15
# @Author  : youjiangyong
# @File    : test_author_TakeProduct.py
import allure
import pytest
import time
from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('达人带货榜')
@pytest.mark.flaky(reruns=2, reruns_delay=1)
class TestCase_author_TakeProduct():

    @allure.feature('验证达人带货榜日榜、周榜、月榜遍历商品大类返回的数据是否大于20条')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('product_type', base.return_product_types(os.getenv("host"), 1))
    @allure.title("达人带货榜时间类型：{times},带货分类类目：{product_type}")
    def test_author_TakeProduct(self, get_token, get_host, times, product_type):
        para = f"day_type={times[0]}&day={times[1]}&big_category={product_type[0]}&first_category=&second_category=&sort=sales_volume&page=1&size=50&verification_type=&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=0"
        responce = base().return_request(method="get", path=PathMessage.author_TakeProduct, data=para, tokens=get_token, hosts=get_host)
        time.sleep(0.1)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 20

    @allure.feature('验证达人带货榜新秀筛选是否有数据')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('New_author', ['1'])
    @allure.title("达人带货榜时间类型：{times},达人类型：[New_author]")
    def test_author_TakeProduct_New_author(self, get_token, get_host, times, New_author):
        para = f"day_type={times[0]}&day={times[1]}&big_category=&first_category=&second_category=&sort=sales_volume&page=1&size=50&verification_type=&is_brand_self_author=0&is_shop_author=0&dark_horse={New_author}&first_rank=0&is_bomb=0"
        responce = base().return_request(method="get", path=PathMessage.author_TakeProduct, data=para, tokens=get_token, hosts=get_host)
        time.sleep(0.1)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 0

    @allure.feature('验证达人带货榜首次上榜筛选是否有数据')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('first_rank', ['1'])
    @allure.title("达人带货榜时间类型：{times},达人类型：[first_rank]")
    def test_author_TakeProduct_first_rank(self, get_token, get_host, times, first_rank):
        para = f"day_type={times[0]}&day={times[1]}&big_category=&first_category=&second_category=&sort=sales_volume&page=1&size=50&verification_type=&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank={first_rank}&is_bomb=0"
        responce = base().return_request(method="get", path=PathMessage.author_TakeProduct, data=para, tokens=get_token,
                                         hosts=get_host)
        time.sleep(0.1)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 0

    @allure.story('验证达人带货榜黑马达人筛选是否正确')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('is_bomb', ['1'])
    def test_author_TakeProduct_is_bomb(self, get_token, get_host, times, is_bomb):
        para = f"day_type={times[0]}&day={times[1]}&big_category=&first_category=&second_category=&sort=sales_volume&page=1&size=50&verification_type=&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb={is_bomb}"
        responce = base().return_request(method="get", path=PathMessage.author_TakeProduct, data=para,
                                         tokens=get_token, hosts=get_host)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 0

    @allure.feature('验证达人带货榜蓝V筛选是否有数据')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('verification_type', ['2'])
    @allure.title("达人带货榜时间类型：{times},达人类型：[verification_type]")
    def test_author_TakeProduct_verification_type_2(self, get_token, get_host, times, verification_type):
        para = f"day_type={times[0]}&day={times[1]}&big_category=&first_category=&second_category=&sort=sales_volume&page=1&size=50&verification_type={verification_type}&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=0"
        responce = base().return_request(method="get", path=PathMessage.author_TakeProduct, data=para, tokens=get_token,
                                         hosts=get_host)
        time.sleep(0.1)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 0


    @allure.feature('验证达人带货榜品牌自播筛选是否有数据')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('brand_self_author', ['1'])
    @allure.title("达人带货榜时间类型：{times},达人类型：[brand_self_author]")
    def test_author_TakeProduct_brand_self_author(self, get_token, get_host, times, brand_self_author):
        para = f"day_type={times[0]}&day={times[1]}&big_category=&first_category=&second_category=&sort=sales_volume&page=1&size=50&verification_type=&is_brand_self_author={brand_self_author}&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=0"
        responce = base().return_request(method="get", path=PathMessage.author_TakeProduct, data=para, tokens=get_token,
                                         hosts=get_host)
        time.sleep(0.1)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 0

    @allure.feature('验证达人带货榜店播筛选是否有数据')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('shop_author', ['1'])
    @allure.title("达人带货榜时间类型：{times},达人类型：[shop_author]")
    def test_author_TakeProduct_shop_author(self, get_token, get_host, times, shop_author):
        para = f"day_type={times[0]}&day={times[1]}&big_category=&first_category=&second_category=&sort=sales_volume&page=1&size=50&verification_type=&is_brand_self_author=&is_shop_author={shop_author}&dark_horse=0&first_rank=0&is_bomb=0"
        responce = base().return_request(method="get", path=PathMessage.author_TakeProduct, data=para, tokens=get_token,
                                         hosts=get_host)
        time.sleep(0.1)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 0

