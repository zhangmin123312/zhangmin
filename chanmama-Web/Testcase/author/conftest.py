import pytest
import os
import allure
from Selenium.pom.Page import Page_Obj
# 导入独立的浏览器驱动对象
from Selenium.base.Init_Driver import Init_Driver




browser_driver = None
# 用例失败后自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(browser_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(browser_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)



@pytest.fixture(scope='class')
def browser():
    global browser_driver
    if browser_driver is None:
        browser_driver = Init_Driver("google",1)
        browser_driver = Page_Obj(browser_driver).go_to_login().password_login(18695682863, 123456)
    yield browser_driver
    browser_driver.quit()



