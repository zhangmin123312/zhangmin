import pytest

from Common.Base import base
from Config.path_config import PathMessage
import datetime,os,jsonpath,json,time
from Config.Consts import sub_telephone

@pytest.fixture(scope='session')
def add_author(get_token):
    """
    添加达人收藏
    """
    # 搜索达人
    search_para = {"keyword": "a"}
    search_response = base().return_request(method="post", path=PathMessage.v1_author_search, data=json.dumps(search_para),tokens=get_token, hosts=os.environ["host"])
    author_id=search_response['response_body']['data']['author_info']['author_id']
    nickname=search_response['response_body']['data']['author_info']['nickname']
    tag=search_response['response_body']['data']['author_info']['single_tags']['first']
    # 添加达人收藏
    addMine_para = {"author_id": author_id}
    addMine_response = base().return_request(method="post", path=PathMessage.authorMine_addMine,data=json.dumps(addMine_para),tokens=get_token, hosts=os.environ["host"])
    # 添加分组
    addGroup_para = {"group_name": "测试分组"}
    addGroup_response = base().return_request(method="post", path=PathMessage.authorMine_addGroup,data=json.dumps(addGroup_para),tokens=get_token, hosts=os.environ["host"])
    group_id = addGroup_response['response_body']['data']['group_id']
    # 达人转移到分组内
    changeGroup_para = {"group_id": group_id,"author_id": author_id}
    changeGroup_response = base().return_request(method="post", path=PathMessage.authorMine_changeGroup,data=json.dumps(changeGroup_para),tokens=get_token, hosts=os.environ["host"])
    yield author_id,nickname,tag,group_id
    # 删除分组
    delGroup_para = {"group_id": group_id}
    delGroup_response = base().return_request(method="post", path=PathMessage.authorMine_delGroup,data=json.dumps(delGroup_para),tokens=get_token, hosts=os.environ["host"])

@pytest.fixture(scope='session')
def add_subAccount(get_token):
    """
    添加子账号
    """
    # 搜索子账号
    searchAccount_para = f"account={str(sub_telephone)}"
    searchAccount_response = base().return_request(method="get", path=PathMessage.subuser_searchAccount, data=searchAccount_para,tokens=get_token, hosts=os.environ["host"])
    sub_user_id=searchAccount_response['response_body']['data']['id']

    # 添加子账号
    addSubAccount_para = {"sub_user_id": sub_user_id}
    addSubAccount_response = base().return_request(method="post", path=PathMessage.subuser_addSubAccount,data=json.dumps(addSubAccount_para),tokens=get_token, hosts=os.environ["host"])

    return sub_user_id

@pytest.fixture(scope='session')
def add_productMine(get_token):
    """
    添加商品收藏
    """
    # 获取商品id
    product_search_para = {}
    product_search_response = base().return_request(method="post", path=PathMessage.product_search, data=json.dumps(product_search_para),tokens=get_token, hosts=os.environ["host"])
    promotion_id=product_search_response['response_body']['data']['list'][0]['promotion_id']
    title=product_search_response['response_body']['data']['list'][0]['title']

    # 商品收藏
    add_para = {"promotion_id": promotion_id}
    add_response = base().return_request(method="post", path=PathMessage.productMine_add,data=json.dumps(add_para),tokens=get_token, hosts=os.environ["host"])

    # 获取商品分类
    catList_para = f"account={str(sub_telephone)}"
    catList_response = base().return_request(method="get", path=PathMessage.productMine_catList,
                                                   data=catList_para, tokens=get_token, hosts=os.environ["host"])
    key = catList_response['response_body']['data'][0]['key']
    return promotion_id,title,key