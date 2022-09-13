# # -*- coding: utf-8 -*-
# # @Time    : 2021/12/22
# # @Author  : linchenzhen
# # @File    : test_authorRank_starDailyRank.py
#直播分享榜已下线
# import allure
# import pytest
#
# from Common.Base import base
# from Config.path_config import PathMessage
# import os,jsonpath
#
#
# @allure.feature('直播分享榜')
# # @pytest.mark.flaky(reruns=5, reruns_delay=1)
# class TestCase_AuthorRank_StarDailyRank():
#
#
#     @allure.description("""验证直播分享榜周榜是否有返回数据""")
#     @pytest.mark.parametrize('times', base.return_time_message()[1:2])
#     @allure.title("直播分享榜日期：{times}")
#     def test_starDailyRank_week(self,get_token,get_host,times):
#         para=f"day_type={times[0]}&date={times[1]}&page=1&size=50&share_type=1&star_category=&province="
#         response = base().return_request(method="get", path=PathMessage.rank_starDailyRank1, data=para,tokens=get_token,hosts=get_host, )
#         assert response["status_code"]==200
#         assert len(response["response_body"]["data"]["list"]) > 0
#
#     @allure.description("""验证直播分享榜月榜是否有返回数据""")
#     @pytest.mark.parametrize('times', base.return_time_message()[2:])
#     @allure.title("直播分享榜日期：{times}")
#     def test_starDailyRank_month(self,get_token,get_host,times):
#         para=f"day_type={times[0]}&date={times[1]}&page=1&size=50&share_type=1&star_category=&province="
#         response = base().return_request(method="get", path=PathMessage.rank_starDailyRank2, data=para,tokens=get_token,hosts=get_host, )
#         assert response["status_code"]==200
#         assert len(response["response_body"]["data"]["list"]) > 0
#
