# -*- coding: utf-8 -*-
# @Time    : 2022/1/11
# @Author  : linchenzhen
# @File    : test_productMine.py

import allure
import jsonpath
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,json

@allure.feature('商品收藏')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_ProductMine():

    @pytest.mark.run(order=1)
    @allure.description("""验证添加商品，商品收藏列表是否正确显示""")
    @allure.title("添加商品，收藏列表正确显示")
    def test_productMine_list(self,get_token,get_host,add_productMine):
        promotion_id,title,key=add_productMine
        para=f"page=1&keyword=&sub_user_id=0&label=&page_size=50"
        response = base().return_request(method="get", path=PathMessage.productMine_listsV2, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        promotion_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].promotion_id')
        assert promotion_id in promotion_id_list

    @pytest.mark.run(order=1)
    @allure.description("""验证搜索商品，商品收藏列表是否正确显示""")
    @allure.title("搜索商品昵称，收藏列表正确显示")
    def test_productMine_keyword(self,get_token,get_host,add_productMine):
        promotion_id,title,key=add_productMine
        para=f"page=1&keyword={title}&sub_user_id=0&label=&page_size=50"
        response = base().return_request(method="get", path=PathMessage.productMine_listsV2, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        promotion_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].promotion_id')
        assert promotion_id in promotion_id_list

    @pytest.mark.run(order=1)
    @allure.description("""验证按商品分类筛选，商品收藏列表是否正确显示""")
    @allure.title("搜索商品分类，收藏列表正确显示")
    def test_productMine_star_category(self,get_token,get_host,add_productMine):
        promotion_id,title,key=add_productMine
        para=f"page=1&keyword=&sub_user_id=0&label={key}&page_size=50"
        response = base().return_request(method="get", path=PathMessage.productMine_listsV2, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @pytest.mark.run(order=1)
    @allure.description("""验证子账号商品收藏列表是否正确显示""")
    @allure.title("子账号商品收藏列表正确显示")
    def test_productMine_subAccount(self,get_token,get_host,common_init):
        para=f"page=1&keyword=&sub_user_id={common_init}&label=&page_size=50"
        response = base().return_request(method="get", path=PathMessage.productMine_listsV2, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0


    @pytest.mark.run(order=2)
    @allure.description("""验证取消商品收藏，商品收藏列表是否正确显示""")
    @allure.title("取消收藏商品，收藏列表正确显示")
    def test_productMine_fav(self,get_token,get_host,add_productMine):
        promotion_id,title,key=add_productMine
        # 取消商品收藏
        fav_para = {"promotion_id": promotion_id}
        fav_response = base().return_request(method="post", path=PathMessage.product_fav, data=json.dumps(fav_para),
                                             tokens=get_token, hosts=get_host)
        para=f"page=1&keyword=&sub_user_id=0&label=&page_size=50"
        response = base().return_request(method="get", path=PathMessage.productMine_listsV2, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        promotion_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].promotion_id')
        assert promotion_id not in promotion_id_list
