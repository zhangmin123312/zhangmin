import pytest

from Common.Base import base
from Config.path_config import PathMessage
import datetime,os,jsonpath,json,time
from filelock import FileLock
import time


def get_live_monitor_id(get_token,unique_id):

    monitor_id_Next,monitor_id_this=None,None
    # 查询是否已添加监控
    list_para = f"page=1&size=15&status=-1&keyword={unique_id}"
    list_response = base().return_request(method="get", path=PathMessage.live_monitor_list, data=list_para, tokens=get_token,hosts=os.environ["host"])
    assert list_response["status_code"] == 200
    for value in list_response['response_body']['data']['list']:
        if value['status']==0:
            monitor_id_Next=value['id']
        elif value['status']==1:
            monitor_id_this=value['id']

    return monitor_id_Next,monitor_id_this

def add_live(get_token,author_id,type):
    """添加直播监控，type=0添加本月监控，否则添加次月监控"""
    now_time = datetime.datetime.now()
    month = now_time.month
    if month == 12:
        month = 0
    # 次月1号0点
    next_mouth_first = datetime.datetime(now_time.year, month + 1, 1, 0, 0, 0)
    future_mouth_next = datetime.datetime(now_time.year, month + 2, 1, 0, 0, 0)
    this_month_last = next_mouth_first - datetime.timedelta(seconds=1)
    next_month_last = next_mouth_first + datetime.timedelta(hours=5)

    if type==0:
        start_time=int(time.mktime(now_time.timetuple()))
        end_time=int(time.mktime(this_month_last.timetuple()))
    else:
        start_time=int(time.mktime(next_mouth_first.timetuple()))
        end_time=int(time.mktime(next_month_last.timetuple()))

    add_para = {
	"author_id": author_id,
	"start_time": start_time,
	"end_time": end_time,
	"notice": 1
    }
    add_response = base().return_request(method="post", path=PathMessage.live_monitor_add,data=json.dumps(add_para), tokens=get_token,hosts=os.environ["host"])
    return add_response['response_body']['data']['monitor_id']


@pytest.fixture(scope='session')
def add_live_monitor(get_token):
    """
    添加直播收藏
    """
    # 搜索达人
    multiSearch_para = {"keyword": "b"}
    multiSearch_response = base().return_request(method="post", path=PathMessage.author_multiSearch, data=json.dumps(multiSearch_para),tokens=get_token, hosts=os.environ["host"])
    # print(multiSearch_response)
    nickname=multiSearch_response['response_body']['data']['search_results'][0]['author_info']['nickname']
    #有些达人没有unique_id，统一全部取short_id
    unique_id=multiSearch_response['response_body']['data']['search_results'][0]['author_info']['short_id']
    author_id=multiSearch_response['response_body']['data']['search_results'][0]['author_info']['author_id']

    # 查询是否已添加监控
    monitor_id_Next,monitor_id_this=get_live_monitor_id(get_token,unique_id)
    # 添加当月监控
    if monitor_id_this==None:
        monitor_id_this=add_live(get_token, author_id, type=0)
    # 添加次月监控
    if monitor_id_Next==None:
        monitor_id_Next=add_live(get_token, author_id, type=1)

    yield nickname,unique_id,monitor_id_this,monitor_id_Next

    # 清理过期的监控(监控结束时间超过2个月的)
    list_para = f"page=1&size=15&status=-1&keyword="
    list_response = base().return_request(method="get", path=PathMessage.live_monitor_list, data=list_para, tokens=get_token,hosts=os.environ["host"])

    for value in list_response['response_body']['data']['list']:
        end_time = datetime.datetime.strptime(value['end_time'], "%Y-%m-%dT%H:%M:%S+08:00")
        if time.time()-time.mktime(end_time.timetuple())>2*30*24*60*60:
            delete_para = {"monitor_id": value['id']}
            delete_response = base().return_request(method="post", path=PathMessage.live_monitor_delete,data=json.dumps(delete_para),tokens=get_token, hosts=os.environ["host"])


@pytest.fixture(scope='session')
def add_author_monitor(get_token):

    #搜索达人
    authorSeach_para={'keyword': "7"}
    authorSeach_responce=base().return_request(method="post",path=PathMessage.authorSearch,data=json.dumps(authorSeach_para),tokens=get_token,hosts=os.environ["host"])
    # print(authorSeach_responce)
    nickname=authorSeach_responce["response_body"]["data"]['author_info']["nickname"]
    author_id=authorSeach_responce["response_body"]["data"]['author_info']["author_id"]
    unique_id=authorSeach_responce["response_body"]["data"]['author_info']["unique_id"]
    # print(nickname,unique_id,author_id)

    yield nickname, unique_id, author_id


@pytest.fixture(scope='session')
def delete_author_monitor(get_token):

    #筛选已完成监控的达人
    data = {
        'keyword': '',
        'list_type': 'author',
        'page': '1',
        'pagesize': 15,
        'status': 2
    }
    responce=base().return_request(method="post",path=PathMessage.track_history,data=json.dumps(data),tokens=get_token,hosts=os.environ["host"])
    # print(responce)
    trackId = jsonpath.jsonpath(responce["response_body"], f'$.data.track_lists[*].track_info.trackId')
    yield trackId


@pytest.fixture(scope='session')
def delete_aweme_monitor(get_token):
# 筛选已完成监控的视频监控id
    delete_aweme_data = {
        'keyword': '',
        'list_type': 'aweme',
        'page': '1',
        'pagesize': 15,
        'status': 2
    }


    delete_aweme_responce = base().return_request(method="post", path=PathMessage.track_history, data=json.dumps(delete_aweme_data), tokens=get_token,
                                 hosts=os.environ["host"])
    # print(delete_aweme_responce)
    trackId = jsonpath.jsonpath(delete_aweme_responce["response_body"], f'$.data.track_lists[*].track_info.trackId')
    yield trackId


@pytest.fixture(scope='session')
def add_aweme_monitor(get_token):
#热门视频库获取监控视频id
    para='gender_type=-1&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort=digg_count&time=24h&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&aweme_graph_type=0&filter_delete=1&order_by=desc&from=detail'


    responce = base().return_request(method="get", path=PathMessage.aweme_search, data=para, tokens=get_token,
                                 hosts=os.environ["host"])

    nickname = responce["response_body"]["data"]['list'][0]["author_info"]['nickname']
    aweme_url = responce["response_body"]["data"]['list'][0]["aweme_info"]['aweme_url']
    aweme_title = responce["response_body"]["data"]['list'][0]["aweme_info"]['aweme_title']
    # print(nickname, aweme_url, aweme_title)
    yield nickname, aweme_url, aweme_title
@pytest.fixture(scope='session')
def add_live_topic_monitor(get_token):
    datatime1 = datetime.datetime.now() - datetime.timedelta(days=1)
    times=datatime1.strftime('%Y-%m-%d')
    para=f'day_type=day&day={times}&big_category=&first_category=&second_category=&sort=sales_volume&page=1&size=50&verification_type=&is_brand_self_author=0&is_shop_author=0&dark_horse=0&first_rank=0&is_bomb=0'
    responce = base().return_request(method="get", path=PathMessage.author_TakeProduct, data=para, tokens=get_token,
                                     hosts=os.environ["host"])
    # print(responce)
    nickname=responce["response_body"]["data"]['list'][0]["nickname"]
    author_id=responce["response_body"]["data"]['list'][0]["author_id"]
    unique_id=responce["response_body"]["data"]['list'][0]["unique_id"]
    yield nickname, author_id, unique_id







