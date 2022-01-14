# -*- coding: utf-8 -*-
# @Time    : 2021/12/20
# @Author  : linchenzhen
# @File    : test_rank_sales.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath


@allure.feature('达人带货榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_Sales():

    sort=['sales_volume','sales','average_price']

    @allure.description("""验证达人带货榜单日榜、周榜、月榜是否会排序规则排序""")
    @pytest.mark.parametrize('sort', sort)
    @pytest.mark.parametrize('times',base.return_time_message())
    @allure.title("达人带货榜日期：{times}，按{sort}排序")
    def test_sales_orderby(self,get_token,get_host,sort,times):
        para=f"day_type={times[0]}&day={times[1]}&big_category=&first_category=&second_category=&sort={sort}&page=1&size=50&verification_type=&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=0"
        response = base().return_request(method="get", path=PathMessage.rank_sales, data=para,tokens=get_token,hosts=get_host, )
        sort_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].{sort}')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]['list']) > 0
        assert all(sort_list[i] >= sort_list[i+1] for i in range(len(sort_list)-1))

    @allure.description("""验证达人带货榜日榜、周榜、月榜遍历商品一级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1,'sales'))
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("达人带货榜日期：{times}，按商品一级分类：{product_type}")
    def test_sales_big_category(self,get_token,get_host,product_type,times):
        para=f"day_type={times[0]}&day={times[1]}&big_category={product_type[0]}&first_category=&second_category=&sort={self.sort[0]}&page=1&size=50&verification_type=&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=0"
        response = base().return_request(method="get", path=PathMessage.rank_sales, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    # @allure.description("""验证达人带货榜日榜、周榜、月榜遍历商品二级分类是否有返回数据""")
    # @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2,'sales'))
    # @pytest.mark.parametrize('times', base.return_time_message())
    # @allure.title("达人带货榜日期：{times}，商品二级分类：{product_type}")
    # def test_sales_first_category(self,get_token,get_host,product_type,times):
    #     para=f"day_type={times[0]}&day={times[1]}&big_category={product_type[0]}&first_category={product_type[1]}&second_category=&sort={self.sort[0]}&page=1&size=50&verification_type=&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=0"
    #     response = base().return_request(method="get", path=PathMessage.rank_sales, data=para,tokens=get_token,hosts=get_host, )
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证达人带货榜日榜、周榜、月榜按低粉爆款达人筛选，数据是否正确""")
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("达人带货榜日期：{times}，按低粉爆款达人筛选")
    def test_sales_low_fans(self,get_token,get_host,times):
        para=f"day_type={times[0]}&day={times[1]}&big_category=&first_category=&second_category=&sort={self.sort[0]}&page=1&size=50&verification_type=&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=1"
        response = base().return_request(method="get", path=PathMessage.rank_sales, data=para,tokens=get_token,hosts=get_host, )
        follower_count_list = jsonpath.jsonpath(response["response_body"], '$.data.[list][*].follower_count')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0
        # 验证粉丝数小于10万
        assert all(value < 1000000 for value in follower_count_list)
        # 验证日均销售额10万以上
        date_list = base.return_Filter_date(1, 7)
        for info in response["response_body"]["data"]["list"]:
            day_avg_amount_para = f"author_id={info['author_id']}&start_date={date_list[3][0]}&end_date={date_list[3][1]}"
            day_avg_amount_response = base().return_request(method="get", path=PathMessage.author_liveAnalysisV2, data=day_avg_amount_para,
                                             tokens=get_token, hosts=get_host, )
            day_avg_amount=day_avg_amount_response["response_body"]["data"]["summary"]["day_avg_amount"]
            assert day_avg_amount>100000

    @allure.description("""验证达人带货榜日榜、周榜、月榜只看蓝V达人数据是否正确""")
    @pytest.mark.parametrize('times', base.return_time_message())
    @allure.title("达人带货榜日期：{times}只看蓝V达人")
    def test_sales_verification_type(self,get_token,get_host,times):
        para=f"day_type={times[0]}&day={times[1]}&big_category=&first_category=&second_category=&sort={self.sort[0]}&page=1&size=50&verification_type=2&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=0"
        response = base().return_request(method="get", path=PathMessage.rank_sales, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        verification_type_list = jsonpath.jsonpath(response["response_body"], '$.data.[list][*].verification_type')
        assert all(value == 2 for value in verification_type_list)


