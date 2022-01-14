# -*- coding: utf-8 -*-
# @Time    : 2021/12/01
# @Author  : chenxubin
# @File    : conftest.py

import sys
import os
import pytest
import json
from Common.request import Request
from Common.mylog import Mylog
from Config.request_config import HostMessage
from Config.Consts import API_ENVIRONMENT,telephone,user_agent
from Config.path_config import PathMessage
from Common.Base import base


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if API_ENVIRONMENT == "release":
	host = HostMessage.release_host

if API_ENVIRONMENT == "debug":
	host = HostMessage.debug_host

if API_ENVIRONMENT == "stage":
	host = HostMessage.stage_host

#设置全局host变量
os.environ["host"] = host

if os.getenv("token")==None:
	os.environ["token"] = base().return_token(host)






@pytest.fixture(scope="session", autouse=True)
def get_token():
	"""
	备注：获取token方法已迁移至common/base.py,此处仅调用
	"""

	#
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

	return base().return_token(host)


@pytest.fixture(scope="session", autouse=True)
def get_host():

	return host














#
# if __name__ == '__main__':
#
#     daren()


