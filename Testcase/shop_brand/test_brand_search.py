# -*- coding: utf-8 -*-
# @Time    : 2021/12/7
# @Author  : chenxubin
# @File    : test_brand_search
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os


@allure.feature('抖音品牌库')
@pytest.mark.flaky(reruns=5, reruns_delay=2)
class TestCase_Brand_Search():

    @allure.story('验证抖音品牌库遍历商品大类返回的数据是否大于20条')
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("抖音品牌库请求类目：{product_type}")
    def test_brand_search_product_type(self,get_token,get_host,product_type):
        para = "page=1&category={}&keyword=&fans_age=&fans_gender=-1&fans_province=&sort=day_volume&order_by=desc&size=50&has_aweme_sale=0&has_live_sale=0&interaction_inc_range=&amount_range=".format(product_type[0])
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para,tokens=get_token,hosts=get_host, )
        assert len(responce["response_body"]["data"]["list"]) > 20




    @allure.story('验证抖音品牌库、销量、销售额、升序、降序排序是否正确')
    @pytest.mark.parametrize('sort', ["day_amount","day_volume","day_interaction_inc"])
    @pytest.mark.parametrize('orderby', ["desc", "asc",])
    @allure.title("抖音品牌库筛选类型：{sort},排序类型:{orderby}")
    def test_brand_search_sort(self,get_token,get_host,sort,orderby):
        para = "page=1&category=&keyword=&fans_age=&fans_gender=-1&fans_province=&sort={}day_volume&order_by={}&size=20&has_aweme_sale=0&has_live_sale=0&interaction_inc_range=&amount_range=".format(sort,orderby)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para,tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]


        if orderby == "desc":

            day_amount = float("inf")
            day_volume = float("inf")
            day_interaction_inc = float("inf")

            if sort == "day_volume":
                for i in responce:
                    assert i["day_volume"] <= day_volume
                    day_volume = i["day_volume"]


            elif sort == "day_amount":
                for i in responce:
                    assert i["day_amount"] <= day_amount
                    day_amount = i["day_amount"]

            elif sort == "day_interaction_inc":
                for i in responce:
                    assert i["day_interaction_inc"] <= day_interaction_inc
                    day_interaction_inc = i["day_interaction_inc"]


            else:
                print("排序传参有误")
                raise False

        elif orderby == "asc":

            day_amount = -float("inf")
            day_volume = -float("inf")
            day_interaction_inc = -float("inf")

            if sort == "day_volume":
                for i in responce:
                    assert i["volume"] >= day_volume
                    day_volume = i["volume"]


            elif sort == "day_amount":
                for i in responce:
                    assert i["day_amount"] >= day_amount
                    day_amount = i["day_amount"]

            elif sort == "day_interaction_inc":
                for i in responce:
                    assert i["day_interaction_inc"] >= day_interaction_inc
                    day_interaction_inc = i["day_interaction_inc"]

            else:
                print("排序传参有误")
                raise False

        else:
            print("desc或asc传参有误")
            raise False


    @allure.story('验证抖音品牌库近30日销售额筛选与详情页校验')
    @allure.title("近30日销售额筛选区间：{amount_range},直播带货状态：{has_live_sale},视频带货状态：{has_aweme_sale}")
    @pytest.mark.parametrize('amount_range', ["100-500", "500-1000", "2000-5000"])
    @pytest.mark.parametrize('has_live_sale', [0,1])
    @pytest.mark.parametrize('has_aweme_sale', [0,1])
    def test_brand_search_amount(self, get_token, get_host,amount_range,has_live_sale,has_aweme_sale):
        para = "page=1&category=&keyword=&fans_age=&fans_gender=-1&fans_province=&sort=day_volume&order_by=desc&size=20&has_aweme_sale={}&has_live_sale={}&interaction_inc_range=&amount_range={}".format(has_aweme_sale,has_live_sale,amount_range)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
        amount_list = amount_range.split("-")
        for i in responce:
            with allure.step("校验详情页近30日销售额是否在所选区间内"):
                para = "brand_code=" + i["brand_code"]
                responce = base().return_request(method="get", path=PathMessage.brand_detail_info, data=para, tokens=get_token,
                                      hosts=get_host, )["response_body"]["data"]
                assert responce["month_amount"] >= int(amount_list[0]) and responce["month_amount"] <= int(amount_list[1])




    # @allure.story('验证抖音品牌库男女比例、主要年龄筛选是否与详情页一致')
    # @pytest.mark.parametrize('fans_gender',[0,1])
    # @pytest.mark.parametrize('fans_age',[0,1,2,3,4,5])
    # @allure.title("抖音品牌库筛选的性别比例传参为：{fans_gender}，主要年龄传参为{fans_age}",)
    # def test_brand_search_fans_gender(self, get_token, get_host, fans_gender,fans_age):
    #     para = "page=1&category=&keyword=&fans_age=&fans_gender={}&fans_province=&sort=day_volume&order_by=desc&size=20&has_aweme_sale=0&has_live_sale=0&interaction_inc_range=&amount_range=".format(fans_gender)
    #     responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,
    #                                      hosts=get_host, )["response_body"]["data"]["list"]
    #     for i in responce:
    #         para = "brand_code={}&start_time={}&end_time={}".format(i["brand_code"],base.get_time("nowday","del",30),base.get_time("nowday","del",1))
    #         responce = base().return_request(method="get", path=PathMessage.brand_detail_authorFansAnalysis, data=para, tokens=get_token,
    #                                 hosts=get_host, )["response_body"]["data"]["view_user"]["portrait_summary"]
    #
    #         if len(responce["gender_portrait"]) > 1:
    #
    #             responce = responce["gender_portrait"].replace("居多"," ").strip()
    #
    #             if fans_gender == 0:
    #
    #                 assert responce == "男性"
    #
    #
    #             elif fans_gender == 1:
    #
    #                 assert responce == "女性"
    #
    #         else:
    #             print("用户画像接口没返回数据")