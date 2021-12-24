# -*- coding: utf-8 -*-
# @Time    : 2021/12/17
# @Author  : linchenzhen
# @File    : test_live_search.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath,json
@allure.feature('直播库')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Live_Search():

    sort=['amount','begin_time','total_user','volume']
    order_by=['desc','asc']
    follower_count=['0-10000','10000-100000','100000-1000000','1000000-5000000','5000000-10000000','10000000-']
    volume=['100-','500-','1000-','2000-','5000-','10000-','20000-','50000-']

    @allure.description("""验证直播库单是否会排序规则排序""")
    @pytest.mark.parametrize('sort', sort)
    @pytest.mark.parametrize('order_by', order_by)
    @allure.title("直播库按{sort}{order_by}排序")
    def test_live_search_sort(self,get_token,get_host,sort,order_by,get_7_date):
        para={"search_type":0,"keyword_type":0,"province":"","page":1,"star_category":"","star_sub_category":"","multi_product_category":[],"keyword":"","follower_count":"","volume":"","sort":sort,"order_by":order_by,"size":50,"is_take_product":0,"has_search_aweme":0,"live_state":-1,"live_begin_time":get_7_date[0],"live_end_time":get_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host)
        sort_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].{sort}')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]['list']) > 0
        if order_by=="desc":
            assert all(float(sort_list[i]) >= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))
        else:
            assert all(float(sort_list[i]) <= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))

    @allure.description("""验证直播库遍历达人一级分类是否有返回数据""")
    @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),1))
    @allure.title("直播库达人一级分类：{star_category}")
    def test_live_search_star_category(self,get_token,get_host,star_category,get_7_date):
        para={"search_type":0,"keyword_type":0,"province":"","page":1,"star_category":star_category[0],"star_sub_category":"","multi_product_category":[],"keyword":"","follower_count":"","volume":"","sort":self.sort[3],"order_by":self.order_by[0],"size":50,"is_take_product":0,"has_search_aweme":0,"live_state":-1,"live_begin_time":get_7_date[0],"live_end_time":get_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证直播库遍历达人二级分类是否有返回数据""")
    @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),2))
    @allure.title("直播库达人二级分类：{star_category}")
    def test_live_search_star_category(self,get_token,get_host,star_category,get_7_date):
        para={"search_type":0,"keyword_type":0,"province":"","page":1,"star_category":star_category[0],"star_sub_category":star_category[1],"multi_product_category":[],"keyword":"","follower_count":"","volume":"","sort":self.sort[3],"order_by":self.order_by[0],"size":50,"is_take_product":0,"has_search_aweme":0,"live_state":-1,"live_begin_time":get_7_date[0],"live_end_time":get_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0
        
    @allure.description("""验证直播库近7天遍历商品一级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("直播库近7天分析商品一级分类：{product_type}")
    def test_live_search_big_category(self,get_token,get_host,product_type,get_7_date):
        para={"search_type":0,"keyword_type":0,"province":"","page":1,"star_category":"","star_sub_category":"","multi_product_category":[product_type],"keyword":"","follower_count":"","volume":"","sort":self.sort[0],"order_by":self.order_by[0],"size":50,"is_take_product":0,"has_search_aweme":0,"live_state":-1,"live_begin_time":get_7_date[0],"live_end_time":get_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证直播库近7天遍历商品二级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2))
    @allure.title("直播库近7天商品二级分类：{product_type}")
    def test_live_search_first_category(self,get_token,get_host,product_type,get_7_date):
        para={"search_type":0,"keyword_type":0,"province":"","page":1,"star_category":"","star_sub_category":"","multi_product_category":[product_type],"keyword":"","follower_count":"","volume":"","sort":self.sort[0],"order_by":self.order_by[0],"size":50,"is_take_product":0,"has_search_aweme":0,"live_state":-1,"live_begin_time":get_7_date[0],"live_end_time":get_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证直播库按日期筛选""")
    @pytest.mark.parametrize('live_time',base.return_Filter_date(1,7))
    @allure.title("直播库按日期{live_time}筛选")
    def test_live_search_time(self,get_token,get_host,live_time):
        para={"search_type":0,"keyword_type":0,"province":"","page":1,"star_category":"","star_sub_category":"","multi_product_category":[],"keyword":"","follower_count":"","volume":"","sort":self.sort[3],"order_by":self.order_by[0],"size":50,"is_take_product":0,"has_search_aweme":0,"live_state":-1,"live_begin_time":live_time[0],"live_end_time":live_time[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证直播库遍历地区是否有返回数据""")
    @pytest.mark.parametrize('province',base.return_city(os.getenv("host"),1))
    @allure.title("直播库达人地区：{province}")
    def test_live_search_province(self,get_token,get_host,province,get_7_date):
        para={"search_type":0,"keyword_type":0,"province":province,"page":1,"star_category":"","star_sub_category":"","multi_product_category":[],"keyword":"","follower_count":"","volume":"","sort":self.sort[0],"order_by":self.order_by[0],"size":50,"is_take_product":0,"has_search_aweme":0,"live_state":-1,"live_begin_time":get_7_date[0],"live_end_time":get_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证直播库遍历地区是否有返回数据""")
    @pytest.mark.parametrize('city',base.return_city(os.getenv("host"),2))
    @allure.title("直播库达人地区：{city}")
    def test_live_search_province(self,get_token,get_host,city,get_7_date):
        para={"search_type":0,"keyword_type":0,"province":city[0],"city":city[1],"page":1,"star_category":"","star_sub_category":"","multi_product_category":[],"keyword":"","follower_count":"","volume":"","sort":self.sort[0],"order_by":self.order_by[0],"size":50,"is_take_product":0,"has_search_aweme":0,"live_state":-1,"live_begin_time":get_7_date[0],"live_end_time":get_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证直播库按粉丝数筛选是否有返回数据""")
    @pytest.mark.parametrize('follower_count',follower_count)
    @allure.title("直播库按粉丝数筛选：{follower_count}")
    def test_live_search_province(self,get_token,get_host,follower_count,get_7_date):
        para={"search_type":0,"keyword_type":0,"province":"","page":1,"star_category":"","star_sub_category":"","multi_product_category":[],"keyword":"","follower_count":follower_count,"volume":"","sort":self.sort[0],"order_by":self.order_by[0],"size":50,"is_take_product":0,"has_search_aweme":0,"live_state":-1,"live_begin_time":get_7_date[0],"live_end_time":get_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0
        # 粉丝数是增量，直播后查询可能溢出，暂不做验证
        # follower_count_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].author.follower_count')
        # follower_count=follower_count.split("-")
        # assert all(float(follower_count[0])<=float(value) for value in follower_count_list if len(follower_count[0])>0)
        # assert all(float(value)<=float(follower_count[1]) for value in follower_count_list if len(follower_count[1])>0)

    @allure.description("""验证直播库按销量筛选是否有返回数据""")
    @pytest.mark.parametrize('volume',volume)
    @allure.title("直播库按销量筛选：{volume}")
    def test_live_search_province(self,get_token,get_host,volume,get_7_date):
        para={"search_type":0,"keyword_type":0,"province":"","page":1,"star_category":"","star_sub_category":"","multi_product_category":[],"keyword":"","follower_count":"","volume":volume,"sort":self.sort[0],"order_by":self.order_by[0],"size":50,"is_take_product":0,"has_search_aweme":0,"live_state":-1,"live_begin_time":get_7_date[0],"live_end_time":get_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0
        volume_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].volume')
        volume = volume.replace("-", '')
        assert all(value > int(volume) for value in volume_list)

    @allure.description("""验证直播库按直播带货筛选是否有返回数据""")
    @allure.title("直播库按直播带货筛选")
    def test_live_search_province(self,get_token,get_host,get_7_date):
        para={"search_type":0,"keyword_type":0,"province":"","page":1,"star_category":"","star_sub_category":"","multi_product_category":[],"keyword":"","follower_count":"","volume":"","sort":self.sort[0],"order_by":self.order_by[0],"size":50,"is_take_product":1,"has_search_aweme":0,"live_state":-1,"live_begin_time":get_7_date[0],"live_end_time":get_7_date[1]}
        response = base().return_request(method="post", path=PathMessage.live_search, data=json.dumps(para),tokens=get_token,hosts=get_host)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0
        product_size_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].product_size')
        assert all(value > 0 for value in product_size_list)