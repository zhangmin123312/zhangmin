# -*- coding: utf-8 -*-

"""
  @desc: 登录页PO
  @author: chenxubin
  @file: Search_Page.py
  @date: 2019/12/12
"""
import time
import Selenium.pom
from Selenium.base.BasePage import BasePage


class Login_Page(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)  # Base类的初始化方法

    def password_login(self, user, psd):
        """
        密码登录操作
        """
        self.click_element(["css", 'li.is-active'])
        self.input_data(["css", 'input.el-input__inner[type=text]'], user)
        self.input_data(["css", 'input.el-input__inner[type=password]'], psd)
        self.click_element(["css", '.el-button[type=button]'])
        time.sleep(1)
        try:
            self.click_element(["css", ".item-svg.cursor-pointer.svg-icon.svg-fill"])
            print("弹框清除")
        except:
            print("无弹窗或清除失败")
        # assert self.exit_element(['css', '#e2e-login-avatar'])
        return self.driver

    def code_login(self, user, code):
        """
        验证码登录
        """
        self.click_element(['css', '.el-menu-item'], 1)
        self.input_data(['css', '.el-input__inner'], user, 0)
        self.click_element(['css', '.flex.align-items-center.justify-content-center.fs14.cursor-pointer>div'])
        self.input_data(['css', 'input[placeholder=请输入验证码]'], code)
        self.click_element(["css", '.el-button[type=button]'])
        time.sleep(1)
        try:
            self.click_element(["css", ".item-svg.cursor-pointer.svg-icon.svg-fill"])
            print("弹框清除")
        except:
            print("无弹窗或清除失败")
        assert self.exit_element(['css', '#e2e-login-avatar']) == True

    def forget_password(self, user, new_psd):
        """
        忘记密码
        """
        self.click_element(["css", 'li.is-active'])
        self.click_element(
            ["xpath", '//*[@id="app"]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/form/div[3]/div/div/div[2]'])
        self.input_data(["css", 'input[placeholder=请输入手机号]'], user)
        self.click_element(["css", "div.get-code"])
        time.sleep(1)
        self.input_data(["css", 'input[placeholder=请输入验证码]'], "123456")
        self.click_element(["css", 'button[type=button].el-button'])
        self.wait_element(".login-form")
        self.input_data(["css", "[type=password][placeholder=请输入新密码]"], new_psd)
        self.input_data(["css", "[type=password][placeholder=再次输入确认新密码]"], new_psd)
        self.click_element(["css", '.el-form-item__content [type=button]'])
        self.password_login(user, new_psd)
