# -*- coding: utf-8 -*-
# @Time    : 2022/1/7
# @Author  : linchenzhen
# @File    : test_music_search.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,jsonpath
@allure.feature('音乐库')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_music_search():

    orderby=['user_incr','user_count']
    incr_type=['yesterday','3d','7d']

    @allure.description("""验证音乐库遍历昨天、近3天、近7天是否有返回数据""")
    @pytest.mark.parametrize('incr_type', incr_type)
    @allure.title("音乐库按时间{incr_type}查看")
    def test_music_search_incr_type(self,get_token,get_host,incr_type):
        para=f"keyword=&page=1&size=50&orderby={self.orderby[0]}&incr_type={incr_type}&order=desc"
        response = base().return_request(method="get", path=PathMessage.music_search, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证音乐库是否会排序规则排序""")
    @pytest.mark.parametrize('orderby', orderby)
    @allure.title("音乐库按{orderby}排序")
    def test_music_search_orderby(self,get_token,get_host,orderby):
        para=f"keyword=&page=1&size=50&orderby={orderby}&incr_type={self.incr_type[0]}&order=desc"
        response = base().return_request(method="get", path=PathMessage.music_search, data=para,tokens=get_token,hosts=get_host)
        orderby_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].{orderby}')
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]['list']) > 0
        assert all(orderby_list[i] >= orderby_list[i+1] for i in range(len(orderby_list)-1))

    @allure.description("""验证音乐库搜索结果是否正确""")
    @allure.title("音乐库搜索结果是否正确")
    def test_music_search_keyword(self,get_token,get_host):
        title_para=f"keyword=&page=1&size=50&orderby={self.orderby[0]}&incr_type={self.incr_type[0]}&order=desc"
        title_response = base().return_request(method="get", path=PathMessage.music_search, data=title_para, tokens=get_token,hosts=get_host)
        keyword=title_response["response_body"]["data"]["list"][0]['title']

        para = f"keyword={keyword}&page=1&size=50&orderby={self.orderby[0]}&incr_type={self.incr_type[0]}&order=desc"
        response = base().return_request(method="get", path=PathMessage.music_search, data=para, tokens=get_token,
                                         hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        # 验证搜索结果包含关键字的每一个字
        title_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].title')
        for i in keyword:
            assert all(i in value for value in title_list)