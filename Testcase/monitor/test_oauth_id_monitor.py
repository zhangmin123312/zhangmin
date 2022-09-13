# -*- coding: utf-8 -*-
# @Time    : 2022/9/14
# @Author  : zhangmin
# @File    : test_oauth_id_monitor.py
import allure
import jsonpath
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os,json
@allure.feature('评论监控')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_oauth_id_monitor():


    @allure.description("""验证评论列表显示是否正确""")
    @allure.title("验证评论列表显示是否正确")
    def test_oauth_id_list(self, get_token, get_host):
        response_auth = base().return_request(method="get", path=PathMessage.authormine_auth, tokens=get_token,
                                         hosts=get_host)
        response_auth_id=response_auth["response_body"]["data"]["list"][0]["oauth"]['id']
        response_auth_expire=response_auth["response_body"]["data"]["list"][0]["oauth"]['expire']
        if response_auth_expire == 0:
            para = f"oauth_id={response_auth_id}&cursor=0"
            response_expire0 = base().return_request(method="get", path=PathMessage.getCreatorAwemeList, data=para, tokens=get_token,
                                             hosts=get_host)
            # print(response_expire1)
            assert response_expire0["status_code"] == 200
            assert len(response_expire0["response_body"]["data"]["item_info_list"]) > 0
        elif response_auth_expire == 1:
            para = f"oauth_id={response_auth_id}&cursor=0"
            response_expire1 = base().return_request(method="get", path=PathMessage.getCreatorAwemeList, data=para,
                                             tokens=get_token,
                                             hosts=get_host)
            # print(response_expire2)
            assert response_expire1["status_code"] == 200
            assert response_expire1["response_body"]['errMsg'] == '抖音号授权已过期，请重新授权'


