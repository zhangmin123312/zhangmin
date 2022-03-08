# -*- coding: utf-8 -*-
# @Time    : 2022/1/25
# @Author  : linchenzhen
# @File    : test_live_monitor.py

import allure
import jsonpath
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os,json

@allure.feature('直播监控')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_live_monitor():


    @allure.description("""验证添加直播，直播监控列表是否正确显示""")
    @allure.title("添加直播，监控列表正确显示")
    def test_live_monitor_list(self,get_token,get_host,add_live_monitor):
        nickname, unique_id, monitor_id_this, monitor_id_Next=add_live_monitor
        para=f"page=1&size=15&status=-1&keyword="
        response = base().return_request(method="get", path=PathMessage.live_monitor_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        nickname_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].nickname')
        assert nickname in nickname_list


    @allure.description("""验证搜索昵称，直播监控列表是否正确显示""")
    @allure.title("搜索昵称，监控列表正确显示")
    def test_live_monitor_nickname(self,get_token,get_host,add_live_monitor):
        nickname, unique_id, monitor_id_this, monitor_id_Next=add_live_monitor
        para=f"page=1&size=15&status=-1&keyword={nickname}"
        response = base().return_request(method="get", path=PathMessage.live_monitor_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        nickname_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].nickname')
        assert nickname in nickname_list

    @allure.description("""验证搜索抖音号，直播监控列表是否正确显示""")
    @allure.title("搜索抖音号，监控列表正确显示")
    def test_live_monitor_unique_id(self,get_token,get_host,add_live_monitor):
        nickname, unique_id, monitor_id_this, monitor_id_Next=add_live_monitor
        para=f"page=1&size=15&status=-1&keyword={unique_id}"
        response = base().return_request(method="get", path=PathMessage.live_monitor_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        unique_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].unique_id')
        assert unique_id in unique_id_list

    @allure.description("""验证按直播状态筛选，直播监控列表是否正确显示""")
    @pytest.mark.parametrize("status",[0,1,2])
    @allure.title("搜索直播状态{status}，监控列表正确显示")
    def test_live_monitor_status(self,get_token,get_host,add_live_monitor,status):
        para=f"page=1&size=15&status={status}&keyword="
        response = base().return_request(method="get", path=PathMessage.live_monitor_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证监控置顶，直播监控列表是否正确显示""")
    @allure.title("监控置顶，直播监控列表正确显示")
    def test_live_monitor_subAccount(self,get_token,get_host,add_live_monitor):
        nickname, unique_id, monitor_id_this, monitor_id_Next = add_live_monitor
        # 直播监控置顶
        topSwitch_para = {"id": monitor_id_Next,"top": 1}
        topSwitch_response = base().return_request(method="post", path=PathMessage.live_monitor_topSwitch, data=json.dumps(topSwitch_para),tokens=get_token, hosts=get_host)

        para=f"page=1&size=15&status=-1&keyword="
        response = base().return_request(method="get", path=PathMessage.live_monitor_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        assert all(value['top']==1 for value in response["response_body"]["data"]["list"] if value['id']==monitor_id_Next)

    @allure.description("""验证取消监控置顶，直播监控列表是否正确显示""")
    @allure.title("取消监控置顶，直播监控列表正确显示")
    def test_live_monitor_subAccount(self,get_token,get_host,add_live_monitor):
        nickname, unique_id, monitor_id_this, monitor_id_Next = add_live_monitor
        # 直播监控置顶
        topSwitch_para = {"id": monitor_id_Next,"top": 0}
        topSwitch_response = base().return_request(method="post", path=PathMessage.live_monitor_topSwitch, data=json.dumps(topSwitch_para),tokens=get_token, hosts=get_host)

        para=f"page=1&size=15&status=-1&keyword="
        response = base().return_request(method="get", path=PathMessage.live_monitor_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        assert all(value['top']==0 for value in response["response_body"]["data"]["list"] if value['id']==monitor_id_Next)

    @allure.description("""验证取消直播监控，直播监控列表是否正确显示""")
    @allure.title("取消监控直播，监控列表正确显示")
    def test_live_monitor_fav(self,get_token,get_host,add_live_monitor):
        nickname, unique_id, monitor_id_this, monitor_id_Next = add_live_monitor
        # 取消直播监控
        delete_para = {"monitor_id":monitor_id_Next}
        delete_response = base().return_request(method="post", path=PathMessage.live_monitor_cancel, data=json.dumps(delete_para),tokens=get_token, hosts=get_host)

        para=f"page=1&size=15&status=-1&keyword="
        response = base().return_request(method="get", path=PathMessage.live_monitor_list, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        monitor_id_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].id')
        assert monitor_id_Next not in monitor_id_list

