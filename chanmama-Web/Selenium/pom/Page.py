# -*- coding: utf-8 -*-
# @Time    : 2019/12/27
# @Author  : chenlinjie
# @File    : Page.py
import time
from Selenium.pom.Login_Page import Login_Page
from Selenium.base.BasePage import BasePage
from Selenium.pom.Author_Page import Author_Page

class Page_Obj(BasePage):

    def __init__(self,driver):
        BasePage.__init__(self, driver)
        #进入登录页
        # self.open_url('https://sv-test.cds8.cn/douyin')
        self.open_url('https://sv-stage.cds8.cn/douyin')
        # #取消双11活动弹窗
        try:
            # self.click_element(["css", ".item-svg.cursor-pointer.svg-icon.svg-fill"], 1)
            self.click_alert()
            print("弹框清除")
        except:
            print("无弹窗或者弹框失败")


    def go_to_login(self):

        self.click_element(['css', '#e2e-login-btn'])
        return Login_Page(self.driver)


    def go_to_author(self):
        """
        点击跳转到达人相关页
        """
        self.click_element(["css", '.flex.align-items-center.h100p.link-box.fs14'], 0)
        return Author_Page(self.driver)





