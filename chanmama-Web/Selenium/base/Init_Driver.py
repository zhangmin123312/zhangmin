# -*- coding: utf-8 -*-
"""
  @desc: page object测试基类
  @author: chenxubin
  @file: init_Driver.py
  @date: 2019/12/11
"""

from selenium import webdriver


def Init_Driver(type,environment="locale"):

    if type == "google":
        if environment == "locale":
            #本地的谷歌浏览器驱动
            driver = webdriver.Chrome(executable_path='./Selenium/base/chromedriver')
            return driver
        else:
            #服务器远程运行谷歌浏览器
            driver = webdriver.Remote(
                command_executor='http://10.1.153.101:4444/wd/hub',
                # desired_capabilities={'browserName': 'chrome'}
                desired_capabilities={'platform': 'ANY',
                                      'browserName': 'chrome',
                                      'version': '',
                                      'javascriptEnabled': True})
            return driver


    elif type == "firefox":

        if environment == "locale":
            #本地的火狐浏览器驱动
            driver = webdriver.Firefox()
            return driver

        else:
            # 服务器远程运行火狐浏览器
            driver = webdriver.Remote(
                command_executor='http://10.1.153.101:4444/wd/hub',
                # desired_capabilities={'browserName': 'chrome'}
                desired_capabilities={'platform': 'ANY',
                                      'browserName': 'firefox',
                                      'version': '',
                                      'javascriptEnabled': True})
            return driver
