# -*- coding: utf-8 -*-
# @Time    : 2021/12/7
# @Author  : chenxubin
# @File    : test_brand_search
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os
import datetime,time
import jsonpath


@allure.feature('抖音品牌库')
# @pytest.mark.flaky(reruns=5, reruns_delay=2)
class TestCase_Brand_Search():
    datatime1 = datetime.datetime.now() - datetime.timedelta(days=1)
    start_time = datatime1.strftime('%Y-%m-%d')
    datatime2 = datetime.datetime.now() - datetime.timedelta(days=30)
    end_time = datatime2.strftime('%Y-%m-%d')


    @allure.story('验证抖音品牌库遍历商品大类返回的数据是否大于20条')
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("抖音品牌库请求类目：{product_type}")
    def test_brand_search_product_type(self,get_token,get_host,product_type):
        para = "page=1&category={},,&keyword=&day=week&volume_range_30=&amount_range_30=&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30=&sale_way=-1&fans_age=&fans_gender=-1&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date=2022-09-17&end_date=2022-10-16&from=detail".format(product_type[0],TestCase_Brand_Search.end_time,TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para,tokens=get_token,hosts=get_host, )
        assert len(responce["response_body"]["data"]["list"]) > 20




    @allure.story('验证抖音品牌库商品数、销量、销售额、升序、降序排序是否正确')
    @pytest.mark.parametrize('day', ["day","week","month"])
    @pytest.mark.parametrize('sort', ["product_sum_1","day_volume","day_amount"])
    @pytest.mark.parametrize('orderby', ["desc", "asc"])
    @allure.title("抖音品牌库筛选日期:{day}筛选类型:{sort},排序类型:{orderby}")
    def test_brand_search_sort_day_orderby(self,get_token,get_host,day,sort,orderby):
        para = "page=1&category=,,&keyword=&day={}&volume_range_30=&amount_range_30=&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30=&sale_way=-1&fans_age=&fans_gender=-1&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort={}&order_by={}&size=50&start_date={}&end_date={}&from=detail".format(day,sort,orderby,TestCase_Brand_Search.end_time,TestCase_Brand_Search.start_time)
        # print(para)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para,tokens=get_token,hosts=get_host )["response_body"]["data"]["list"]
        assert len(responce) > 20
        if orderby=='desc':
            product_sum_1 = float('inf')
            if sort == "product_sum_1":
                for i in responce:
                    assert i['product_sum_1'] <=product_sum_1
                    product_sum_1=i["product_sum_1"]

        elif orderby=='asc':
            product_sum_1 = float('inf')
            if sort == "product_sum_1":
                for i in responce:
                    assert i['product_sum_1'] <=product_sum_1
                    product_sum_1=i["product_sum_1"]

        # if orderby == 'asc':
        #     product_sum_1 = float('inf')
        #     if sort == "product_sum_1":
        #         for i in responce:
        #             assert i['product_sum_1'] >= product_sum_1
        #             print(product_sum_1)
        #             product_sum_1=i["product_sum_1"]



        # if orderby == "desc":
        #
        #     day_amount = float("inf")
        #     day_volume = float("inf")
        #     day_interaction_inc = float("inf")
        #
        #     if sort == "day_volume":
        #         for i in responce:
        #             assert i["day_volume"] <= day_volume
        #             day_volume = i["day_volume"]
        #
        #
        #     elif sort == "day_amount":
        #         for i in responce:
        #             assert i["day_amount"] <= day_amount
        #             day_amount = i["day_amount"]
        #
        #     elif sort == "day_interaction_inc":
        #         for i in responce:
        #             assert i["day_interaction_inc"] <= day_interaction_inc
        #             day_interaction_inc = i["day_interaction_inc"]
        #
        #
        #     else:
        #         print("排序传参有误")
        #         raise False
        #
        # elif orderby == "asc":
        #
        #     day_amount = -float("inf")
        #     day_volume = -float("inf")
        #     day_interaction_inc = -float("inf")
        #
        #     if sort == "day_volume":
        #         for i in responce:
        #             assert i["volume"] >= day_volume
        #             day_volume = i["volume"]
        #
        #
        #     elif sort == "day_amount":
        #         for i in responce:
        #             assert i["day_amount"] >= day_amount
        #             day_amount = i["day_amount"]
        #
        #     elif sort == "day_interaction_inc":
        #         for i in responce:
        #             assert i["day_interaction_inc"] >= day_interaction_inc
        #             day_interaction_inc = i["day_interaction_inc"]
        #
        #     else:
        #         print("排序传参有误")
        #         raise False
        #
        # else:
        #     print("desc或asc传参有误")
        #     raise False


    # @allure.story('验证抖音品牌库近30日销售额筛选与详情页校验')
    # @allure.title("近30日销售额筛选区间：{amount_range},直播带货状态：{has_live_sale},视频带货状态：{has_aweme_sale}")
    # @pytest.mark.parametrize('amount_range', ["100-500", "500-1000", "2000-5000"])
    # @pytest.mark.parametrize('has_live_sale', [0,1])
    # @pytest.mark.parametrize('has_aweme_sale', [0,1])
    # def test_brand_search_amount(self, get_token, get_host,amount_range,has_live_sale,has_aweme_sale):
    #     para = "page=1&category=&keyword=&fans_age=&fans_gender=-1&fans_province=&sort=day_volume&order_by=desc&size=20&has_aweme_sale={}&has_live_sale={}&interaction_inc_range=&amount_range={}".format(has_aweme_sale,has_live_sale,amount_range)
    #     responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
    #     amount_list = amount_range.split("-")
    #     for i in responce:
    #         with allure.step("校验详情页近30日销售额是否在所选区间内"):
    #             para = "brand_code=" + i["brand_code"]
    #             responce = base().return_request(method="get", path=PathMessage.brand_detail_info, data=para, tokens=get_token,
    #                                   hosts=get_host, )["response_body"]["data"]
    #             assert responce["month_amount"] >= int(amount_list[0]) and responce["month_amount"] <= int(amount_list[1])




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


    @allure.story('验证品牌库近30日销售额筛选')
    @allure.title("近30日销售额筛选区间：{amount_range_30}")
    @pytest.mark.parametrize('amount_range_30', ["100000-1000000", "30000-100000", "-30000",'1000000-10000000','10000000-'])
    def test_brand_search_amount(self, get_token, get_host,amount_range_30):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30= &amount_range_30={}&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30=&sale_way=-1&fans_age=&fans_gender=-1&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(amount_range_30,TestCase_Brand_Search.end_time,TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 20


    @allure.story('验证品牌库近30日销量筛选')
    @allure.title("近30日销量筛选区间：{volume_range_30}")
    @pytest.mark.parametrize('volume_range_30', ['-50000',"50000-100000","100000-300000","300000-500000","500000-"])
    def test_brand_search_volume(self, get_token, get_host,volume_range_30):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30={}&amount_range_30=&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30=&sale_way=-1&fans_age=&fans_gender=-1&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(volume_range_30,TestCase_Brand_Search.end_time,TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 20



    @allure.story('验证品牌库近30日关联达人数筛选')
    @allure.title("近30日关联达人数筛选区间：{author_sum_30}")
    @pytest.mark.parametrize('author_sum_30', ['-10',"10-100","100-1000","1000-5000"])
    def test_brand_search_author_sum_30(self, get_token, get_host,author_sum_30):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30=&amount_range_30={}&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30=&sale_way=-1&fans_age=&fans_gender=-1&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(author_sum_30,TestCase_Brand_Search.end_time,TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 20


    @allure.story('验证品牌库近30日视频数筛选')
    @allure.title("近30日关联视频数筛选区间：{aweme_sum_30}")
    @pytest.mark.parametrize('aweme_sum_30', ['-10',"10-100","100-1000","1000-5000"])
    def test_brand_search_aweme_sum_30(self, get_token, get_host,aweme_sum_30):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30=&amount_range_30=&aweme_sum_30={}&live_sum_30=&author_sum_30=&product_sum_30=&sale_way=-1&fans_age=&fans_gender=-1&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(aweme_sum_30,TestCase_Brand_Search.end_time,TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 10


    @allure.story('验证品牌库近30日直播数筛选')
    @allure.title("近30日关联直播数筛选区间：{live_sum_30}")
    @pytest.mark.parametrize('live_sum_30', ['-10',"10-100","100-1000","1000-5000"])
    def test_brand_search_live_sum_30(self, get_token, get_host,live_sum_30):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30=&amount_range_30=&aweme_sum_30=&live_sum_30={}&author_sum_30=&product_sum_30=&sale_way=-1&fans_age=&fans_gender=-1&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(live_sum_30,TestCase_Brand_Search.end_time,TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 10


    @allure.story('验证品牌库近30日商品数筛选')
    @allure.title("近30日关联商品数筛选区间：{product_sum_30}")
    @pytest.mark.parametrize('product_sum_30', ['-10',"10-100","100-500","500-"])
    def test_brand_search_product_sum_30(self, get_token, get_host,product_sum_30):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30=&amount_range_30=&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30={}&sale_way=-1&fans_age=&fans_gender=-1&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(product_sum_30,TestCase_Brand_Search.end_time,TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 10



    @allure.story('验证品牌库近30日直播带货为主视频带货为主筛选')
    @allure.title("近30日带货方式：{sale_way}")
    @pytest.mark.parametrize('sale_way', ['-1', "1", "2"])
    def test_brand_search_sale_way(self, get_token, get_host, sale_way):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30=&amount_range_30=&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30=&sale_way={}&fans_age=&fans_gender=-1&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(
            sale_way, TestCase_Brand_Search.end_time, TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,
                                         hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 10

        para_main = "brand_code={}".format(responce[0]['brand_code'])
        responce_main = base().return_request(method="get", path=PathMessage.brand_detail_info, data=para_main, tokens=get_token,
                                  hosts=get_host)["response_body"]["data"]["main_way"]
        if sale_way=='1':
            assert responce_main == '直播'
        if sale_way=='2':
            assert responce_main == '视频'


    @allure.story('验证品牌库近30日带货渠道筛选')
    @allure.title("近30日带货渠道：{channel}{open_channel}")
    @pytest.mark.parametrize('channel', ['channel_brand', "channel_shop","channel_author"])
    @pytest.mark.parametrize('open_channel', ['0', "1"])#1勾选带货渠道0不勾选
    def test_brand_search_channel(self, get_token, get_host, channel,open_channel):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30=&amount_range_30=&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30=&sale_way=&fans_age=&fans_gender=-1&multi_fans_areas=[%22%22]&{}={}&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(
            channel,open_channel, TestCase_Brand_Search.end_time, TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,
                                         hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 10
        if channel=="channel_brand":
            if open_channel=='1':
                    para_main = "brand_code={}".format(responce[0]['brand_code'])
                    responce_main = \
                    base().return_request(method="get", path=PathMessage.brand_detail_info, data=para_main,
                                          tokens=get_token,
                                          hosts=get_host)["response_body"]["data"]["main_chanel"]
                    assert responce_main =='品牌自播'
        elif channel=="channel_author":
            if open_channel=='1':
                    para_main = "brand_code={}".format(responce[0]['brand_code'])
                    responce_main = \
                    base().return_request(method="get", path=PathMessage.brand_detail_info, data=para_main,
                                          tokens=get_token,
                                          hosts=get_host)["response_body"]["data"]["main_chanel"]
                    assert responce_main =='达人播'
        elif channel=="channel_shop":
            if open_channel=='1':
                    para_main = "brand_code={}".format(responce[0]['brand_code'])
                    responce_main = \
                    base().return_request(method="get", path=PathMessage.brand_detail_info, data=para_main,
                                          tokens=get_token,
                                          hosts=get_host)["response_body"]["data"]["main_chanel"]
                    assert responce_main =='小店播'



    @allure.story('验证品牌库主要性别筛选')
    @allure.title("近30日主要性别筛选：{fans_gender}")
    @pytest.mark.parametrize('fans_gender', ['0', "1",'-1'])
    def test_brand_search_fans_gender(self, get_token, get_host, fans_gender):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30=&amount_range_30=&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30=&sale_way=-1&fans_age=&fans_gender={}&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(
            fans_gender, TestCase_Brand_Search.end_time, TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,
                                         hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 10

    @allure.story('验证品牌库主要年龄筛选')
    @allure.title("近30日主要年龄筛选：{fans_age}")
    @pytest.mark.parametrize('fans_age', ['2', "3",'4',"5","6"])
    def test_brand_search_fans_gender(self, get_token, get_host, fans_age):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30=&amount_range_30=&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30=&sale_way=-1&fans_age={}&fans_gender=&multi_fans_areas=[%22%22]&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(
            fans_age, TestCase_Brand_Search.end_time, TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,
                                         hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 20

    @allure.story('验证品牌库主要地区筛选')
    @allure.title("近30日主要地区筛选：{fans_areas}")
    @pytest.mark.parametrize('fans_areas', ['北京市', "河北省",'["江苏省","南京市"]','上海市'])
    def test_brand_search_fans_gender(self, get_token, get_host, fans_areas):
        para = "page=1&category=,,&keyword=&day=week&volume_range_30=&amount_range_30=&aweme_sum_30=&live_sum_30=&author_sum_30=&product_sum_30=&sale_way=-1&fans_age=&fans_gender=&multi_fans_areas=['{}']&channel_brand=0&channel_shop=0&channel_author=0&sort=day_amount&order_by=desc&size=50&start_date={}&end_date={}&from=detail".format(
            fans_areas, TestCase_Brand_Search.end_time, TestCase_Brand_Search.start_time)
        responce = base().return_request(method="get", path=PathMessage.brand_search, data=para, tokens=get_token,
                                         hosts=get_host, )["response_body"]["data"]["list"]
        assert len(responce) > 10