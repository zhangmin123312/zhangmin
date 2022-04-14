# -*- coding: utf-8 -*-
"""
  @desc: 蝉妈妈抖音主页
  @author: chenxubin
  @file: test_author.py
  @date: 2022/04/08
"""
import allure
import pytest
import os
from Selenium.pom.Page import Page_Obj
# 导入独立的浏览器驱动对象
# from Selenium.base.Init_Driver import Init_Driver

class Test_Login():

    def setup_class(self):
        pass
        # 初始化driver对象
        # self.driver = Init_Driver("google")
        # 采用密码登录
        # Page_Obj(self.driver).go_to_login().password_login(18695682863, 123456)

    def teardown_class(self):
        pass
        # 退出driver对象
        # self.driver.quit()

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @allure.story("验证搜索框搜索功能")
    def test_search_author(self, browser):
        Page_Obj(browser).go_to_author().search_author()

    @allure.story("验证商品分类筛选是否有数据")
    def test_click_goods_type(self, browser):
        Page_Obj(browser).go_to_author().good_type()

    @allure.story("验证达人分类筛选是否有数据")
    def test_click_star_type(self, browser):
        Page_Obj(browser).go_to_author().star_type()

    @allure.story("验证品牌自播筛选是否有数据")
    def test_click_Brand_self_broadcast(self, browser):
        Page_Obj(browser).go_to_author().Brand_self_broadcast()

    @allure.story("验证店播筛选是否有数据")
    def test_author_message_shop(self, browser):
        Page_Obj(browser).go_to_author().author_message_shop()

    @allure.story("验证达人播筛选是否有数据")
    def test_talent_broadcast(self, browser):
        Page_Obj(browser).go_to_author().talent_broadcast()

    @allure.story("验证星图达人筛选是否有数据")
    def test_author_message_star_map(self, browser):
        Page_Obj(browser).go_to_author().author_message_star_map()

    @allure.story("验证黑马筛选是否有数据")
    def test_author_message_dark_horse(self, browser):
        Page_Obj(browser).go_to_author().author_message_dark_horse()

    @allure.story("验证商品橱窗筛选是否有数据")
    def test_author_message_product_window(self, browser):
        Page_Obj(browser).go_to_author().author_message_product_window()

    @allure.story("验证商品橱窗筛选是否有数据")
    def test_author_message_show_news(self, browser):
        Page_Obj(browser).go_to_author().author_message_show_news()

    @allure.story("验证商品橱窗筛选是否有数据")
    def test_author_have_contact_information(self, browser):
        Page_Obj(browser).go_to_author().author_have_contact_information()


if __name__ == "__main__":
    pass
