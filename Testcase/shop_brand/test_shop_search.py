# -*- coding: utf-8 -*-
# @Time    : 2021/12/7
# @Author  : chenxubin
# @File    : test_shop_search.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os

@allure.feature('抖音小店库')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Shop_Search():

    @allure.story('验证抖音小店库遍历商品大类返回的数据是否大于20条')
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @allure.title("抖音小店库请求类目：{product_type}")
    def test_shop_search_product_type(self,get_token,get_host,product_type):
        para = "page=1&big_category={}&first_category=&keyword=&sort=volume&orderby=desc&size=50&has_aweme=0&has_live=0&avg_price=&avg_amount=&expr_score=".format(product_type[0])
        responce = base().return_request(method="get", path=PathMessage.shop_search, data=para,tokens=get_token,hosts=get_host, )
        assert len(responce["response_body"]["data"]["list"]) > 20




    @allure.story('验证抖音小店库、销量、销售额、升序、降序排序是否正确')
    @pytest.mark.parametrize('sort', ["expr_score","volume","amount"])
    @pytest.mark.parametrize('orderby', ["desc", "asc",])
    @allure.title("抖音小店库筛选类型：{sort},排序类型:{orderby}")
    def test_shop_search_sort(self,get_token,get_host,sort,orderby):
        para = "page=1&big_category=&first_category=&keyword=&sort={}&orderby={}&size=50&has_aweme=0&has_live=0&avg_price=&avg_amount=&expr_score=".format(sort,orderby)
        responce = base().return_request(method="get", path=PathMessage.shop_search, data=para,tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]


        if orderby == "desc":

            amount = float("inf")
            volume = float("inf")
            expr_score = float("inf")

            if sort == "volume":
                for i in responce:
                    assert i["volume"] <= volume
                    volume = i["volume"]


            elif sort == "amount":
                for i in responce:
                    assert i["amount"] <= amount
                    amount = i["amount"]

            elif sort == "expr_score":
                for i in responce:
                    assert i["expr_score"] <= expr_score
                    expr_score = i["expr_score"]


            else:
                print("排序传参有误")
                raise False

        elif orderby == "asc":

            amount = -float("inf")
            volume = -float("inf")
            expr_score = -float("inf")

            if sort == "volume":
                for i in responce:
                    assert i["volume"] >= volume
                    volume = i["volume"]


            elif sort == "amount":
                for i in responce:
                    assert i["amount"] >= amount
                    amount = i["amount"]

            elif sort == "expr_score":
                for i in responce:
                    assert i["expr_score"] >= expr_score
                    expr_score = i["expr_score"]

            else:
                print("排序传参有误")
                raise False

        else:
            print("desc或asc传参有误")
            raise False


    @allure.description("""验证抖音小店库商品体验分筛选校验""")
    @allure.story('验证抖音小店库商品体验分筛选校验')
    @pytest.mark.parametrize('expr_score',["4.5-5.0","4.0-4.5","3.0-4.0","0-3.0"])
    @allure.title("抖音小店库商品体验分区间：{expr_score}")
    def test_shop_search_expr_score(self, get_token, get_host, expr_score):
        para = "page=1&big_category=&first_category=&keyword=&sort=volume&orderby=desc&size=50&has_aweme=0&has_live=0&avg_price=&avg_amount=&expr_score={}".format(expr_score)
        responce = base().return_request(method="get", path=PathMessage.shop_search, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
        expr_score_list = expr_score.split("-")
        for i in responce:
            print(float(expr_score_list[0]),float(expr_score_list[1]))
            assert i["expr_score"] >= float(expr_score_list[0]) and i["expr_score"] <= float(expr_score_list[1])



    @allure.story('验证抖音小店库近30日销售额、近30日客单价筛选与详情页校验')
    @allure.title("抖音小店库近30日销售额筛选区间：{avg_amount},近30日客单价区间：{avg_price},直播带货状态：{has_live},视频带货状态：{has_aweme}")
    @pytest.mark.parametrize('avg_amount', ["100-500", "500-1000", "2000-5000"])
    @pytest.mark.parametrize('avg_price', ["1-20", "50-100"])
    @pytest.mark.parametrize('has_live', [0,1])
    @pytest.mark.parametrize('has_aweme', [0,1])
    def test_shop_search_avg(self, get_token, get_host,avg_amount,avg_price,has_live,has_aweme):
        para = "page=1&big_category=&first_category=&keyword=&sort=volume&orderby=desc&size=50&has_aweme={}&has_live={}&avg_price={}&avg_amount={}&expr_score=".format(has_aweme,has_live,avg_price,avg_amount)
        responce = base().return_request(method="get", path=PathMessage.shop_search, data=para, tokens=get_token,hosts=get_host, )["response_body"]["data"]["list"]
        amount_list = avg_amount.split("-")
        price_list = avg_price.split("-")
        for i in responce:
            para = "shop_id=" + i["shop_id"]
            responce = base().return_request(method="get", path=PathMessage.shop_detail_info, data=para, tokens=get_token,
                                             hosts=get_host, )["response_body"]["data"]
            assert responce["total_amount"] >= int(amount_list[0]) and responce["total_amount"] <= int(amount_list[1])
            assert responce["avg_product_price"] >= int(price_list[0]) and responce["avg_product_price"] <= int(price_list[1])

