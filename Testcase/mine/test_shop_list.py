# -*- coding: utf-8 -*-
# @Time    : 2022/1/20
# @Author  : linchenzhen
# @File    : test_shop_list.py

import allure
import jsonpath
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,json

@allure.feature('小店收藏')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Shop_List():

    @pytest.mark.run(order=1)
    @allure.description("""验证添加小店，小店收藏列表是否正确显示""")
    @allure.title("添加小店，收藏列表正确显示")
    def test_shop_list_list(self,get_token,get_host,add_shop_list):
        shop_id,category_big=add_shop_list
        para=f"page=1&sub_user_id=&category=&page_size=50"
        response = base().return_request(method="get", path=PathMessage.shop_detail_fav_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        shop_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].shop_id')
        assert shop_id in shop_id_list

    @pytest.mark.run(order=1)
    @allure.description("""验证按小店分类筛选，小店收藏列表是否正确显示""")
    @allure.title("搜索小店分类，收藏列表正确显示")
    def test_shop_list_star_category(self,get_token,get_host,add_shop_list):
        shop_id,category_big=add_shop_list
        para=f"page=1&sub_user_id=&category={category_big}&page_size=50"
        response = base().return_request(method="get", path=PathMessage.shop_detail_fav_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        shop_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].shop_id')
        assert shop_id in shop_id_list

    @pytest.mark.run(order=1)
    @allure.description("""验证子账号小店收藏列表是否正确显示""")
    @allure.title("子账号小店收藏列表正确显示")
    def test_shop_list_subAccount(self,get_token,get_host,common_init):
        para=f"page=1&keyword=&sub_user_id={common_init}&label=&page_size=50"
        response = base().return_request(method="get", path=PathMessage.shop_detail_fav_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0


    @pytest.mark.run(order=2)
    @allure.description("""验证取消小店收藏，小店收藏列表是否正确显示""")
    @allure.title("取消收藏小店，收藏列表正确显示")
    def test_shop_list_fav(self,get_token,get_host,add_shop_list):
        shop_id,category_big=add_shop_list
        # 取消小店收藏
        fav_para = {"shop_id": shop_id}
        fav_response = base().return_request(method="post", path=PathMessage.shop_detail_fav_cancel, data=json.dumps(fav_para),
                                             tokens=get_token, hosts=get_host)
        para=f"page=1&keyword=&sub_user_id=0&label=&page_size=50"
        response = base().return_request(method="get", path=PathMessage.shop_detail_fav_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        shop_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].shop_id')
        assert shop_id not in shop_id_list
