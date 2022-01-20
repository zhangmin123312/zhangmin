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
    product_path = ["/v1/product/category"]

    # 达人分类路径
    star_category = ["/v1/common/starCategory"]

    # 地域分类
    common_area = ["/v1/common/area"]

    #成长达人榜
    cheng_zhang_da_ren_bang = ["/v1/authorRank/bangNew"]

    #商品品牌榜
    brand_rank = ["/v1/brand/rank"]

    #抖音销量榜
    rank_yesterdaySaleRank = ["/v1/home/rank/yesterdaySaleRank"]

    #抖音热推榜
    rank_yesterdayHotRank = ["/v1/home/rank/yesterdayHotRank"]

    #实时销量榜
    rank_liveRank = ["/v1/home/rank/liveRank"]

    #抖音小店榜
    rank_specialtyToday = ["/v1/home/rank/specialtyToday"]

    #小店库
    shop_search = ["/v2/shop/search"]

    #小店详情页
    shop_detail_info = ["/v1/shop/detail/info"]

    #选品库
    product_search = ["/v2/product/search"]
    
    #品牌库
    brand_search = ["/v2/home/brand/search"]

    #品牌详情页
    brand_detail_info = ["/v1/brand/detail/info"]

    #品牌详情页-小店分析
    brand_detail_chart = ["/v1/brand/detail/chart"]

    #品牌详情页-观众分析
    brand_detail_authorFansAnalysis = ["/v2/brand/detail/authorFansAnalysis"]

    #全天销量榜
    rank_allDayRank = ["/v1/home/rank/allDayRank"]

    #涨粉达人榜
    author_rank_fans = ["/v1/home/author/rank/fans"]

    #达人详情页info
    author_detail_info = ["/v1/author/detail/info"]

    # 商品分享日榜
    authorRank_starDailyRank = ["/v1/authorRank/starDailyRank"]

    # 商品分享周榜和月榜
    authorRank_starRank = ["/v1/authorRank/starRank"]

    #达人榜
    authorRank_bangNew = ["/v1/authorRank/bangNew"]

    # 带货视频榜
    rank_productAweme = ['/v1/home/rank/productAweme']

    # 热门视频榜
    rank_hotAweme = ["/v1/home/rank/hotAweme"]

    # 直播-今日带货榜
    rank_official_daily = ["/v1/douyin/live/rank/official/daily"]

    # 直播-带货小时榜
    rank_official = ["/v1/douyin/live/rank/official"]

    # 直播-带货小时榜-榜点
    rank_official_hours = ["/v1/douyin/live/rank/official/hours"]

    # 直播-直播实时热榜
    rank_top = ["/v1/douyin/live/rank/live/top"]

    # 直播-抖音官方小时榜
    rank_soundbyte = ["/v1/douyin/live/rank/soundbyte"]

    # 直播-抖音官方小时榜-榜点
    rank_soundbyte_hours = ["/v1/douyin/live/rank/soundbyte/hours"]

    # 直播-预热视频分析
    live_warm = ["/v1/douyin/live/warm"]

    # 直播-达人带货榜
    rank_sales = ["/v1/douyin/live/rank/author/sales"]

    # 达人详情-直播概览
    author_liveAnalysisV2 = ["/v1/author/detail/liveAnalysisV2"]

    # 直播-直播商品榜
    rank_product = ["/v1/douyin/live/rank/product"]

    # 直播-直播风车榜
    rank_windmill = ["/v1/douyin/live/rank/windmill"]

    # 特殊的达人分类
    specialAuthorCategory = ["/v1/common/specialAuthorCategory"]

    # 直播分享榜-周榜
    rank_starDailyRank1 = ["/v1/authorRank/starDailyRank"]

    # 直播分享榜-月榜
    rank_starDailyRank2 = ["/v1/authorRank/starRank"]

    # 直播分享榜-月榜
    live_search = ["/v2/douyin/live/search"]

    # 视频库
    aweme_search = ["/v2/home/aweme/search"]

    # 视频详情，观众分析
    aweme_personas = ["/v1/aweme/personas"]

    #达人库
    author_search = ["/v2/home/author/search"]

    #达人视频指数或潜力榜
    rank_officialStarRank = ["/v1/home/rank/officialStarRank"]

    # 视频探测器榜点
    aweme_hotspot_deadline = ["/v1/aweme/hotspot/deadline"]

    # 视频探测器小时榜
    aweme_hotspot_hour = ["/v1/aweme/hotspot/hour"]

    # 视频探测器每日榜
    aweme_hotspot_day = ["/v1/aweme/hotspot/day"]

    # 视频探测器七日榜
    aweme_hotspot_week = ["/v1/aweme/hotspot/week"]

    # 音乐库
    music_search = ["/v2/music/search"]

    # 本地生活榜地区
    poi_rank_area = ["/v1/douyin/poi/rank/area"]

    # 本地生活榜标签
    poi_rank_label = ["/v1/douyin/poi/rank/label"]

    # 本地生活榜
    poi_rank = ["/v1/douyin/poi/rank"]

    # 达人收藏-搜索达人
    v1_author_search = ["/v1/author/search"]

    # 添加达人收藏
    authorMine_addMine = ["/v1/authorMine/addMine"]

    # 取消达人收藏
    author_fav = ["/v1/author/fav"]

    # 达人收藏列表
    authorMine_listsV2 = ["/v1/authorMine/listsV2"]

    # 达人收藏分类
    authorMine_getLabels = ["/v1/authorMine/getLabels"]

    # 达人收藏添加分组
    authorMine_addGroup = ["/v1/authorMine/addGroup"]

    # 达人转移到分组
    authorMine_changeGroup = ["/v1/authorMine/changeGroup"]

    # 删除达人分组
    authorMine_delGroup = ["/v1/authorMine/delGroup"]

    # 查找子账号
    subuser_searchAccount = ["/v1/vip/subuser/searchAccount"]

    # 添加子账号
    subuser_addSubAccount = ["/v1/vip/subuser/addSubAccount"]

    # 商品收藏列表
    productMine_listsV2 = ["/v1/productMine/listV2"]

    # 添加商品收藏
    productMine_add = ["/v1/productMine/add"]

    # 获取商品分类
    productMine_catList = ["/v1/productMine/catList"]

    # 取消商品收藏
    product_fav = ["/v1/product/fav"]

    # 获取视频收藏列表
    aweme_favLists = ["/v1/aweme/favLists"]

    # 获取视频分类
    aweme_favListCat = ["/v1/aweme/favListCat"]

    # 新增视频收藏分组
    aweme_favGroupAdd = ["/v1/aweme/favGroupAdd"]

    # 新增视频收藏
    aweme_fav = ["/v1/aweme/fav"]

    # 取消视频收藏
    aweme_favCancel = ["/v1/aweme/favCancel"]

    # 删除视频收藏的分组
    aweme_favGroupDel = ["/v1/aweme/favGroupDel"]

if __name__ == '__main__':

    pass

