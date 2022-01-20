# -*- coding: utf-8 -*-
# @Time    : 2022/1/13
# @aweme_info  : linchenzhen
# @File    : test_aweme_favLists.py

import allure
import jsonpath
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,json

@allure.feature('视频收藏')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Aweme_FavLists():

    @pytest.mark.run(order=1)
    @allure.description("""验证添加视频，视频收藏列表是否正确显示""")
    @allure.title("添加视频，收藏列表正确显示")
    def test_aweme_favLists_list(self,get_token,get_host,add_aweme_fav):
        aweme_id,aweme_title,category,group_id=add_aweme_fav
        para={"page": 1,"page_size": 50,"label": "","keyword": "","group_id": 0,"sub_user_id":""}
        response = base().return_request(method="post", path=PathMessage.aweme_favLists, data=json.dumps(para), tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["fav_lists"]) > 0
        aweme_title_list = jsonpath.jsonpath(response["response_body"], f'$.data.fav_lists[*].aweme_info.aweme_title')
        assert aweme_title in aweme_title_list

    @pytest.mark.run(order=2)
    @allure.description("""验证搜索视频昵称，视频收藏列表是否正确显示""")
    @allure.title("搜索视频昵称，收藏列表正确显示")
    def test_aweme_favLists_keyword(self,get_token,get_host,add_aweme_fav):
        aweme_id,aweme_title,category,group_id=add_aweme_fav
        para={"page": 1,"page_size": 50,"label": "","keyword": aweme_title,"group_id": 0,"sub_user_id":""}
        response = base().return_request(method="post", path=PathMessage.aweme_favLists, data=json.dumps(para), tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["fav_lists"]) > 0
        aweme_title_list = jsonpath.jsonpath(response["response_body"], f'$.data.fav_lists[*].aweme_info.aweme_title')
        assert aweme_title in aweme_title_list

    @pytest.mark.run(order=3)
    @allure.description("""验证按视频分类筛选，视频收藏列表是否正确显示""")
    @allure.title("搜索视频分类，收藏列表正确显示")
    def test_aweme_favLists_star_category(self,get_token,get_host,add_aweme_fav):
        aweme_id,aweme_title,category,group_id=add_aweme_fav
        para={"page": 1,"page_size": 50,"label": category,"keyword": "","group_id": 0,"sub_user_id":""}
        response = base().return_request(method="post", path=PathMessage.aweme_favLists, data=json.dumps(para), tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["fav_lists"]) > 0
        aweme_title_list = jsonpath.jsonpath(response["response_body"], f'$.data.fav_lists[*].aweme_info.aweme_title')
        assert aweme_title in aweme_title_list

    @pytest.mark.run(order=4)
    @allure.description("""验证添加视频后，视频分类正确是否正确显示""")
    @allure.title("搜索添加视频后，视频分类正确是否正确显示")
    def test_aweme_favLists_getLabels_category(self,get_token,get_host,add_aweme_fav):
        aweme_id,aweme_title,category,group_id=add_aweme_fav
        para=f"sub_user_id=0"
        response = base().return_request(method="get", path=PathMessage.aweme_favListCat, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]) > 0
        label_list = jsonpath.jsonpath(response["response_body"], f'$.data[*].label')
        assert category in label_list

    @pytest.mark.run(order=5)
    @allure.description("""验证子账号视频收藏列表是否正确显示""")
    @allure.title("子账号收藏列表正确显示")
    def test_aweme_favLists_sub_user_id(self,get_token,get_host,common_init):
        para = {"page": 1, "page_size": 50, "label": "", "keyword": "", "group_id": 0, "sub_user_id": common_init}
        response = base().return_request(method="post", path=PathMessage.aweme_favLists, data=json.dumps(para), tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["fav_lists"]) > 0

    @pytest.mark.run(order=6)
    @allure.description("""验证按视频分组筛选，视频收藏列表是否正确显示""")
    @allure.title("搜索视频分组，收藏列表正确显示")
    def test_aweme_favLists_group_id(self,get_token,get_host,add_aweme_fav):
        aweme_id,aweme_title,category,group_id=add_aweme_fav
        para = {"page": 1, "page_size": 50, "label": "", "keyword": "", "group_id": group_id, "sub_user_id": ""}
        response = base().return_request(method="post", path=PathMessage.aweme_favLists, data=json.dumps(para), tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["fav_lists"]) > 0
        aweme_title_list = jsonpath.jsonpath(response["response_body"], f'$.data.fav_lists[*].aweme_info.aweme_title')
        assert aweme_title in aweme_title_list

    @pytest.mark.run(order=7)
    @allure.description("""验证删除视频分组，视频收藏列表是否正确显示""")
    @allure.title("删除视频分组，收藏列表正确显示")
    def test_aweme_favLists_del_group_id(self,get_token,get_host,add_aweme_fav):
        aweme_id,aweme_title,category,group_id=add_aweme_fav
        # 删除视频分组
        delGroup_para = {"id": group_id}
        delGroup_response = base().return_request(method="post", path=PathMessage.aweme_favGroupDel,
                                                  data=json.dumps(delGroup_para), tokens=get_token,
                                                  hosts=os.environ["host"])
        para = {"page": 1, "page_size": 50, "label": "", "keyword": "", "group_id": "", "sub_user_id": ""}
        response = base().return_request(method="post", path=PathMessage.aweme_favLists, data=json.dumps(para), tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["fav_lists"]) > 0
        aweme_title_list = jsonpath.jsonpath(response["response_body"], f'$.data.fav_lists[*].aweme_info.aweme_title')
        assert aweme_title in aweme_title_list

    @pytest.mark.run(order=8)
    @allure.description("""验证取消视频收藏，视频收藏列表是否正确显示""")
    @allure.title("取消收藏视频，收藏列表正确显示")
    def test_aweme_favLists_fav(self,get_token,get_host,add_aweme_fav):
        aweme_id,aweme_title,category,group_id=add_aweme_fav
        # 取消视频收藏
        fav_para = {"aweme_id": aweme_id,"sub_user_id": 0}
        fav_response = base().return_request(method="post", path=PathMessage.aweme_favCancel, data=json.dumps(fav_para),
                                             tokens=get_token, hosts=get_host)
        para = {"page": 1, "page_size": 50, "label": "", "keyword": "", "group_id": "", "sub_user_id": ""}
        response = base().return_request(method="post", path=PathMessage.aweme_favLists, data=json.dumps(para), tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["fav_lists"]) > 0
        aweme_title_list = jsonpath.jsonpath(response["response_body"], f'$.data.fav_lists[*].aweme_info.aweme_title')
        assert aweme_title not in aweme_title_list