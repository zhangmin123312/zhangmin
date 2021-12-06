# -*- coding: utf-8 -*-
# @Time    : 2021/12/01
# @Author  : chenxubin
# @File    : common_config.py
"""
接口路径配置文件
"""

class PathMessage:

    #token路径
    token = ["/v1/access/token"]

    #商品分类路径
    product_path = ["/v1/product/category?type=all"]

    # 达人分类路径
    star_category = ["/v1/common/starCategory"]

    # 选品库
    xuan_ping_ku = ["/v1/product/search"]

    #抖音销量榜
    quan_tian_xiao_liang_bang = ["/v1/douyin/live/star/live/widget"]

    #成长达人榜
    cheng_zhang_da_ren_bang = ["/v1/authorRank/bangNew"]

    #行业达人榜
    hang_ye_da_ren_bang = ["/v1/authorRank/bangNew"]

    #商品品牌榜
    brand_rank = ["/v1/brand/rank"]

























if __name__ == '__main__':

    pass

# print(da_ren_xiang_qing)

