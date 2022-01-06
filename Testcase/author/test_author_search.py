# -*- coding: utf-8 -*-
# @Time    : 2021/1/4
# @Author  : chenxubin
# @File    : test_author_search.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os, jsonpath


@allure.feature('达人库库')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Author_Search():

    sort = ['follower_count', 'inc_follower', 'aweme_digg_medium', 'aweme_digg_follower_ration','live_pv_medium','live_average_interact_30','live_average_amount_30']
    order_by = ['desc', 'asc']

    @allure.story('验证达人库排序是否正确')
    @pytest.mark.parametrize('sort', sort)
    @pytest.mark.parametrize('order_by', order_by)
    @allure.title("排序为{sort}，按{order_by}")
    def test_author_search_sort(self, get_token, get_host, sort, order_by):
        para = "page=1&reputation_level=-1&star_category=&star_sub_category=&goods_cat=&keyword=&gender=-1&age=&fans_gender=-1&fans_age=&follower_count=&product_platform=&province=&fans_province=&contact=0&is_commerce=0&is_live=0&is_sell_live=0&is_star_author=0&is_low_fans_high_gmv=0&is_brand_self_author=0&is_shop_author=0&verification_type=0&sort={}&order_by={}&size=52&similar_author_id=".format(sort,order_by)
        response = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)
        if sort == 'inc_follower':
            sort = "follower_incr"

        sort_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].{sort}')
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]['list']) > 0
        if order_by == "desc":
            assert all(float(sort_list[i]) >= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))
        else:
            assert all(float(sort_list[i]) <= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))



    @allure.story('验证达人库遍历达人和商品一级分类是否有返回数据')
    @pytest.mark.parametrize('star_category', base.return_star_category(os.getenv("host"), 1))
    @pytest.mark.parametrize('product_category', base.return_product_types(os.getenv("host"), 1))
    @allure.title("达人一级分类：{star_category},商品一级分类：{product_category}")
    def test_author_search_star_product_category(self, get_token, get_host, star_category, product_category):
        para = "page=1&reputation_level=-1&star_category={}&star_sub_category=&goods_cat={}&keyword=&gender=-1&age=&fans_gender=-1&fans_age=&follower_count=&product_platform=&province=&fans_province=&contact=0&is_commerce=0&is_live=0&is_sell_live=0&is_star_author=0&is_low_fans_high_gmv=0&is_brand_self_author=0&is_shop_author=0&verification_type=0&sort=inc_follower&order_by=desc&size=52&similar_author_id=".format(star_category[0],product_category[0])
        response = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                 tokens=get_token, hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) >= 0