# -*- coding: utf-8 -*-
# @Time    : 2019/08/27
# @Author  : chenxubin
# @File    : Assert.py

"""
封装Assert方法
"""

from Common.mylog import Mylog

class Assert:

    def __init__(self):
        pass

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except:
            Mylog.error("statusCode error: expected_code is %s, statusCode is %s " % (expected_code, code))
            raise Exception('返回状态码不正确')

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True
        except:
            Mylog.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            raise Exception('返回信息和预期信息不一致')

    def assert_in_text(self,body,expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        text = None
        try:
            text = body["body"]["data"]["response"][0]
            expected_msg = expected_msg.split(r"\n")[0]
            assert text in expected_msg
            return True
        except :
            Mylog.error("Response body Does not contain expected_msg, response body is: %s, expected_msg is: %s" % (text,expected_msg))
            raise Exception('返回的信息不在预期结果之内')


    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            expected_msg = expected_msg.split(r"\n")[0]
            assert body["body"]["data"]["response"][0].strip() == expected_msg.strip()
            return True
        except:
            Mylog.error("\n\nResponse body != expected_msg, \n\nexpected_msg is: \n%s, \n\nbody is: \n%s\\n" % (expected_msg, body))
            raise Exception('实际返回结果和预期结果不一致')

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            Mylog.error("Response time > expected_time, expected_time is: %s, time is: %s" % (expected_time, time))
            raise Exception('应答响应时间大于预期响应时间')


if __name__ == "__main__":

    a = Assert()
    # a.assert_code(200,200)
    a.assert_code(200,2000)
