# -*- coding: utf-8 -*-
# @Time    : 2022/08/09
# @Author  : youjiangyong
# @File    : test_brand_self_author.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('品牌自播榜')
@pytest.mark.flaky(reruns=2, reruns_delay=1)
class TestCase_brand_self_author():

    @allure.story('验证品牌自播榜日榜、周榜、月榜遍历一级分类是否有数据')
    @pytest.mark.parametrize('times', base.return_time_message())
    @pytest.mark.parametrize('product_type', base.return_product_types(os.getenv("host"), 1))
    @allure.title("品牌自播榜日期:{times},带货分类：{product_type}")
    def test_brand_self_author_1(self, get_token, get_host, times, product_type):
        para = f"day_type={times[0]}&day={times[1]}&big_category={product_type[0]}&first_category=&second_category=&sort=sales_volume&page=1&size=50&is_quick_position=0&author_id=&order_by=desc&verification_type=2&is_brand_self_author=1&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=0"
        responce = base().return_request(method="get", path=PathMessage.brand_self_author, data=para,
                                         tokens=get_token, hosts=get_host, )
        # print(responce)
        assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["list"]) > 0


