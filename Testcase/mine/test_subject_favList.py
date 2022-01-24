# -*- coding: utf-8 -*-
# @Time    : 2022/1/24
# @Author  : linchenzhen
# @File    : test_subject_favList.py

import allure
import jsonpath
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,json

@allure.feature('话题收藏')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Subject_FavList():

    @pytest.mark.run(order=1)
    @allure.description("""验证添加话题，话题收藏列表是否正确显示""")
    @allure.title("添加话题，收藏列表正确显示")
    def test_subject_favList_list(self,get_token,get_host,add_subject_favList):
        subject_id=add_subject_favList
        para="page=1&page_size=50"
        response = base().return_request(method="get", path=PathMessage.subject_favList, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        subject_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].subject_id')
        assert subject_id in subject_id_list

    @pytest.mark.run(order=2)
    @allure.description("""验证取消话题收藏，话题收藏列表是否正确显示""")
    @allure.title("取消收藏话题，收藏列表正确显示")
    def test_subject_favList_fav(self,get_token,get_host,add_subject_favList):
        subject_id=add_subject_favList
        # 取消话题收藏
        fav_para = {"subject_id": subject_id}
        fav_response = base().return_request(method="post", path=PathMessage.subject_fav, data=json.dumps(fav_para),
                                             tokens=get_token, hosts=get_host)
        para="page=1&page_size=50"
        response = base().return_request(method="get", path=PathMessage.subject_favList, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        subject_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].subject_id')
        assert subject_id not in subject_id_list
