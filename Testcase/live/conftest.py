import pytest

from Common.Base import base
from Config.path_config import PathMessage
import datetime,os,jsonpath


def get_official_hours():
    """
    返回直播-带货小时榜的榜点
    """
    para = f"date={datetime.datetime.now().date()}"
    response = base().return_request(method="get", path=PathMessage.rank_official_hours, data=para ,hosts=os.environ["host"])
    return response['response_body']['data']

def get_product_category():
    """
    返回带货小时榜的商品分类
    """
    para = f"star_category=&product_category=&order=desc&orderby=amount&timestamp={get_official_hours()[-1]}&page=1&size=50"
    response = base().return_request(method="get", path=PathMessage.rank_official, data=para ,hosts=os.environ["host"])
    product_category_list = jsonpath.jsonpath(response["response_body"], f'$.data.product_category[*].cat_name')
    return product_category_list

@pytest.fixture(params=get_official_hours())
def timestamps(request):
    yield request.param

@pytest.fixture(scope="session", autouse=True)
def last_timestamp():
    timestamps_list=get_official_hours()
    return timestamps_list[-1]

@pytest.fixture(params=get_product_category())
def product_category(request):
    yield request.param