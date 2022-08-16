import pytest

from Common.Base import base
from Config.path_config import PathMessage
import datetime,os,jsonpath,json,time
from Config.Consts import sub_telephone
from filelock import FileLock

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
    addGroup_para = {"group_name": "测试分组"+str(time.time())}
    addGroup_response = base().return_request(method="post", path=PathMessage.authorMine_addGroup,data=json.dumps(addGroup_para),tokens=get_token, hosts=os.environ["host"])
    group_id = addGroup_response['response_body']['data']['group_id']
    # 达人转移到分组内
    changeGroup_para = {"group_id": group_id,"author_id": author_id}
    changeGroup_response = base().return_request(method="post", path=PathMessage.authorMine_changeGroup,data=json.dumps(changeGroup_para),tokens=get_token, hosts=os.environ["host"])
    yield author_id,nickname,tag,group_id
    # 删除分组
    delGroup_para = {"group_id": group_id}
    delGroup_response = base().return_request(method="post", path=PathMessage.authorMine_delGroup,data=json.dumps(delGroup_para),tokens=get_token, hosts=os.environ["host"])


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

@pytest.fixture(scope='session')
def add_shop_list(get_token):
    """
    添加小店收藏
    """
    # 获取小店id
    shop_search_para ="page=1&big_category=&first_category=&keyword=&sort=volume&orderby=desc&size=50&has_aweme=0&has_live=0&avg_price=&avg_amount=&expr_score="
    shop_search_response = base().return_request(method="get", path=PathMessage.shop_search, data=shop_search_para,tokens=get_token, hosts=os.environ["host"])
    shop_id=shop_search_response['response_body']['data']['list'][1]['shop_id']
    category_big=shop_search_response['response_body']['data']['list'][1]['category_arr'][0]['big']

    # 小店收藏
    add_para = {"shop_id": shop_id}
    add_response = base().return_request(method="post", path=PathMessage.shop_detail_fav_add,data=json.dumps(add_para),tokens=get_token, hosts=os.environ["host"])

    return shop_id,category_big

@pytest.fixture(scope='session')
def add_aweme_fav(get_token):
    """
    添加视频收藏
    """
    # 获取视频id
    search_para="gender_type=-1&age_types=&province=&page=1&star_category=&star_sub_category=&keyword=&digg=&follower_counts=&durations=&hour_ranges=&sort=digg_count&time=24h&size=50&goods_relatived=0&fans_hottest=0&group_buy_relatived=0&filter_delete=1&order_by=desc"
    search_response = base().return_request(method="get", path=PathMessage.aweme_search, data=search_para, tokens=get_token,hosts=os.environ["host"], )
    aweme_id=search_response['response_body']['data']['list'][10]['aweme_info']['aweme_id']
    aweme_title=search_response['response_body']['data']['list'][10]['aweme_info']['aweme_title']
    category=search_response['response_body']['data']['list'][10]['author_info']['single_tags']['first']

    # 添加分组
    favGroupAdd_para = {"group_name": "测试分组"+str(time.time())}
    favGroupAdd_response = base().return_request(method="post", path=PathMessage.aweme_favGroupAdd,data=json.dumps(favGroupAdd_para),tokens=get_token, hosts=os.environ["host"])
    group_id = favGroupAdd_response['response_body']['data']['id']

    # 添加视频收藏
    fav_para = {"aweme_id": aweme_id,"group_id": group_id}
    fav_response = base().return_request(method="post", path=PathMessage.aweme_fav,data=json.dumps(fav_para),tokens=get_token, hosts=os.environ["host"])
    yield str(aweme_id),aweme_title,category,str(group_id)

    # 删除分组
    favGroupDel_para = {"id": group_id}
    favGroupDel_response = base().return_request(method="post", path=PathMessage.aweme_favGroupDel,data=json.dumps(favGroupDel_para),tokens=get_token, hosts=os.environ["host"])
    # 取消收藏
    favCancel_para = {"aweme_id": aweme_id,"sub_user_id": 0}
    favCancel_response = base().return_request(method="post", path=PathMessage.aweme_favCancel,data=json.dumps(favCancel_para),tokens=get_token, hosts=os.environ["host"])

@pytest.fixture(scope="session")
def common_init(tmp_path_factory, worker_id,get_token):

    if worker_id == "master":
        sub_user_id = add_subAccount(get_token)
        os.environ['sub_user_id'] = str(sub_user_id)
        return sub_user_id

    root_tmp_dir = tmp_path_factory.getbasetemp().parent
    fn = root_tmp_dir / "data.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            sub_user_id = json.loads(fn.read_text())
        else:
            sub_user_id = add_subAccount(get_token)
            fn.write_text(json.dumps(sub_user_id))
        os.environ['sub_user_id'] = str(sub_user_id)

    return sub_user_id

@pytest.fixture(scope='session')
def add_music_favLists(get_token):
    """
    添加音乐收藏
    """
    # 获取音乐id
    music_search_para ="keyword=&page=1&size=50&orderby=user_incr&incr_type=yesterday&order=desc"
    music_search_response = base().return_request(method="get", path=PathMessage.music_search, data=music_search_para,tokens=get_token, hosts=os.environ["host"])
    music_id=music_search_response['response_body']['data']['list'][0]['music_id']

    # 音乐收藏
    fav_para = {"music_id": music_id}
    fav_response = base().return_request(method="post", path=PathMessage.music_fav,data=json.dumps(fav_para),tokens=get_token, hosts=os.environ["host"])

    return music_id

@pytest.fixture(scope='session')
def add_subject_favList(get_token):
    """
    添加话题收藏
    """
    # 获取话题id
    date=datetime.datetime.now().date()- datetime.timedelta(days=1)
    rank_subject_para =f"day_type=day&date={date}&order=aweme_count_inc&page=1&size=50"
    rank_subject_response = base().return_request(method="get", path=PathMessage.rank_subject, data=rank_subject_para,tokens=get_token, hosts=os.environ["host"])
    subject_id=rank_subject_response['response_body']['data']['list'][0]['subject_id']

    # 话题收藏
    fav_para = {"subject_id": subject_id}
    fav_response = base().return_request(method="post", path=PathMessage.subject_fav,data=json.dumps(fav_para),tokens=get_token, hosts=os.environ["host"])

    return subject_id
