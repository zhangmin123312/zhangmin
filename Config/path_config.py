# -*- coding: utf-8 -*-
# @Time    : 2021/12/01
# @Author  : chenxubin
# @File    : common_config.py
"""
接口路径配置文件
"""


class PathMessage:
    # token路径
    token = ["/v1/access/token"]

    # 商品分类路径
    product_path = ["/v1/product/category"]

    # 达人分类路径
    star_category = ["/v1/common/starCategory"]

    # 地域分类
    common_area = ["/v1/common/area"]

    # 成长达人榜
    cheng_zhang_da_ren_bang = ["/v1/authorRank/bangNew"]

    # 商品品牌榜
    brand_rank = ["/v1/hot/brand/rank"]

    # 抖音销量榜
    rank_yesterdaySaleRank = ["/v1/home/rank/yesterdaySaleRank"]

    # 抖音热推榜
    rank_yesterdayHotRank = ["/v1/home/rank/yesterdayHotRank"]

    # 实时销量榜
    rank_liveRank = ["/v1/home/rank/liveRank"]

    # 抖音小店榜
    rank_specialtyToday = ["/v1/home/rank/specialtyToday"]

    # 小店库
    shop_search = ["/v2/shop/search"]

    # 小店详情页
    shop_detail_info = ["/v1/shop/detail/info"]

    # 选品库
    product_search = ["/v2/product/search"]

    # 品牌库
    brand_search = ["/v2/home/brand/search"]

    # 品牌详情页
    brand_detail_info = ["/v1/brand/detail/info"]

    # 品牌详情页-小店分析
    brand_detail_chart = ["/v1/brand/detail/chart"]

    # 品牌详情页-观众分析
    brand_detail_authorFansAnalysis = ["/v2/brand/detail/authorFansAnalysis"]


    # 品牌自播榜
    brand_self_author = ["/v1/douyin/live/rank/author/sales"]

    # 全天销量榜
    rank_allDayRank = ["/v1/home/rank/allDayRank"]

    # 涨粉达人榜
    author_rank_fans = ["/v1/home/author/rank/fans"]

    # 达人详情页info
    author_detail_info = ["/v1/author/detail/info"]

    # 商品分享日榜
    authorRank_starDailyRank = ["/v1/authorRank/starDailyRank"]

    # 商品分享周榜和月榜
    authorRank_starRank = ["/v1/authorRank/starRank"]

    # 达人榜
    authorRank_bangNew = ["/v1/authorRank/bangNew"]

    # 达人榜-带货达人
    authorRank_bangProductNew = ["/v1/authorRank/bangProductNew"]

    # 达人带货榜
    author_TakeProduct = ["/v1/douyin/live/rank/author/sales"]

    # 带货视频榜
    rank_productAweme = ['/v1/home/rank/productAweme']

    # 热门视频榜
    rank_hotAweme = ["/v1/home/rank/hotAweme"]

    # 引流视频榜
    rank_DrainageAweme = ["/v1/douyin/drainageAweme/rank"]

    # 官方热点榜
    rank_hotSpotRank = ["/v1/home/rank/hotSpotRank"]

    # 探店视频榜
    rank_searchShop = ["/v1/searchShop/rank"]

    # 探店视频榜地区
    rank_searchShop_area = ["/v1/douyin/poi/rank/area"]

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

    # 视频详情 视频诊断
    aweme_diagnose = ["/v1/aweme/detail/diagnose/info"]

    # 达人库
    author_search = ["/v2/home/author/search"]

    # 达人视频指数或潜力榜
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

    # 话题榜
    rank_subject = ["/v1/subject/rank"]

    # mcn榜
    mcn_rank = ["/v1/mcn/rank"]

    # 小店收藏列表
    shop_detail_fav_list = ["/v1/shop/detail/fav/list"]

    # 添加小店收藏
    shop_detail_fav_add = ["/v1/shop/detail/fav/add"]

    # 取消小店收藏
    shop_detail_fav_cancel = ["/v1/shop/detail/fav/cancel"]

    # 视频收藏列表
    aweme_favLists = ["/v1/aweme/favLists"]

    # 获取视频收藏分类
    aweme_favListCat = ["/v1/aweme/favListCat"]

    # 添加视频收藏分组
    aweme_favGroupAdd = ["/v1/aweme/favGroupAdd"]

    # 添加视频收藏
    aweme_fav = ["/v1/aweme/fav"]

    # 删除视频收藏分组
    aweme_favGroupDel = ["/v1/aweme/favGroupDel"]

    # 取消视频收藏
    aweme_favCancel = ["/v1/aweme/favCancel"]

    # 音乐收藏列表
    music_favLists = ["/v1/music/favLists"]

    # 添加/取消音乐收藏
    music_fav = ["/v1/music/fav"]

    # 话题收藏列表
    subject_favList = ["/v1/subject/favList"]

    # 添加/取消话题收藏
    subject_fav = ["/v1/subject/fav"]

    # 直播监控列表
    live_monitor_list = ["/v1/douyin/live/monitor/list"]

    # 直播监控搜索达人
    author_multiSearch = ["/v1/author/multiSearch"]

    # 添加直播监控
    live_monitor_add = ["/v1/douyin/live/monitor/add"]

    # 删除直播监控
    live_monitor_delete = ["/v1/douyin/live/monitor/delete"]

    # 直播监控置顶
    live_monitor_topSwitch = ["/v1/douyin/live/monitor/topSwitch"]

    # 取消直播监控
    live_monitor_cancel = ["/v1/douyin/live/monitor/cancel"]
     #昨日新兴榜

    authorLiveSelect_rising=['/v1/choose/product/dayRank']
    #三日潜力榜单
    authorLiveSelect_potential = ['/v1/choose/product/dayRank']
    #七日热销榜
    test_rank_authorLiveSelect_hotSale=['/v1/choose/product/dayRank']
    #持续好货榜
    authorLiveSelect_superiorProduct=['/v1/choose/product/continueRank']
    #历史同期榜
    authorLiveSelect_period=['/v1/choose/product/sameTimeRank']
    #直播商品一键采集
    test_home_associcte = ['/v1/author/detail/productSelection']
    #达人监控搜索达人
    authorSearch = ['/v1/author/search']
    #添加达人监控
    track_create = ['/v1/track/create']
    #达人监控列表
    track_history = ['/v1/track/history']
    #达人监控-达人置顶
    track_topSwitch_author=['/v1/track/topSwitch']
    #达人监控-删除达人
    track_delete=['/v1/track/delete']
    #视频监控弹窗，视频搜索
    aweme_monitor_search=["/v1/aweme/search"]
    #评论监控已授权抖音号
    authormine_auth = ['/v1/authormine/auth/list']
    #评论监控已授权抖音号列表
    getCreatorAwemeList = ['/v3/boss/aweme/getCreatorAwemeList']
    #话术监控，添加监控搜索
    author_multadd = ["/v1/author/multiSearch"]
    # 添加话术监控
    add_topic_monitor = ['/v1/douyin/live/topic_monitor/add']
    #话术监控列表
    topic_monitor_list  = ['/v1/douyin/live/topic_monitor/list']
    #删除话术监控
    topic_monitor_delete= ['/v1/douyin/live/topic_monitor/delete']
    #话术监控置顶
    topic_monitor_topSwitch=['/v1/douyin/live/topic_monitor/topSwitch']


if __name__ == '__main__':
    pass

