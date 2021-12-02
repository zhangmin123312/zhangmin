# -*- coding: utf-8 -*-
# @Time    : 2021/12/1
# @Author  : chenxubin
# @File    : test_xuanpingku.py

import allure
from Common.Base import base
from Config.path_config import PathMessage




@allure.feature('测试样例')
class TestCase_XuanPingKu():

    """测试样例"""

    def test_douyin_xiao_liang_bang(self,get_token,get_host):

        responce = base().return_request(method="get",path=PathMessage.quan_tian_xiao_liang_bang,tokens=get_token,hosts=get_host,)
        assert len(responce["response_body"]["data"]["list"]) > 10

    def test_xuan_ping_ku(self,get_token,get_host):
        data = {"keyword":"","keyword_type":"","page":1,"price":"","size":50,"filter_coupon":0,"has_live":0,"has_video":0,"tb_max_commission_rate":"","day_pv_count":"","duration_volume":"","big_category":"","first_category":"","second_category":"","platform":"","sort":"duration_volume","order_by":"desc","day_type":1,"most_volume":-1,"most_aweme_volume":0,"most_live_volume":0}
        responce = base().return_request(method="post", path=PathMessage.xuan_ping_ku, data=data,tokens=get_token,hosts=get_host, )
        assert responce["status_code"] == 200


    def test_cheng_zhang_da_ren_bang(self,get_token,get_host):
        data = {"bang_type":"G","star_category":"","day_type":"day","day":base.get_time("nowday","del",1),"page":1}
        responce = base().return_request(method="post", path=PathMessage.cheng_zhang_da_ren_bang, data=data,tokens=get_token,hosts=get_host, )
        print(responce)
        assert responce["status_code"] == 200




















# if __name__ == '__main__':
#     pytest.main(['-s', '-q', "test_xuanpingku.py::TestCase_XuanPingKu::test_xuanpingku_category_types"])

