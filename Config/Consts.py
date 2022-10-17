# -*- coding: utf-8 -*-
# @Time    : 2021/12/1
# @Author  : chenxubin
# @File    : Consts.py

"""
全局变量
"""

# 接口全局配置,debug测试环境，stage环境，release线上环境
API_ENVIRONMENT = 'release'

# 获取token的账号
telephone = 18695682863
# 用于添加子账号
sub_telephone=13444444445

# 请求头的agent
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0"

# 佣金比例
commission_rate = ['10-', '20-', '30-', '40-', '50-']

# 商品来源
platform = ['jinritemai','taobao','tmall','jd','suning','kaola','weipinhui','yanxuan']

# 钉钉机器人配置
webhook = "https://oapi.dingtalk.com/robot/send?access_token=7627b69d751c1a29e516ff480f8bb1ab2fcf9e8017f470f31874366b45166af2"
secret = 'SEC0c7f019e6065f8728d29896448ee800b7fe78e6b98efcdf6e51826d196f8bd84'
at_phone = ["17350755951", "15760930206"]