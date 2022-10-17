# -*- coding: utf-8 -*-
# @Time    : 2021/12/01
# @Author  : chenxubin
# @File    : conftest.py

import sys
import os,time
import pytest
import json
from Common.request import Request
from Common.mylog import Mylog
from Config.request_config import HostMessage
from Config.Consts import API_ENVIRONMENT,telephone,user_agent
from Config.path_config import PathMessage
from Common.Base import base
from filelock import FileLock


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if API_ENVIRONMENT == "release":
	host = HostMessage.release_host

if API_ENVIRONMENT == "debug":
	host = HostMessage.debug_host

if API_ENVIRONMENT == "stage":
	host = HostMessage.stage_host

#设置全局host,token变量
os.environ["host"] = host
# token = base().return_token(host)
# os.environ["token"] = token

if os.getenv("token") is None:
	os.environ["token"] = base().return_token(host)




@pytest.fixture(scope="session", autouse=True)
def get_token():
	"""
	备注：获取token方法已迁移至common/base.py,此处仅调用
	"""
	
	# data = {
	# "username": str(telephone),
	# "timeStamp": "1620637379378",
	# "appId": "10004",
	# "grant_type": "password",
	# "password": "e10adc3949ba59abbe56e057f20f883e"}
	#
	# data = json.dumps(data)
	#
	# header = {"User-Agent": user_agent,}
	#
	# try:
	#
	# 	token = Request.post_request(url=host + PathMessage.token[0], headers=header, data=data)['response_body']["data"]["token"]
	#
	# except:
	# 	print("获取token失败")
	# 	Mylog.error("获取token失败")
	# 	raise False

	if os.getenv("token") is None:
		os.environ["token"] = base().return_token(host)
	return os.getenv("token")


@pytest.fixture(scope="session", autouse=True)
def get_host():
	return host

def pytest_terminal_summary(terminalreporter):
	"""
	收集测试结果
	"""

	_PASSED = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
	_ERROR = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
	_FAILED = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
	_SKIPPED = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
	_TOTAL = terminalreporter._numcollected
	_TIMES = round(time.time() - terminalreporter._sessionstarttime, 2)
	times = base.second_switch(_TIMES)

	send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
	print(send_time, _TOTAL, _PASSED, _FAILED, _SKIPPED, _ERROR, times)
	os.environ["REPORT"] = "蝉妈妈自动化运行情况：\n发送时间: {},\n用例总数: {},\n通过用例数: {},\n失败用例数: {},\n跳过用例数: {},\n错误用例数: {},\n总用时: {}".format(send_time, _TOTAL, _PASSED, _FAILED, _SKIPPED, _ERROR, times)














#
# if __name__ == '__main__':
#
#     daren()


