# # -*- coding: utf-8 -*-
# # @Time    : 2021/12/13
# # @Author  : chenxubin
# # @File    : test_authorRank_starRank.py
# import allure
# import pytest
#
# from Common.Base import base
# from Config.path_config import PathMessage
#
#
# @allure.feature('商品分享榜')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
# class TestCase_AuthorRank_StarRank():
#
#     @allure.story('验证商品分享榜日榜数据是否大于20条')
#     def test_authorRank_starRank_day_data(self, get_token, get_host,):
#         para = "date={}&page=1&size=50&share_type=0&star_category=&province=".format(base.return_time_message()[0][1])
#         responce = base().return_request(method="get", path=PathMessage.authorRank_starDailyRank, data=para, tokens=get_token,
#                                          hosts=get_host, )
#
#         assert responce["status_code"] == 200
#         assert len(responce["response_body"]["data"]["list"]) > 20
#
#
#
#
#     @allure.story('验证商品分享榜周榜和月榜数据是否大于20条')
#     @pytest.mark.parametrize('times', base.return_time_message()[1:3])
#     def test_authorRank_starRank_week_moth(self, get_token, get_host,times):
#         para = "day_type={}&date={}&page=1&size=50&share_type=0&star_category=&province=".format(times[0],times[1])
#         print(para)
#         responce = base().return_request(method="get", path=PathMessage.authorRank_starRank, data=para,
#                                          tokens=get_token,
#                                          hosts=get_host, )
#
#         assert responce["status_code"] == 200
#         assert len(responce["response_body"]["data"]["list"]) > 20
#
#
#
#
#
#
#
#
#
#
