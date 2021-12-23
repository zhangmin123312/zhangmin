# -*- coding: utf-8 -*-
# @Time    : 2021/12/16
# @Author  : linchenzhen
# @File    : test_rank_official.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath
@allure.feature('带货小时榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Rank_Official():

    orderby=['amount','volume','score','follower_count']

    @allure.description("""验证带货小时榜遍历所有的小时榜点是否有返回数据""")
    @allure.title("带货小时榜查看榜点：{timestamps}")
    def test_official_timestamp(self,get_token,get_host,timestamps):
        para = f"star_category=&product_category=&order=desc&orderby={self.orderby[0]}&timestamp={timestamps}&page=1&size=50"
        response = base().return_request(method="get", path=PathMessage.rank_official, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证带货小时榜单是否会排序规则排序""")
    @pytest.mark.parametrize('orderby', orderby)
    @allure.title("带货小时榜按{orderby}排序")
    def test_official_orderby(self,get_token,get_host,orderby,last_timestamp):
        para = f"star_category=&product_category=&order=desc&orderby={orderby}&timestamp={last_timestamp}&page=1&size=50"
        response = base().return_request(method="get", path=PathMessage.rank_official, data=para,tokens=get_token,hosts=get_host)
        orderby_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].{orderby}')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]['list']) > 0
        assert all(orderby_list[i] >= orderby_list[i+1] for i in range(len(orderby_list)-1))

    @allure.description("""验证带货小时榜遍历商品分类是否有返回数据""")
    @allure.title("带货小时榜商品分类：{product_category}")
    def test_official_product_category(self,get_token,get_host,product_category,last_timestamp):
        para = f"star_category=&product_category={product_category}&order=desc&orderby={self.orderby[0]}&timestamp={last_timestamp}&page=1&size=50"
        response = base().return_request(method="get", path=PathMessage.rank_official, data=para,tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]['list']) > 0

    @allure.description("""验证带货小时榜遍历达人一级分类是否有返回数据""")
    @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),1))
    @allure.title("带货小时榜达人一级分类：{star_category}")
    def test_official_star_category(self,get_token,get_host,star_category,last_timestamp):
        para = f"star_category={star_category[0]}&product_category=&order=desc&orderby={self.orderby[0]}&timestamp={last_timestamp}&page=1&size=50"
        response = base().return_request(method="get", path=PathMessage.rank_official, data=para,tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0
