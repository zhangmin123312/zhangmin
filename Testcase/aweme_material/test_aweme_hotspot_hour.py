# -*- coding: utf-8 -*-
# @Time    : 2022/1/6
# @Author  : linchenzhen
# @File    : test_aweme_hotspot_hour.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
import os
@allure.feature('小时探测榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Aweme_Hotspot_Hour():


    @allure.description("""验证小时探测榜遍历所有的小时榜点是否有返回数据""")
    @pytest.mark.parametrize('hour_interval',base.return_hotspot_time(os.getenv("token"),os.getenv("host"),data_type='hour'))
    @allure.title("小时探测榜查看榜点：{hour_interval}")
    def test_hotspot_hour_interval(self,get_token,get_host,hour_interval):
        para=f"hour_interval={hour_interval}&publish_time=&size=50&page=1"
        response = base().return_request(method="get", path=PathMessage.aweme_hotspot_hour, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证小时探测榜按视频发布时间筛选是否有返回数据""")
    @pytest.mark.parametrize('publish_time',base.return_hotspot_time(os.getenv("token"),os.getenv("host")))
    @pytest.mark.parametrize('hour_interval',[base.return_hotspot_time(os.getenv("token"),os.getenv("host"),data_type='hour')[0]])
    @allure.title("小时探测榜{publish_time}发布的视频在{hour_interval}排榜情况")
    def test_hotspot_publish_time(self,get_token,get_host,hour_interval,publish_time):
        para=f"hour_interval={hour_interval}&publish_time={publish_time}&size=50&page=1"
        response = base().return_request(method="get", path=PathMessage.aweme_hotspot_hour, data=para, tokens=get_token,hosts=get_host)
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0