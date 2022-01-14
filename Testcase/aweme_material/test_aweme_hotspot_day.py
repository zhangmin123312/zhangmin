# -*- coding: utf-8 -*-
# @Time    : 2022/1/7
# @Author  : linchenzhen
# @File    : test_aweme_hotspot_day.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os
@allure.feature('每日探测榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Aweme_Hotspot_day():


    @allure.description("""验证每日探测榜遍历所有榜点是否有返回数据""")
    @pytest.mark.parametrize('list_date',base.return_hotspot_time(os.getenv("token"),os.getenv("host"),data_type='day'))
    @allure.title("每日探测榜查看榜点：{list_date}")
    def test_hotspot_day_list_date(self,get_token,get_host,list_date):
        para=f"list_date={list_date}&publish_time=&size=50&page=1"
        response = base().return_request(method="get", path=PathMessage.aweme_hotspot_day, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证每日探测榜按视频发布时间筛选是否有返回数据""")
    @pytest.mark.parametrize('publish_time',base.return_hotspot_time(os.getenv("token"),os.getenv("host"),include_today=0))
    @pytest.mark.parametrize('list_date',[base.return_hotspot_time(os.getenv("token"),os.getenv("host"),data_type='day')[-1]])
    @allure.title("每日探测榜{publish_time}发布的视频在{list_date}排榜情况")
    def test_hotspot_day_publish_time(self,get_token,get_host,list_date,publish_time):
        para=f"list_date={list_date}&publish_time={publish_time}&size=50&page=1"
        response = base().return_request(method="get", path=PathMessage.aweme_hotspot_day, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0



