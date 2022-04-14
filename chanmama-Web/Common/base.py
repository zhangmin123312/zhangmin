# import time
#
# import allure
#
#
# def try_except(driver,action):
#     try:
#         action
#         time.sleep(1)
#     except:
#         with allure.step('添加失败截图...'):
#             allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
#             raise False