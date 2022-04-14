# -*- coding: utf-8 -*-
# @Time    : 2022/04/02
# @Author  : chenxubin
# @File    : run.py


import pytest
import os
from Config.config import Config

if __name__ == '__main__':

    args = ["./Testcase", "-q", "-s", "--alluredir=./Report/allure-results","--clean-alluredir"]
    pytest.main(args)
    # args = ["./Testcase/", '-s', '--alluredir=./Report/result_data', '--clean-alluredir']
    # os.system(r"allure generate --clean ./Report/result_data -o ./Report/html ")
