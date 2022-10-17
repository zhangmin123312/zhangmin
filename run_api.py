# -*- coding: utf-8 -*-
# @Time    : 2021/12/02
# @Author  : chenxubin
# @File    : run_api.py

import pytest
import os
from Common.Base import base


if __name__ == "__main__":
    args = ["./Testcase","-n","auto","--dist=loadfile","-q","-s","--alluredir=./Report/allure-results","--clean-alluredir"]
    pytest.main(args)
    base.dingding()
    # os.system(r"allure generate --clean ./Report/allure-results/ -o ./Report/html")
