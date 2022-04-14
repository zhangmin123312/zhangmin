# -*- coding: utf-8 -*-
"""
  @desc: page object测试基类
  @author: chenxubin
  @file: base_page.py
  @date: 2019/7/11
"""
import json
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



class BasePage(object):
    # 初始化方法
    def __init__(self, driver):
        # 创建浏览器对象
        self.driver = driver
        # 设置隐式等待
        self.driver.implicitly_wait(5)
        # 设置浏览器的最大化
        self.driver.maximize_window()

    def open_url(self, url):
        # 请求指定站点
        self.driver.get(url)
        time.sleep(1)

    def close(self):
        # 退出浏览器
        time.sleep(1)
        print("close有生效")
        self.driver.quit()

    def current_url(self):
        # 获取当前的url
        return self.driver.current_url

    def locateElement(self, locate):
        # 判断定位方式并调用相关方法
        el = None
        if locate[0] == 'id':
            el = self.driver.find_element_by_id(locate[1])
        elif locate[0] == 'name':
            el = self.driver.find_element_by_name(locate[1])
        elif locate[0] == 'class':
            el = self.driver.find_element_by_class_name(locate[1])
        elif locate[0] == 'text':
            el = self.driver.find_element_by_link_text(locate[1])
        elif locate[0] == 'xpath':
            el = self.driver.find_element_by_xpath(locate[1])
        elif locate[0] == 'css':
            el = self.driver.find_element_by_css_selector(locate[1])
        # 如果el不为None,则返回
        if el is not None:
            return el


    def locateElements(self, locate):
        # 获取elements并调用相关方法
        el = None
        if locate[0] == 'id':
            el = self.driver.find_elements_by_id(locate[1])
        elif locate[0] == 'name':
            el = self.driver.find_elements_by_name(locate[1])
        elif locate[0] == 'class':
            el = self.driver.find_elements_by_class_name(locate[1])
        elif locate[0] == 'text':
            el = self.driver.find_elements_by_link_text(locate[1])
        elif locate[0] == 'xpath':
            el = self.driver.find_elements_by_xpath(locate[1])
        elif locate[0] == 'css':
            el = self.driver.find_elements_by_css_selector(locate[1])
        # 如果el不为None,则返回
        if el is not None:
            return el


    # 指定对某一元素的点击操作
    def click_element(self, locate,elemrnts_num=None):
        # 调用定位方法进行元素定位
        if elemrnts_num is not None:
            el = self.locateElements(locate)[elemrnts_num]
            el.click()
        else:
            el = self.locateElement(locate)
            # 执行点击操作
            el.click()
        time.sleep(1)

    # 对指定的元素进行数据输入
    def input_data(self, locate, data,elemrnts_num=None):
        # 对输入框输入值
        if elemrnts_num is not None:
            el = self.locateElements(locate)[elemrnts_num]
            el.click()
            el.clear()
            el.send_keys(data)
        el = self.locateElement(locate)
        # 执行输入操作
        el.click()
        el.clear()
        el.send_keys(data)

    # 获取指定元素的文本内容
    def get_text(self, locate,elemrnts_num=None):
        # 调用定位元素的text
        if elemrnts_num is not None:
            el = self.locateElements(locate)[elemrnts_num]
            return el.text
        else:
            el = self.locateElement(locate)
        return el.text

    # 获取指定元素的属性值
    def get_attr(self, locate, data):
        # 调用定位方法进行元素定位
        el = self.locateElement(locate)
        return el.get_attribute(data)

    # 显式等待
    def wait_element(self, element):
        ele = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
        return ele

    # 判断弹框
    def is_alert(self):
        """
        切换window窗口,切换一次后退出
        :return: 无
        """
        curHandle = self.driver.current_window_handle  # 获取当前窗口聚丙
        allHandle = self.driver.window_handles  # 获取所有聚丙
        print(len(allHandle))
        for h in allHandle:
            if h != curHandle:
                self.driver.switch_to.window(h)  # 切换聚丙，到新弹出的窗口
                break

    # 获取cookies保存到Data文件
    def save_cookie(self):
        cookies = self.driver.get_cookies()
        json_cookies = json.dumps(cookies)
        with open(r'./Data/cookies_csnd.json', 'w') as f:
            f.write(json_cookies)

    # 读取文件中的cookie
    def add_cookie(self):
        self.driver.delete_all_cookies()
        dict_cookies = {}
        with open('d:/cookies.json', 'r', encoding='utf-8') as f:
            list_cookies = json.loads(f.read())
        for i in list_cookies:
            self.driver.add_cookie(i)

    def exit_element(self,locate):
        is_re = True
        try:
            self.locateElement(locate)
            return is_re
        except:
            is_re = False
            return is_re


    def click_alert(self,locate=["css", ".item-svg.cursor-pointer.svg-icon.svg-fill"]):
        self.click_element(locate)


    def scroll_find_element(self,locate,elemrnts_num=None):
        """滑动查找元素 找到就退出"""
        scroll = 0
        while scroll < 9999:
            try:
                text = self.get_text(locate,elemrnts_num)
                if text:
                    return text
            except NoSuchElementException:
                time.sleep(1)
                js = "document.documentElement.scrollTop={0}".format(scroll)
                self.driver.execute_script(js)
                scroll += 10



if __name__ == '__main__':
    pass
