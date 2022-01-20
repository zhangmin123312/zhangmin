# -*- coding: utf-8 -*-
# @Time    : 2021/12/27
# @Author  : linchenzhen
# @File    : test_aweme_search.py
import json
import re

import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath


@allure.feature('视频库')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Aweme_Search():

    sort=['digg_count','comment_count','share_count']
    time=['24h','6h','12h','3d','7d','15d','30d','90d']
    digg=['0-10000','10000-50000','50000-100000','100000-500000','500000-1000000','1000000-2000000','2000000-']
    durations=['0-15','15-30','60-','30-60']
    hour_ranges=['0-8','8-14','14-18','18-24']
    age_types={'0':'6-17','1':'18-24','2':'25-30','3':'31-35','4':'36-40','5':'>41'}

    @allure.description("""验证视频库是否会排序规则排序""")
    @pytest.mark.parametrize('sort', sort)
    @allure.title("视频库按{sort}排序")
    def test_aweme_search_sort(self,get_token,get_host,sort):
        para=f"gender_type=-1&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort={sort}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        sort_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].aweme_info.{sort}')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]['list']) > 0
        assert all(sort_list[i] >= sort_list[i+1] for i in range(len(sort_list)-1))

    @allure.description("""验证视频库遍历达人一级分类是否有返回数据""")
    @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),1))
    @allure.title("视频库按达人一级分类：{star_category}")
    def test_aweme_search_star_category(self,get_token,get_host,star_category):
        para=f"gender_type=-1&age_types=&province=&page=1&star_category={star_category[0]}&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    # @allure.description("""验证视频库遍历达人二级分类是否有返回数据""")
    # @pytest.mark.parametrize('star_category',base.return_star_category(os.getenv("host"),2))
    # @allure.title("视频库达人二级分类：{star_category}")
    # def test_aweme_search_star_sub_category(self,get_token,get_host,star_category):
    #     para=f"gender_type=-1&age_types=&province=&page=1&star_category={star_category[0]}&star_sub_category={star_category[1]}&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
    #     response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证视频库按视频点赞数筛选，数据是否正确""")
    @pytest.mark.parametrize('digg', digg)
    @allure.title("视频库按视频点赞数{digg}筛选")
    def test_aweme_search_digg(self,get_token,get_host,digg):
        para=f"gender_type=-1&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg={digg}&follower_counts=&durations=&hour_ranges=&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        digg_count_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.digg_count')
        digg_count=digg.split("-")
        assert all(float(digg_count[0])<=float(value) for value in digg_count_list if len(digg_count[0])>0)
        assert all(float(value)<=float(digg_count[1]) for value in digg_count_list if len(digg_count[1])>0)

    @allure.description("""验证视频库按视频时长筛选，数据是否正确""")
    @pytest.mark.parametrize('durations', durations)
    @allure.title("视频库按视频时长{durations}筛选")
    def test_aweme_search_durations(self,get_token,get_host,durations):
        para=f"gender_type=-1&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations={durations}&hour_ranges=&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        durations_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.duration')
        duration=durations.split("-")
        assert all(float(duration[0])<=float(value) for value in durations_list if len(duration[0])>0)
        assert all(float(value)<=float(duration[1]) for value in durations_list if len(duration[1])>0)

    @allure.description("""验证视频库按发布时间筛选，数据是否正确""")
    @pytest.mark.parametrize('time', time)
    @allure.title("视频库按发布时间{time}筛选")
    def test_aweme_search_time(self,get_token,get_host,time):
        para=f"gender_type=-1&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort={self.sort[0]}&time={time}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证视频库按发布时段筛选，数据是否正确""")
    @pytest.mark.parametrize('hour_ranges', hour_ranges)
    @allure.title("视频库按发布时段{hour_ranges}筛选")
    def test_aweme_search_hour_ranges(self,get_token,get_host,hour_ranges):
        para=f"gender_type=-1&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges={hour_ranges}&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        durations_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.aweme_create_time')
        new_durations_list=[re.findall(r"\s(.+?):",value) for value in durations_list]
        hour_range=hour_ranges.split("-")
        assert all(float(hour_range[0])<=float(value[0])<=float(hour_range[1]) for value in new_durations_list )

    @allure.description("""验证视频库按关联商品筛选，数据是否正确""")
    @allure.title("视频库按关联商品筛选")
    def test_aweme_search_goods_relatived(self,get_token,get_host):
        para=f"gender_type=-1&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=1&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        product_info_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].product_info.promotion_id')
        assert all(value for value in product_info_list )

    @allure.description("""验证视频库按低粉爆款筛选，数据是否正确""")
    @allure.title("视频库按低粉爆款筛选")
    def test_aweme_search_fans_hottest(self,get_token,get_host):
        para=f"gender_type=-1&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=1&group_buy_relatived=0&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        follower_count_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].author_info.follower_count')
        assert all(value<10000 for value in follower_count_list )
        digg_count_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.digg_count')
        assert all(value>2000 for value in digg_count_list )

    @allure.description("""验证视频库按观众性别筛选，数据是否正确""")
    @pytest.mark.parametrize('gender_type', [0,1])
    @allure.title("视频库按观众性别{gender_type}筛选")
    def test_aweme_search_gender_type(self,get_token,get_host,gender_type):
        para=f"gender_type={gender_type}&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
        response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        aweme_id_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.aweme_id')
        for id in aweme_id_list:
            personas_para={"aweme_id":id}
            personas_response = base().return_request(method="post", path=PathMessage.aweme_personas, data=json.dumps(personas_para),tokens=get_token, hosts=get_host)
            if gender_type==0:
                assert personas_response["response_body"]['data']['portrait_summary']['gender_portrait']=='男生居多'
            else:
                assert personas_response["response_body"]['data']['portrait_summary']['gender_portrait']=='女生居多'

    # @allure.description("""验证视频库按观众年龄筛选，数据是否正确""")
    # @pytest.mark.parametrize('age_type', age_types.keys())
    # @allure.title("视频库按观众性别{age_type}筛选")
    # def test_aweme_search_age_types(self,get_token,get_host,age_type):
    #     para=f"gender_type=&age_types={age_type}&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
    #     response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]["list"]) > 0
    #     aweme_id_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.aweme_id')
    #     for id in aweme_id_list:
    #         personas_para={"aweme_id":id}
    #         personas_response = base().return_request(method="post", path=PathMessage.aweme_personas, data=json.dumps(personas_para),tokens=get_token, hosts=get_host)
    #         assert self.age_types[age_type] in personas_response["response_body"]['data']['portrait_summary']['age_portrait']

    # @allure.description("""验证视频库按观众地区筛选，数据是否正确""")
    # @pytest.mark.parametrize('province', base.return_city(os.getenv("host"),1))
    # @allure.title("视频库按观众地区{province}筛选")
    # def test_aweme_search_province(self,get_token,get_host,province):
    #     para=f"gender_type=&age_types=&province={province}&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort={self.sort[0]}&time={self.time[0]}&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
    #     response = base().return_request(method="get", path=PathMessage.aweme_search, data=para,tokens=get_token,hosts=get_host, )
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]["list"]) > 0
    #     aweme_id_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].aweme_info.aweme_id')
    #     for id in aweme_id_list:
    #         personas_para={"aweme_id":id}
    #         personas_response = base().return_request(method="post", path=PathMessage.aweme_personas, data=json.dumps(personas_para),tokens=get_token, hosts=get_host)
    #         assert province[:2] in personas_response["response_body"]['data']['portrait_summary']['province_portrait']