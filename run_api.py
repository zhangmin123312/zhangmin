# -*- coding: utf-8 -*-
# @Time    : 2020/05/03
# @Author  : chenxubin
# @File    : run_api.py

import pytest
import os
from Common.Base import base


if __name__ == "__main__":
    args = ["./Testcase/rank/test_xuanpingku.py","-q","-s","--alluredir=./Report/allure-results","--clean-alluredir"]
    pytest.main(args)
    # base.dingding_suceces()
    # os.system(r"allure generate --clean ./Report/allure-results/ -o ./Report/html")

