# -*- coding: utf-8 -*-
# @Time    : 2021/12/17
# @Author  : linchenzhen
# @File    : test_live_warm.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath,json


@allure.feature('预热视频分析')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Live_Warm():

    sort=['warm_aweme_digg_sum']
    order_by=['desc','asc']

    @allure.description("""验证预热视频分析不同时间榜单是否会按总点赞增量升降排序""")
    @pytest.mark.parametrize('sort', sort)
    @pytest.mark.parametrize('order_by', order_by)
    @pytest.mark.parametrize('live_time',base.return_Filter_date(0,7))
    @allure.title("预热视频分析时间区间：{live_time},按总点赞增量{order_by}排序")
    def test_warm_sort(self,get_token,get_host,sort,order_by,live_time):
        para={"search_type":0,"keyword_type":0,"page":1,"star_category":"","star_sub_category":"","multi_category":[],"keyword":"","sort":sort,"order_by":order_by,"size":50,"live_begin_time":live_time[0],"live_end_time":live_time[1]}
        response = base().return_request(method="post", path=PathMessage.live_warm, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        sort_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].{sort}')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]['list']) > 0
        if order_by=="desc":
            assert all(sort_list[i] >= sort_list[i+1] for i in range(len(sort_list)-1))
        else:
            assert all(sort_list[i] <= sort_list[i + 1] for i in range(len(sort_list) - 1))

    @allure.description("""验证预热视频分析近7天遍历商品一级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("预热视频近7天分析商品一级分类：{product_type}")
    def test_warm_big_category(self,get_token,get_host,product_type,get_Nearly_7_date):
        para={"search_type":0,"keyword_type":0,"page":1,"star_category":"","star_sub_category":"","multi_category":product_type,"keyword":"","sort":self.sort[0],"order_by":self.order_by[0],"size":50,"live_begin_time":get_Nearly_7_date[0],"live_end_time":get_Nearly_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_warm, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证预热视频分析近7天遍历商品二级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2))
    @allure.title("预热视频分析近7天商品二级分类：{product_type}")
    def test_warm_first_category(self,get_token,get_host,product_type,get_Nearly_7_date):
        para={"search_type":0,"keyword_type":0,"page":1,"star_category":"","star_sub_category":"","multi_category":[product_type],"keyword":"","sort":self.sort[0],"order_by":self.order_by[0],"size":50,"live_begin_time":get_Nearly_7_date[0],"live_end_time":get_Nearly_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_warm, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证预热视频分析近7天遍历达人一级分类是否有返回数据""")
    @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),1))
    @allure.title("预热视频分析近7天达人一级分类：{star_category}")
    def test_warm_star_category(self,get_token,get_host,star_category,get_Nearly_7_date):
        para={"search_type":0,"keyword_type":0,"page":1,"star_category":star_category[0],"star_sub_category":"","multi_category":[],"keyword":"","sort":self.sort[0],"order_by":self.order_by[0],"size":50,"live_begin_time":get_Nearly_7_date[0],"live_end_time":get_Nearly_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_warm, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证预热视频分析近7天遍历达人二级分类是否有返回数据""")
    @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),2))
    @allure.title("预热视频分析近7天达人二级分类：{star_category}")
    def test_warm_star_sub_category(self,get_token,get_host,star_category,get_Nearly_7_date):
        para={"search_type":0,"keyword_type":0,"page":1,"star_category":star_category[0],"star_sub_category":star_category[1],"multi_category":[],"keyword":"","sort":self.sort[0],"order_by":self.order_by[0],"size":50,"live_begin_time":get_Nearly_7_date[0],"live_end_time":get_Nearly_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_warm, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0