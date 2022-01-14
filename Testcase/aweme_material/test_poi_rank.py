# -*- coding: utf-8 -*-
# @Time    : 2022/1/8
# @Author  : linchenzhen
# @File    : test_poi_rank.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath,datetime,random

def get_area():
    data=f"date={datetime.datetime.now().date()}"
    area_response = base().return_request(method="get", path=PathMessage.poi_rank_area, data=data,tokens=os.getenv("token"), hosts=os.getenv("host"))
    area_list = jsonpath.jsonpath(area_response["response_body"], '$.data.area[*].area[*].code')
    return area_list

def get_label(city_code):

    data=f"date={datetime.datetime.now().date()}&city_code={city_code}"
    label_response = base().return_request(method="get", path=PathMessage.poi_rank_label, data=data,tokens=os.getenv("token"), hosts=os.getenv("host"))
    rank_id_category_list = [(x['cat_name'], y) for x in label_response["response_body"]['data'] for y in jsonpath.jsonpath(x, '$.sub_categories[*].ranks[*].rank_id')]

    return rank_id_category_list

@allure.feature('抖音本地生活榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Poi_Rank():


    area_list=get_area()
    # 地区总共有380个左右，每个地区有接近200个榜单，全部都跑体量太大，所以随机抽取部分城市来验证
    # num=random.randint(0,len(area_list)-1)
    num = 5


    @allure.description("""验证抖音本地生活榜查看任意分类""")
    @pytest.mark.parametrize('get_label', get_label(area_list[num]))
    @allure.title("抖音本地生活榜按{get_label}查看")
    def test_poi_rank_get_label(self,get_token,get_host,get_label):
        para=f"rank_id={get_label[1]}&city={self.area_list[self.num]}&category={get_label[0]}&date={datetime.datetime.now().date()}&page=1&size=50"
        response = base().return_request(method="get", path=PathMessage.poi_rank, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0