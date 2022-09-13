# -*- coding: utf-8 -*-
# @Time    : 2021/12/27
# @Author  : linchenzhen
# @File    : test_aweme_product_search.py
import json
import re

import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath


@allure.feature('带货视频库')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Aweme_Product_Search():

    sort=['product_volume','product_amount','digg_count']
    time=['24h','3d','7d','15d','30d','90d']
    digg=['0-10000','10000-50000','50000-100000','100000-500000','500000-1000000','1000000-2000000','2000000-']
    durations=['0-15','15-30','60-','30-60']
    hour_ranges=['0-8','8-14','14-18','18-24']
    product_volume=['0-500','500-1000','1000-2000','2000-5000','5000-10000','10000-']
    product_amount=['0-5000','5000-10000','10000-20000','20000-50000','50000-100000','100000-']

    @allure.description("""验证带货视频库是否会排序规则排序""")
    @pytest.mark.parametrize('sort', sort)
    @allure.title("带货视频库按{sort}排序")
    def test_aweme_product_search_sort(self,get_token,get_host,sort):
        para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges=&star_category=&star_sub_category=&big_category=&first_category=&second_category=&keyword=&digg=&follower_count=&durations=&product_amount=&product_volume=&sort={sort}&time={self.time[0]}&size=50&rank_type=1&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        sort_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].aweme_info.{sort}')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]['list']) > 0
        assert all(sort_list[i] >= sort_list[i+1] for i in range(len(sort_list)-1))

    @allure.description("""验证带货视频库遍历达人一级分类是否有返回数据""")
    @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),1))
    @allure.title("带货视频库按达人一级分类：{star_category}")
    def test_aweme_product_search_star_category(self,get_token,get_host,star_category):
        para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges=&star_category={star_category[0]}&star_sub_category=&big_category=&first_category=&second_category=&keyword=&digg=&follower_count=&durations=&product_amount=&product_volume=&sort={self.sort[0]}&time={self.time[0]}&size=50&rank_type=1&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    # @allure.description("""验证带货视频库遍历达人二级分类是否有返回数据""")
    # @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),2))
    # @allure.title("带货视频库达人二级分类：{star_category}")
    # def test_aweme_product_search_star_sub_category(self,get_token,get_host,star_category):
    #     para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges=&star_category={star_category[0]}&star_sub_category={star_category[1]}&big_category=&first_category=&second_category=&keyword=&digg=&follower_count=&durations=&product_amount=&product_volume=&sort={self.sort[0]}&time={self.time[0]}&size=50&rank_type=1&filter_delete=1&order_by=desc"
    #     response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证带货视频库遍历商品一级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("带货视频库按商品一级分类：{product_type}")
    def test_aweme_product_big_category(self,get_token,get_host,product_type):
        para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges=&star_category=&star_sub_category=&big_category={product_type[0]}&first_category=&second_category=&keyword=&digg=&follower_count=&durations=&product_amount=&product_volume=&sort={self.sort[0]}&time={self.time[0]}&size=50&rank_type=1&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        # print(response)
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 10
        # aweme_id_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.aweme_id')
        # for id in aweme_id_list:
        #     diagnose_para = {"aweme_id": id, "time_section": 1, "diagnose_type": "big"}
        #     diagnose_response = base().return_request(method="get", path=PathMessage.aweme_diagnose, data=diagnose_para, tokens=get_token, hosts=get_host)
            # print(diagnose_response)
            # assert json.dumps(product_type) in diagnose_response["response_body"]['data']['label']

    # @allure.description("""验证带货视频库遍历商品二级分类是否有返回数据""")
    # @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2))
    # @allure.title("带货视频库商品二级分类：{product_type}")
    # def test_aweme_product_search_first_category(self,get_token,get_host,product_type):
    #     para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges=&star_category=&star_sub_category=&big_category={product_type[0]}&first_category={product_type[1]}&second_category=&keyword=&digg=&follower_count=&durations=&product_amount=&product_volume=&sort={self.sort[0]}&time={self.time[0]}&size=50&rank_type=1&filter_delete=1&order_by=desc"
    #     response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证带货视频库按视频点赞数筛选，数据是否正确""")
    @pytest.mark.parametrize('digg', digg)
    @allure.title("带货视频库按视频点赞数{digg}筛选")
    def test_aweme_product_search_digg(self,get_token,get_host,digg):
        para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges=&star_category=&star_sub_category=&big_category=&first_category=&second_category=&keyword=&digg={digg}&follower_count=&durations=&product_amount=&product_volume=&sort={self.sort[0]}&time={self.time[0]}&size=50&rank_type=1&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        digg_count_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.digg_count')
        digg_count=digg.split("-")
        assert all(float(digg_count[0])<=float(value) for value in digg_count_list if len(digg_count[0])>0)
        assert all(float(value)<=float(digg_count[1]) for value in digg_count_list if len(digg_count[1])>0)

    @allure.description("""验证带货视频库按视频时长筛选，数据是否正确""")
    @pytest.mark.parametrize('durations', durations)
    @allure.title("带货视频库按视频时长{durations}筛选")
    def test_aweme_product_search_durations(self,get_token,get_host,durations):
        para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges=&star_category=&star_sub_category=&big_category=&first_category=&second_category=&keyword=&digg=&follower_count=&durations={durations}&product_amount=&product_volume=&sort={self.sort[0]}&time={self.time[0]}&size=50&rank_type=1&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        durations_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.duration')
        duration=durations.split("-")
        assert all(float(duration[0])<=float(value) for value in durations_list if len(duration[0])>0)
        assert all(float(value)<=float(duration[1]) for value in durations_list if len(duration[1])>0)

    @allure.description("""验证带货视频库按发布时间筛选，数据是否正确""")
    @pytest.mark.parametrize('time', time)
    @allure.title("带货视频库按发布时间{time}筛选")
    def test_aweme_product_search_time(self,get_token,get_host,time):
        para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges=&star_category=&star_sub_category=&big_category=&first_category=&second_category=&keyword=&digg=&follower_count=&durations=&product_amount=&product_volume=&sort={self.sort[0]}&time={time}&size=50&rank_type=1&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证带货视频库按发布时段筛选，数据是否正确""")
    @pytest.mark.parametrize('hour_ranges', hour_ranges)
    @allure.title("带货视频库按发布时段{hour_ranges}筛选")
    def test_aweme_product_search_hour_ranges(self,get_token,get_host,hour_ranges):
        para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges={hour_ranges}&star_category=&star_sub_category=&big_category=&first_category=&second_category=&keyword=&digg=&follower_count=&durations=&product_amount=&product_volume=&sort={self.sort[0]}&time={self.time[0]}&size=50&rank_type=1&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        durations_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.aweme_create_time')
        new_durations_list=[re.findall(r"\s(.+?):",value) for value in durations_list]
        hour_range=hour_ranges.split("-")
        assert all(float(hour_range[0])<=float(value[0])<=float(hour_range[1]) for value in new_durations_list )

    @allure.description("""验证带货视频库按商品预估销量筛选，数据是否正确""")
    @pytest.mark.parametrize('product_volume', product_volume)
    @allure.title("带货视频库按商品预估销量{product_volume}筛选")
    def test_aweme_product_search_digg(self,get_token,get_host,product_volume):
        para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges=&star_category=&star_sub_category=&big_category=&first_category=&second_category=&keyword=&digg=&follower_count=&durations=&product_amount=&product_volume={product_volume}&sort={self.sort[0]}&time={self.time[0]}&size=50&rank_type=1&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        product_volume_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.product_volume')
        product_volumes=product_volume.split("-")
        assert all(float(product_volumes[0])<=float(value) for value in product_volume_list if len(product_volumes[0])>0)
        assert all(float(value)<=float(product_volumes[1]) for value in product_volume_list if len(product_volumes[1])>0)

    @allure.description("""验证带货视频库按商品预估销售额筛选，数据是否正确""")
    @pytest.mark.parametrize('product_amount', product_amount)
    @allure.title("带货视频库按商品预估销售额{product_amount}筛选")
    def test_aweme_product_search_digg(self,get_token,get_host,product_amount):
        para=f"search_type=aweme&goods_relatived=1&page=1&hour_ranges=&star_category=&star_sub_category=&big_category=&first_category=&second_category=&keyword=&digg=&follower_count=&durations=&product_amount={product_amount}&product_volume=&sort={self.sort[0]}&time={self.time[0]}&size=50&rank_type=1&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        product_amount_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.product_amount')
        product_amounts=product_amount.split("-")
        assert all(float(product_amounts[0])<=float(value) for value in product_amount_list if len(product_amounts[0])>0)
        assert all(float(value)<=float(product_amounts[1]) for value in product_amount_list if len(product_amounts[1])>0)


    @allure.description("""验证视频库按图文筛选，数据是否正确""")
    @allure.title("视频库按图文筛选")
    def test_aweme_search_aweme_graph_type(self,get_token,get_host):
        para=f"gender_type=-1&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&aweme_graph_type=1&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        # print(response)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 10