import pytest

from Common.Base import base
from Config.path_config import PathMessage
import datetime,os,jsonpath


def get_hours(path):
    """
    返回直播-带货小时榜的榜点
    """
    para = f"date={datetime.datetime.now().date()}"
    response = base().return_request(method="get", path=path, data=para ,hosts=os.environ["host"])
    return response['response_body']['data']

def get_product_category():
    """
    返回带货小时榜的商品分类
    """
    para = f"star_category=&product_category=&order=desc&orderby=amount&timestamp={get_hours(PathMessage.rank_official_hours)[-1]}&page=1&size=50"
    response = base().return_request(method="get", path=PathMessage.rank_official, data=para ,hosts=os.environ["host"])
    product_category_list = jsonpath.jsonpath(response["response_body"], f'$.data.product_category[*].cat_name')
    return product_category_list

@pytest.fixture(params=get_hours(PathMessage.rank_official_hours))
def timestamps(request):
    """
    获取直播-带货小时榜的单个榜点
    """
    yield request.param

@pytest.fixture(scope="session", autouse=True)
def last_timestamp():
    """
    获取直播-带货小时榜的最后一个榜点
    """
    timestamps_list=get_hours(PathMessage.rank_official_hours)
    return timestamps_list[-1]

@pytest.fixture(params=get_product_category())
def product_category(request):
    """
    获取带货小时榜的单个商品分类
    """
    yield request.param

@pytest.fixture(params=get_hours(PathMessage.rank_soundbyte_hours))
def soundbyte_timestamps(request):
    """
    获取直播-抖音官方小时榜的单个榜点
    """
    yield request.param

@pytest.fixture(scope="session", autouse=True)
def soundbyte_last_timestamp():
    """
    获取直播-抖音官方小时榜的最后一个榜点
    """
    timestamps_list=get_hours(PathMessage.rank_soundbyte_hours)
    return timestamps_list[-1]

@pytest.fixture(scope="session", autouse=True)
def get_Nearly_7_date():
    """
    获取预热视频分析近7天的日期
    """
    date_list=base.return_Filter_date(0,7)
    return date_list[1]