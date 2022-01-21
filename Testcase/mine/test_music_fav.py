# -*- coding: utf-8 -*-
# @Time    : 2022/1/21
# @Author  : linchenzhen
# @File    : test_music_fav.py

import allure
import jsonpath
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,json

@allure.feature('音乐收藏')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Music_FavLists():

    @pytest.mark.run(order=1)
    @allure.description("""验证添加音乐，音乐收藏列表是否正确显示""")
    @allure.title("添加音乐，收藏列表正确显示")
    def test_music_favLists_list(self,get_token,get_host,add_music_favLists):
        music_id=add_music_favLists
        para={"sub_user_id": 0,	"page": 1,	"page_size": 50}
        response = base().return_request(method="post", path=PathMessage.music_favLists, data=json.dumps(para), tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["fav_lists"]) > 0
        music_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.fav_lists[*].id')
        assert music_id in music_id_list


    @pytest.mark.run(order=1)
    @allure.description("""验证子账号音乐收藏列表是否正确显示""")
    @allure.title("子账号音乐收藏列表正确显示")
    def test_music_favLists_subAccount(self,get_token,get_host,common_init):
        para={"sub_user_id": common_init,	"page": 1,	"page_size": 50}
        response = base().return_request(method="post", path=PathMessage.music_favLists, data=json.dumps(para), tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["fav_lists"]) > 0


    @pytest.mark.run(order=2)
    @allure.description("""验证取消音乐收藏，音乐收藏列表是否正确显示""")
    @allure.title("取消收藏音乐，收藏列表正确显示")
    def test_music_favLists_fav(self,get_token,get_host,add_music_favLists):
        music_id=add_music_favLists
        # 取消音乐收藏
        fav_para = {"music_id": music_id}
        fav_response = base().return_request(method="post", path=PathMessage.music_fav, data=json.dumps(fav_para),
                                             tokens=get_token, hosts=get_host)
        para={"sub_user_id": 0,	"page": 1,	"page_size": 50}
        response = base().return_request(method="post", path=PathMessage.music_favLists, data=json.dumps(para), tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["fav_lists"]) > 0
        music_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.fav_lists[*].id')
        assert music_id not in music_id_list
