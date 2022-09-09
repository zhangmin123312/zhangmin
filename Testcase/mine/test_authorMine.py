# -*- coding: utf-8 -*-
# @Time    : 2022/1/12
# @Author  : linchenzhen
# @File    : test_authorMine.py

import allure
import jsonpath
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os,json

@allure.feature('达人收藏')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_AuthorMine():

    @pytest.mark.run(order=1)
    @allure.description("""验证添加达人，达人收藏列表是否正确显示""")
    @allure.title("添加达人，收藏列表正确显示")
    def test_authorMine_list(self,get_token,get_host,add_author):
        author_id, nickname, label,group_id=add_author
        para=f"page=1&page_size=50&star_category=&group_id=&sub_user_id=0&keyword="
        response = base().return_request(method="get", path=PathMessage.authorMine_listsV2, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        author_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].author.author_id')
        assert author_id in author_id_list

    @pytest.mark.run(order=1)
    @allure.description("""验证搜索达人昵称，达人收藏列表是否正确显示""")
    @allure.title("搜索达人昵称，收藏列表正确显示")
    def test_authorMine_keyword(self,get_token,get_host,add_author):
        author_id, nickname, label,group_id=add_author
        para=f"page=1&page_size=50&star_category=&group_id=&sub_user_id=0&keyword={nickname}"
        response = base().return_request(method="get", path=PathMessage.authorMine_listsV2, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        nickname_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].author.nickname')
        assert nickname in nickname_list

    # @pytest.mark.run(order=1)
    # @allure.description("""验证按达人分类筛选，达人收藏列表是否正确显示""")
    # @allure.title("搜索达人分类，收藏列表正确显示")
    # def test_authorMine_star_category(self,get_token,get_host,add_author):
    #     author_id, nickname, tag,group_id=add_author
    #     para=f"page=1&page_size=50&star_category={tag}&group_id=&sub_user_id=0&keyword="
    #     response = base().return_request(method="get", path=PathMessage.authorMine_listsV2, data=para, tokens=get_token,hosts=get_host)
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]["list"]) > 0
    #     author_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].author.author_id')
    #     assert author_id in author_id_list

    @pytest.mark.run(order=1)
    @allure.description("""验证添加达人后，达人分类正确是否正确显示""")
    @allure.title("搜索添加达人后，达人分类正确是否正确显示")
    def test_authorMine_getLabels_tag(self,get_token,get_host,add_author):
        author_id, nickname, tag,group_id=add_author
        para=f"sub_user_id=0&is_star=1"
        response = base().return_request(method="get", path=PathMessage.authorMine_getLabels, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]) > 0
        key_list = jsonpath.jsonpath(response["response_body"], f'$.data[*].key')
        assert tag in key_list

    @pytest.mark.run(order=1)
    @allure.description("""验证子账号达人收藏列表是否正确显示""")
    @allure.title("子账号收藏列表正确显示")
    def test_authorMine_sub_user_id(self,get_token,get_host,common_init):
        para=f"page=1&page_size=50&star_category=&group_id=&sub_user_id={common_init}&keyword="
        response = base().return_request(method="get", path=PathMessage.authorMine_listsV2, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @pytest.mark.run(order=1)
    @allure.description("""验证按达人分组筛选，达人收藏列表是否正确显示""")
    @allure.title("搜索达人分组，收藏列表正确显示")
    def test_authorMine_group_id(self,get_token,get_host,add_author):
        author_id, nickname, tag,group_id=add_author
        para=f"page=1&page_size=50&star_category=&group_id={group_id}&sub_user_id=0&keyword="
        response = base().return_request(method="get", path=PathMessage.authorMine_listsV2, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        author_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].author.author_id')
        assert author_id in author_id_list

    @pytest.mark.run(order=2)
    @allure.description("""验证删除达人分组，达人收藏列表是否正确显示""")
    @allure.title("删除达人分组，收藏列表正确显示")
    def test_authorMine_del_group_id(self,get_token,get_host,add_author):
        author_id, nickname, tag,group_id=add_author
        # 删除达人分组
        delGroup_para = {"group_id": group_id}
        delGroup_response = base().return_request(method="post", path=PathMessage.authorMine_delGroup,
                                                  data=json.dumps(delGroup_para), tokens=get_token,
                                                  hosts=os.environ["host"])

        para=f"page=1&page_size=50&star_category=&group_id=&sub_user_id=0&keyword="
        response = base().return_request(method="get", path=PathMessage.authorMine_listsV2, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(jsonpath.jsonpath(response["response_body"], f'$.data.list[*].author.author_id')) > 0
        author_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].author.author_id')
        assert author_id in author_id_list


    # @pytest.mark.run(order=3)
    # @allure.description("""验证取消达人收藏，达人收藏列表是否正确显示""")
    # @allure.title("取消收藏达人，收藏列表正确显示")
    # def test_authorMine_fav(self,get_token,get_host,add_author):
    #     author_id, nickname, label,group_id=add_author
    #     # 取消达人收藏
    #     fav_para = {"author_id": author_id}
    #     fav_response = base().return_request(method="post", path=PathMessage.author_fav, data=json.dumps(fav_para),
    #                                          tokens=get_token, hosts=get_host)
    #     para=f"page=1&page_size=50&star_category=&group_id=&sub_user_id=0&keyword="
    #     response = base().return_request(method="get", path=PathMessage.authorMine_listsV2, data=para, tokens=get_token,hosts=get_host)
    #     assert response["status_code"] == 200
    #     assert len(response["response_body"]["data"]["list"]) > 0
    #     author_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].author.author_id')
    #     assert author_id not in author_id_list