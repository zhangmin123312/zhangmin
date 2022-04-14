# 导入封装好的页面对象
import allure
from Selenium.pom.Page import Page_Obj
# 导入独立的浏览器驱动对象
from Selenium.base.Init_Driver import Init_Driver
# 导入读取yml文件方法
# from Selenium.base.Read_Data import Read_Yaml_Data
import time


# def read_test_data():
#     list_data = []
#     test_Data = Read_Yaml_Data("login").get("User")
#     for i in test_Data.keys():
#         list_data.append((i,test_Data.get(i).get("user"),test_Data.get(i).get("psd"),test_Data.get(i).get("except")))
#     print(list_data)
#     return list_data


class Test_Login:

    def setup_method(self):
        # 初始化driver对象
        self.driver = Init_Driver('google',1)

    def teardown_method(self):
        # 退出driver对象
        self.driver.quit()

    @allure.story("验证密码登录")
    def test_login(self):
        try:
            Page_Obj(self.driver).go_to_login().password_login(18695682863, 123456)
            time.sleep(1)
        except:
            with allure.step('添加失败截图...'):
                allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            raise False

    @allure.story("验证忘记密码")
    def test_forget_password(self):
        try:
            # 忘记密码流程
            Page_Obj(self.driver).go_to_login().forget_password(18046304924, 123456)
            time.sleep(1)
        except:
            with allure.step('添加失败截图...'):
                allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            raise False

    @allure.story("验证验证码登录")
    def test_code_login(self):
        # 验证码登录流程
        try:
            Page_Obj(self.driver).go_to_login().code_login(18046304924, 123456)
            time.sleep(1)
        except:
            with allure.step('添加失败截图...'):
                allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            raise False


if __name__ == "__main__":
    pass
