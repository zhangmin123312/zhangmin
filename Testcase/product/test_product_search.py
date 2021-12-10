# -*- coding: utf-8 -*-
# @Time    : 2021/12/9
# @Author  : linchenzhen
# @File    : test_product_search.py
import allure
import pytest

from Common.Base import base
from Config.path_config import PathMessage
from Config.Consts import platform
import os,jsonpath,json


@allure.feature('选品库')
# @pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Product_Search():

    day_type=[1,7,30]
    sort=['duration_volume','tb_max_commission_rate','duration_pv','duration_live_volume','duration_aweme_volume']
    order_by=["desc","asc"]
    tb_max_commission_rate=['0-5','5-10','10-20','20-30','30-40','40-50','50-60']
    duration_volume=['100-','200-','300-','500-','1000-','2000-','3000-','5000-','10000-']
    day_pv_count=['500-','1000-','2000-','3000-','5000-','10000-','20000-','40000-','60000-','80000-']
    price=['50-100','100-','-100','50.5-100.5','0-9.9']

    @allure.description("""验证选品库昨日、7天、30天是否有数据""")
    @pytest.mark.parametrize('day_type',day_type )
    @allure.title("验证选品库{day_type}是否有数据")
    def test_product_search_day_type(self,get_token,get_host,day_type):
        para={"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":"","duration_volume":"","big_category":"","first_category":"","second_category":"","platform":"","sort":self.sort[0],"order_by":self.order_by[0],"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证选品库昨日、7天、30天按分类升序降序，排序结果是否正确""")
    @pytest.mark.parametrize('sort', sort)
    @pytest.mark.parametrize('day_type', day_type)
    @pytest.mark.parametrize('order_by', order_by)
    @allure.title("验证选品库日期类型：{day_type}，按{sort}、{order_by}排序是否正确")
    def test_product_search_sort(self,get_token,get_host,day_type,sort,order_by):
        para={"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":"","duration_volume":"","big_category":"","first_category":"","second_category":"","platform":"","sort":sort,"order_by":order_by,"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        sort_list=jsonpath.jsonpath(response["response_body"],f'$.data.list[*].{sort}')
        assert response["status_code"]==200
        if order_by=="desc":
            assert all(float(sort_list[i]) >= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))
        else:
            assert all(float(sort_list[i]) <= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))

    @allure.description("""验证选品库昨日、7天、30天按转化率排序是否正确""")
    @pytest.mark.parametrize('sort', ['duration_product_rate'])
    @pytest.mark.parametrize('day_type', day_type)
    @pytest.mark.parametrize('order_by', order_by)
    @allure.title("验证选品库日期类型：{day_type}按转化率{order_by}排序是否正确")
    def test_product_search_sort_duration_product_rate(self,get_token,get_host,day_type,sort,order_by):
        para={"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":"500-","duration_volume":"100-","big_category":"","first_category":"","second_category":"","platform":"","sort":sort,"order_by":order_by,"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        sort_list=jsonpath.jsonpath(response["response_body"],f'$.data.list[*].{sort}')
        assert response["status_code"]==200
        if order_by=="desc":
            assert all(float(sort_list[i]) >= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))
        else:
            assert all(float(sort_list[i]) <= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))

    @allure.description("""验证选品库遍历商品一级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),1))
    @pytest.mark.parametrize('day_type', day_type)
    @allure.title("选品库日期：{day_type},商品一级分类：{product_type}")
    def test_product_search_big_category(self,get_token,get_host,product_type,day_type):
        para={"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":"","duration_volume":"","big_category":product_type[0],"first_category":"","second_category":"","platform":"","sort":self.sort[0],"order_by":self.order_by[0],"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证选品库遍历商品二级分类是否有返回数据""")
    @pytest.mark.parametrize('product_type',base.return_product_types(os.getenv("host"),2))
    @pytest.mark.parametrize('day_type', day_type)
    @allure.title("选品库日期：{day_type},商品二级分类：{product_type}")
    def test_product_search_big_category(self,get_token,get_host,product_type,day_type):
        para={"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":"","duration_volume":"","big_category":product_type[0],"first_category":product_type[1],"second_category":"","platform":"","sort":self.sort[0],"order_by":self.order_by[0],"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        assert response["status_code"]==200
        assert len(response["response_body"]["data"]["list"]) > 0

    @allure.description("""验证选品库昨日、7天、30天，按商品来源筛选""")
    @pytest.mark.parametrize('platform',platform[:5])
    @pytest.mark.parametrize('day_type', day_type)
    @allure.title("选品库日期:day_type,商品来源：{platform}")
    def test_product_search_platform(self,get_token,get_host,day_type,platform):
        para={"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":"","duration_volume":"","big_category":"","first_category":"","second_category":"","platform":platform,"sort":self.sort[0],"order_by":self.order_by[0],"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        platform_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].platform')
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        assert all(value == platform for value in platform_list)

    @allure.description("""验证选品库昨日、7天、30天，按佣金比例筛选""")
    @pytest.mark.parametrize('tb_max_commission_rate',tb_max_commission_rate)
    @pytest.mark.parametrize('day_type', day_type)
    @allure.title("选品库日期:day_type,佣金比例：{tb_max_commission_rate}")
    def test_product_search_commission_rate(self,get_token,get_host,day_type,tb_max_commission_rate):
        para={"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":tb_max_commission_rate,"day_pv_count":"","duration_volume":"","big_category":"","first_category":"","second_category":"","platform":"","sort":self.sort[0],"order_by":self.order_by[0],"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        tb_max_commission_rate_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].tb_max_commission_rate')
        commission_rate=tb_max_commission_rate.split("-")
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        assert all(float(commission_rate[0])<=float(value)<=float(commission_rate[1]) for value in tb_max_commission_rate_list)

    @allure.description("""验证选品库昨日、7天、30天，按抖音销量筛选""")
    @pytest.mark.parametrize('duration_volume',duration_volume)
    @pytest.mark.parametrize('day_type', day_type)
    @allure.title("选品库日期:day_type,抖音销量：{duration_volume}")
    def test_product_search_duration_volume(self,get_token,get_host,day_type,duration_volume):
        para={"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":"","duration_volume":duration_volume,"big_category":"","first_category":"","second_category":"","platform":"","sort":self.sort[0],"order_by":self.order_by[0],"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        duration_volume_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].duration_volume')
        duration_volume=duration_volume.replace("-",'')
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        assert all(value>int(duration_volume) for value in duration_volume_list)

    @allure.description("""验证选品库昨日、7天、30天，按昨日抖音浏览量筛选""")
    @pytest.mark.parametrize('day_pv_count',day_pv_count)
    @pytest.mark.parametrize('day_type', day_type)
    @allure.title("选品库日期:day_type,昨日抖音浏览量：{day_pv_count}")
    def test_product_search_duration_volume(self,get_token,get_host,day_type,day_pv_count):
        para={"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":day_pv_count,"duration_volume":"","big_category":"","first_category":"","second_category":"","platform":"","sort":self.sort[0],"order_by":self.order_by[0],"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        day_pv_count_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].day_pv_count')
        day_pv_count=day_pv_count.replace("-",'')
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        assert all(value>int(day_pv_count) for value in day_pv_count_list)

    @allure.description("""验证选品库昨日、7天、30天，按价格区间筛选""")
    @pytest.mark.parametrize('price',price)
    @pytest.mark.parametrize('day_type', day_type)
    @allure.title("选品库日期:day_type,价格区间：{price}")
    def test_product_search_commission_rate(self,get_token,get_host,day_type,price):
        para={"keyword":"","keyword_type":"","page":1,"price":price,"size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":"","duration_volume":"","big_category":"","first_category":"","second_category":"","platform":"","sort":self.sort[0],"order_by":self.order_by[0],"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        price_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].price')
        price=price.split("-")
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        assert all(float(price[0])<=float(value) for value in price_list if len(price[0])!=0)
        assert all(float(value)<=float(price[1]) for value in price_list if len(price[1])!=0)

    @allure.description("""验证选品库昨日、7天、30天，按是否有优惠券筛选""")
    @pytest.mark.parametrize('filter_coupon',[1])
    @pytest.mark.parametrize('day_type', day_type)
    @allure.title("选品库日期:day_type，按有优惠券搜索")
    def test_product_search_commission_rate(self,get_token,get_host,day_type,filter_coupon):
        para={"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":filter_coupon,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":"","duration_volume":"","big_category":"","first_category":"","second_category":"","platform":"","sort":self.sort[0],"order_by":self.order_by[0],"day_type":day_type,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(para),tokens=get_token,hosts=get_host, )
        have_coupon_list = jsonpath.jsonpath(response["response_body"], '$.data.list[*].have_coupon')
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]["list"]) > 0
        assert all(value for value in have_coupon_list)