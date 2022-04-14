# -*- coding: utf-8 -*-
"""
  @desc: 读取yaml文件数据
  @author: chenxubin
  @file: Read_Data.py
  @date: 2019/12/11
"""

import yaml
import os

def Read_Yaml_Data(file_name):
    #定义yml文件路径
    file_path = os.getcwd() + os.sep + "Selenium" + os.sep + "Data" + os.sep + file_name + ".yml"
    #解析yml文件数据
    with open(file_path,"r") as f:
        return yaml.load(f,Loader=yaml.FullLoader)
