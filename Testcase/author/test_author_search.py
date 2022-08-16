# -*- coding: utf-8 -*-
# @Time    : 2022/8/9
# @Author  : youjiangyong
# @File    : test_author_search.py
import allure
import pytest
from Common.Base import base
from Config.path_config import PathMessage
import os, jsonpath
import time


@allure.feature('达人库')
@pytest.mark.flaky(reruns=5, reruns_delay=1)
class TestCase_Author_Search():

    sort = ['follower_count', 'inc_follower', 'aweme_digg_medium', 'aweme_digg_follower_ration', 'live_count_30','live_average_amount_30_v2', 'live_average_user_30', ]
    order_by = ['desc', 'asc']

    @allure.story('验证达人库排序是否正确')
    @pytest.mark.parametrize('sort', sort)
    @pytest.mark.parametrize('order_by', order_by)
    @allure.title("排序为{sort}，按{order_by}")
    def test_author_search_sort(self, get_token, get_host, sort, order_by):
        para = "page=1&reputation_level=-1&star_category=&star_sub_category=&goods_cat=&keyword=&gender=-1&age=&fans_gender=-1&fans_age=&follower_count=&product_platform=&province=&fans_province=&contact=0&is_commerce=0&is_live=0&is_sell_live=0&is_star_author=0&is_low_fans_high_gmv=0&is_brand_self_author=0&is_shop_author=0&verification_type=0&sort={}&order_by={}&size=52&similar_author_id=".format(sort,order_by)
        response = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)
        if sort == 'inc_follower':
            sort = "follower_incr"

        sort_list = jsonpath.jsonpath(response["response_body"], f'$.data.list[*].{sort}')
        assert response["status_code"] == 200
        assert len(response["response_body"]["data"]['list']) > 0
        if order_by == "desc":
            assert all(float(sort_list[i]) >= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))
        else:
            assert all(float(sort_list[i]) <= float(sort_list[i + 1]) for i in range(len(sort_list) - 1))



    @allure.story('验证达人库遍历达人和商品一级分类是否有返回数据')
    @pytest.mark.parametrize('star_category', base.return_star_category(os.getenv("host"), 1))
    @pytest.mark.parametrize('product_category', base.return_product_types(os.getenv("host"), 1))
    @allure.title("达人一级分类：{star_category},商品一级分类：{product_category}")
    def test_author_search_star_product_category(self, get_token, get_host, star_category, product_category):
        para = "page=1&reputation_level=-1&star_category={}&star_sub_category=&goods_cat={}&keyword=&gender=-1&age=&fans_gender=-1&fans_age=&follower_count=&product_platform=&province=&fans_province=&contact=0&is_commerce=0&is_live=0&is_sell_live=0&is_star_author=0&is_low_fans_high_gmv=0&is_brand_self_author=0&is_shop_author=0&verification_type=0&sort=inc_follower&order_by=desc&size=52&similar_author_id=".format(star_category[0],product_category[0])
        response = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                 tokens=get_token, hosts=get_host)
        time.sleep(0.1)
        # print(response)
        assert len(response["response_body"]["data"]["list"]) >= 0


    @allure.story('验证达人库直播达人筛选是否正确')
    @pytest.mark.parametrize('author_type', [1])
    def test_author_search_author_livetype(self, get_token, get_host, author_type):
        para = f"keyword=&author_type={author_type}&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=live_average_amount_30_v2&bring_product_brand=&order_by=desc&from=detail"
        response = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        print(response)
        for i in response:
            assert i["bring_live_products"] == 1

    @allure.story('验证达人库商品橱窗筛选是否正确')
    def test_author_search_is_commerce(self, get_token, get_host):
        para = "page=1&reputation_level=-1&star_category=&star_sub_category=&goods_cat=&keyword=&gender=-1&age=&fans_gender=-1&fans_age=&follower_count=&product_platform=&province=&fans_province=&contact=0&is_commerce=1&is_live=0&is_sell_live=0&is_star_author=0&is_low_fans_high_gmv=0&is_brand_self_author=0&is_shop_author=0&verification_type=0&sort=inc_follower&order_by=desc&size=52&similar_author_id="
        response = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        for i in response:
            assert i["commerce"] == 1


    @allure.story('验证达人库黑马达人筛选是否正确')
    def test_author_search_live_average_amount_30(self, get_token, get_host):
        para = "page=1&reputation_level=-1&star_category=&star_sub_category=&goods_cat=&keyword=&gender=-1&age=&fans_gender=-1&fans_age=&follower_count=&product_platform=&province=&fans_province=&contact=0&is_commerce=0&is_live=0&is_sell_live=0&is_star_author=0&is_low_fans_high_gmv=1&is_brand_self_author=0&is_shop_author=0&verification_type=0&sort=inc_follower&order_by=desc&size=52&similar_author_id="
        response = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        # print(response)
        for i in response:
            assert  i["live_average_amount_30_v2"] > 100000 and i["follower_count"] < 100000

    @allure.story('验证达人库性别筛选是否正确')
    @pytest.mark.parametrize('gender', [0, 1])
    @allure.title("性别为{gender}")
    def test_author_search_age_type(self, get_token, get_host,gender):
        para = "page=1&reputation_level=-1&star_category=&star_sub_category=&goods_cat=&keyword=&gender={}&age=&fans_gender=-1&fans_age=&follower_count=&product_platform=&province=&fans_province=&contact=0&is_commerce=0&is_live=0&is_sell_live=0&is_star_author=0&is_low_fans_high_gmv=1&is_brand_self_author=0&is_shop_author=0&verification_type=0&sort=inc_follower&order_by=desc&size=52&similar_author_id=".format(gender)
        response = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        for i in response:
            assert i["gender"] == gender

    @allure.story('验证达人库地区筛选是否正确')
    @pytest.mark.parametrize('city', base.return_city_3(os.getenv("host"), "河北省"))
    @allure.title("地区筛选条件为：{city}")
    def test_author_search_city_type(self, get_token, get_host, city):
        para = f"keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=%E6%B2%B3%E5%8C%97%E7%9C%81&city={city}&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=10&sort=inc_follower&bring_product_brand=&order_by=desc&from=detail"
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        print(responce)
        time.sleep(0.1)
        for i in responce:
            para = "author_id={}".format(i["author_id"])
            responce = base().return_request(method="get", path=PathMessage.author_detail_info, data=para,
                                  tokens=get_token, hosts=get_host)["response_body"]["data"]
            assert responce["city"] in city


    @allure.story('验证达人库认证类型筛选是否正确')
    @pytest.mark.parametrize('verification_type', [1, 2])
    @allure.title("认证筛选条件为：{verification_type}")
    def test_author_search_verification_type(self, get_token, get_host, verification_type):
        para1 = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type={}&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=10&sort=inc_follower&bring_product_brand=&order_by=desc&from=detail".format(verification_type)
        response = base().return_request(method="get", path=PathMessage.author_search, data=para1,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        for i in response:
            para1 = "author_id={}".format(i["author_id"])
            response = base().return_request(method="get", path=PathMessage.author_detail_info, data=para1,
                                  tokens=get_token, hosts=get_host)["response_body"]["data"]
            assert response["verification_type"] == verification_type

    @allure.story('验证达人库带货水平筛选是否有数据')
    @pytest.mark.parametrize('take_product_level', ["-30000", "30000-100000", "100000-1000000", "1000000-10000000", "10000000-"])
    def test_author_search_take_product_level(self, get_token, get_host, take_product_level):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level={}&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=live_average_amount_30_v2&bring_product_brand=&order_by=desc&from=detail".format(take_product_level)

        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 1

    @allure.story('验证达人库粉丝数筛选是否有数据')
    @pytest.mark.parametrize('follower_count', ["-10000", "10000-100000", "100000-1000000", "1000000-5000000", "5000000-10000000", "10000000-"])
    def test_author_search_follower_count(self, get_token, get_host, follower_count):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count={}&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=live_average_amount_30_v2&bring_product_brand=&order_by=desc&from=detail".format(follower_count)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)
        # print(responce)
        assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["list"]) > 1


    @allure.story('验证达人库带货方式是否有数据')
    @pytest.mark.parametrize('author_type', ["0", "1", "2"])
    @pytest.mark.parametrize('take_product_method', ["0", "1", "2"])
    def test_author_search_take_product_method(self, get_token, get_host, author_type, take_product_method):
        para = f"keyword=&author_type={author_type}&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method={take_product_method}&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=inc_follower&bring_product_brand=&order_by=desc&from=detail"
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)
        print(responce)
        # assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["list"]) > 1

    @allure.story('验证达人库直播平均场观筛选是否有数据')
    @pytest.mark.parametrize('live_watch_count', [ "-100000", "100000-1000000", "1000000-3000000", "3000000-5000000", "5000000-10000000","10000000-"])
    def test_author_search_live_watch_count(self, get_token, get_host, live_watch_count):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level&take_product_price=&reputation_level=-1&live_watch_count={}&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=live_average_amount_30_v2&bring_product_brand=&order_by=desc&from=detail".format(live_watch_count)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                             tokens=get_token, hosts=get_host)
        # print(responce)
        # assert responce["status_code"] == 200
        assert len(responce["response_body"]["data"]["list"]) > 1

    @allure.story('验证达人库直播平均场观筛选是否有数据')
    @pytest.mark.parametrize('live_average_amount_30_v2',
                             ["-500", "100000-1000000", "1000000-5000000", "5000000-10000000", "10000000-"])
    def test_author_search_live_average_amount_30_v2(self, get_token, get_host, live_average_amount_30_v2):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2={}&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=live_average_amount_30_v2&bring_product_brand=&order_by=desc&from=detail".format(
            live_average_amount_30_v2)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 1

    @allure.story('验证达人库直播GPM筛选是否有数据')
    @pytest.mark.parametrize('gpm', ["-5", "5-10", "10-30", "30-50", "50-100", "100-150", "150-"])
    def test_author_search_gpm(self, get_token, get_host, gpm):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm={}&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=live_average_amount_30_v2&bring_product_brand=&order_by=desc&from=detail".format(
            gpm)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 1

    @allure.story('验证达人库直播预期视频点赞数筛选是否有数据')
    @pytest.mark.parametrize('digg_count', ["-10000", "10000-50000", "50000-100000", "100000-1000000", "1000000-"])
    def test_author_search_digg_count(self, get_token, get_host, digg_count):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count{}=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=live_average_amount_30_v2&bring_product_brand=&order_by=desc&from=detail".format(
            digg_count)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)
        # print(responce)
        assert len(responce["response_body"]["data"]["list"]) > 1

    @allure.story('验证达人库星图达人筛选是否有数据')
    @pytest.mark.parametrize('is_star_author', ["1"])
    def test_author_search_single_tags(self, get_token, get_host, is_star_author):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author={}&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=inc_follower&bring_product_brand=&order_by=desc&from=detail".format(
            is_star_author)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"][0][
            "single_tags"]
        print(responce)
        assert len(responce) > 1

    @allure.story('验证达人库达人联系方式是否有数据')
    @pytest.mark.parametrize('contact', ["1"])
    def test_author_search_contact(self, get_token, get_host, contact):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact={}&similar_author_id=&page=1&size=50&sort=inc_follower&bring_product_brand=&order_by=desc&from=detail".format(
            contact)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        print(responce)
        assert len(responce) > 1

    @allure.story('验证达人库达人带货口碑筛选是否有数据')
    @pytest.mark.parametrize('reputation_level', ["-1", "0", "1", "2", "3"])
    def test_author_search_reputation_level(self, get_token, get_host, reputation_level):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=-30000&take_product_price=&reputation_level={}&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=inc_follower&bring_product_brand=&order_by=desc&from=detail".format(
            reputation_level)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        # print(responce)
        assert len(responce) > 1

    @allure.story('验证达人库达人品牌自播筛选是否有数据')
    @pytest.mark.parametrize('is_brand_self_author', ["1"])
    def test_author_search_is_brand_self_author(self, get_token, get_host, is_brand_self_author):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author={}&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=inc_follower&bring_product_brand=&order_by=desc&from=detail".format(
            is_brand_self_author)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        # print(responce)
        assert len(responce) > 1

    @allure.story('验证达人库达人店播筛选是否有数据')
    @pytest.mark.parametrize('is_shop_author', ["1"])
    def test_author_search_is_shop_author(self, get_token, get_host, is_shop_author):
        para = "keyword=&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author={}&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=inc_follower&bring_product_brand=&order_by=desc&from=detail".format(
            is_shop_author)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        # print(responce)
        assert len(responce) > 1

    @allure.story('验证达人库带货品牌搜索框是否有数据')
    @pytest.mark.parametrize('bring_product_brand', ["NIKE/耐克"])
    def test_author_search_bring_product_brand(self, get_token, get_host, bring_product_brand):
        para = "&author_type=0&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page=1&size=50&sort=inc_follower&bring_product_brand={}&order_by=desc&from=detail".format(
            bring_product_brand)
        responce = base().return_request(method="get", path=PathMessage.author_search, data=para,
                                         tokens=get_token, hosts=get_host)["response_body"]["data"]["list"]
        # print(responce)
        assert len(responce) > 1