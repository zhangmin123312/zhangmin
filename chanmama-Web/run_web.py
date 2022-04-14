# -*- coding: utf-8 -*-
# @Time    : 2022/04/02
# @Author  : chenxubin
# @File    : run.py


import pytest
import os
from Config.config import Config

if __name__ == '__main__':

    args = ["./Testcase/", '-s', '--alluredir=./Report/result_data', '--clean-alluredir']
    # args = ["./Testcase/test_author.py",'-s', '-q']
    pytest.main(args)
    os.system(r"allure generate --clean ./Report/result_data -o ./Report/html ")
