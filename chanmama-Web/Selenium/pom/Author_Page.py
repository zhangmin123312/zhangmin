# -*- coding: utf-8 -*-
"""
  @desc: 蝉妈妈抖音主页
  @author: chenxubin
  @file: Author_Page.py
  @date: 2022/04/08
"""
import time
import Selenium.pom
from Selenium.base.BasePage import BasePage


class Author_Page(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)  # Base类的初始化方法
        try:
            self.click_alert()
        except:
            pass

    def is_author(self):
        """
        密码登录操作
        """
        assert self.get_text(['css', '.cp.fs16.font-weight-500.cursor-pointer']) == "智能达人匹配"

    def search_author(self):
        self.input_data(['css', '#e2e-common-search-input'], '罗永浩')
        self.click_element(['css', '#e2e-common-search-btn'])
        seacher_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
        # seacher_text = self.scroll_find_element(['css','.link.no'],0)
        assert seacher_text == '罗永浩'

    def good_type(self):
        for i in self.locateElements(
                ['xpath', ".//*[@id='app']/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div[1]/div[2]/div/div/div"]):
            i.click()
            time.sleep(3)
            responce_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
            assert len(responce_text) > 0

    def star_type(self):
        self.click_element(['css', '.open-icon.flex.align-items-center.justify-content-center>span'])
        for i in self.locateElements(['xpath',
                                      "html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div[2]/div[2]/div/div/div/div"]):
            i.click()
            time.sleep(3)
            responce_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
            assert len(responce_text) > 0

    def Brand_self_broadcast(self):
        self.click_element(['css', 'div > label > span.el-checkbox__label'], 0)
        responce_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
        assert len(responce_text) > 0

    def author_message_shop(self):
        self.click_element(['css', 'div > label > span.el-checkbox__label'], 1)
        responce_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
        assert len(responce_text) > 0

    def talent_broadcast(self):
        self.click_element(['css', 'div > label > span.el-checkbox__label'], 2)
        responce_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
        assert len(responce_text) > 0

    def author_message_star_map(self):
        self.click_element(['css', 'div > label > span.el-checkbox__label'], 3)
        responce_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
        assert len(responce_text) > 0

    def author_message_dark_horse(self):
        self.click_element(['css', 'div > label > span.el-checkbox__label'], 4)
        responce_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
        assert len(responce_text) > 0

    def author_message_product_window(self):
        self.click_element(['css', 'div > label > span.el-checkbox__label'], 5)
        responce_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
        assert len(responce_text) > 0

    def author_message_show_news(self):
        self.click_element(['css', 'div > label > span.el-checkbox__label'], 6)
        responce_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
        assert len(responce_text) > 0

    def author_have_contact_information(self):
        self.click_element(['css', 'div > label > span.el-checkbox__label'], 7)
        responce_text = self.get_text(['css', '.text-decoration-none.c333.link-hover.cursor-pointer.ellipsis-1'], 0)
        assert len(responce_text) > 0
