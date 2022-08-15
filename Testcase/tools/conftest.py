# -*- coding: utf-8 -*-
# @Time    : 2022/8/12
# @Author  : zhangmin
import shutil
import hashlib
import datetime
from datetime import timedelta
import time,json,os
from dingtalkchatbot.chatbot import DingtalkChatbot
from Common.request import Request
from Config.Consts import user_agent
from Config.path_config import PathMessage
from Config.Consts import API_ENVIRONMENT,telephone,user_agent
from Common.mylog import Mylog
from Common.Base import base
from Config.path_config import PathMessage

def get_author(host):
    para = f'day_type=day&day={datetime.datetime.now().date() - datetime.timedelta(days=1)}&big_category=&first_category=&second_category=&sort=sales_volume&page=1&size=50&verification_type=&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=0'
    responce = \
    base().return_request(method="get", path=PathMessage.rank_sales, data=para, hosts=host)['response_body']['data'][
        'list']
    # print(responce)
    author_sales = []
    for i in responce:
        author_sales.append(i['author_id'])
    print(author_sales)
    return author_sales
