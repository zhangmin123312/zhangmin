# -*- coding: utf-8 -*-
# @Time    : 2021/12/01
# @Author  : chenxubin
# @File    : Base.py

"""
封装常用的方法
"""
import shutil
import hashlib
import datetime
from datetime import timedelta
import time
from dingtalkchatbot.chatbot import DingtalkChatbot
from Common.request import Request
from Config.Consts import user_agent
from Config.path_config import PathMessage



class base():

    @staticmethod
    def copy_file(source_file,targrt_file):
        """复制文件"""
        shutil.copyfile(source_file,targrt_file)


    @staticmethod
    def dingding(title):
        """使用钉钉，发送消息"""

        # 机器人的webhooK
        webhook = "https://oapi.dingtalk.com/robot/send?access_token=496fea610cae3356bd829c68db5b82b6affe551726c1c917c09c61b7e2114c58"
        send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        xiaoding = DingtalkChatbot(webhook)
        xiaoding.send_text(msg="""监控等级：WARNING\n时间：{}\n类型：小红书数据\n内容：{}""".format(send_time,title), at_mobiles=["17350894220","18521716740"])

    @staticmethod
    def dingding_suceces():
        webhook = "https://oapi.dingtalk.com/robot/send?access_token=496fea610cae3356bd829c68db5b82b6affe551726c1c917c09c61b7e2114c58"
        send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        xiaoding = DingtalkChatbot(webhook)
        xiaoding.send_text(msg="""监控情况：无异常\n时间：{}\n类型：小红书数据""".format(send_time), at_mobiles=["18695682863"])


    @staticmethod
    def get_time(types, method, num):
        """
        :param Types:
        # :param method: add为增加，del为减少
        # :param num: 具体的天数或周数
        # :return: 当前日期加上或减去具体的天数或周数
        """

        if types == "nowweek":
            if method == "add":
                now = datetime.datetime.now().date()
                lDay = now + timedelta(days=(7 - now.weekday()) + 7 * (num - 1))
                rDay = lDay + timedelta(days=6)
                date1 = [str(lDay).replace("-", ""), str(rDay).replace("-", "")]
                date2 = [str(lDay), str(rDay)]
                return [date1, date2]
            elif method == "del":
                now = datetime.datetime.now().date()
                lDay = now - timedelta(days=now.weekday() + (7 * abs(num)))
                rDay = lDay + timedelta(days=6)
                date1 = [str(lDay).replace("-", ""), str(rDay).replace("-", "")]
                date2 = [str(lDay), str(rDay)]
                return [date1, date2]
            else:
                print("方法输入错误")

        elif types == "del_month":

            today = datetime.date.today()
            first = today.replace(day=1)
            last_month = first - datetime.timedelta(days=1)
            return last_month.strftime("%Y%m")


        elif types == "nowday":

            if method == "add":
                add_day = datetime.datetime.now() + datetime.timedelta(days=num)
                now_day = add_day.strftime('%Y-%m-%d')
                # print(now_day)
                return now_day
            elif method == "del":
                del_day = datetime.datetime.now() - datetime.timedelta(days=num)
                now_day = del_day.strftime('%Y-%m-%d')
                # print(now_day)
                return now_day
            else:
                print("方法输入错误")

        else:
            print("类型输入错误")




    @staticmethod
    def return_time_message():
        """
        返回昨天、上周、上个月的时间list
        """
        now = datetime.datetime.now().date()
        lDay = now - timedelta(days=now.weekday() + (7 * abs(1)))
        rDay = lDay + timedelta(days=6)
        week_date = "{}-{}".format(str(lDay).replace("-", ""), str(rDay).replace("-", ""))
        del_day = datetime.datetime.now() - datetime.timedelta(days=1)
        now_day = del_day.strftime('%Y-%m-%d')
        today = datetime.date.today()
        day = today.replace(day=1)
        last_month = day - datetime.timedelta(days=1)
        month_data = last_month.strftime("%Y%m")

        return [["day",now_day],["week",week_date],["month",month_data]]




    @staticmethod
    def return_product_types(host,type):
        """
        返回商品分类
        """
        responce = base().return_request(method="get",path=PathMessage.product_path,hosts=host)['response_body']['data']
        category_big_types_list = []
        category_first_types_list = []
        # category_two_types_list = []
        for i in responce:
            category_big_types_list.append([i["cat_name"]])
            for a in i["sub_categories"]:
                category_first_types_list.append([i["cat_name"], a["cat_name"]])
            # for b in a["sub_categories"]:
            # 	category_two_types_list.append([i["cat_name"],a["cat_name"],b["cat_name"]])


        if type == 1:

            return category_big_types_list

        elif type == 2:

            return category_first_types_list

        else:
            print("类别输入有误")
            raise False



    @staticmethod
    def return_star_category(host,type):
        """
        返回达人分类
        """
        responce = base().return_request(method="get",path=PathMessage.star_category,hosts=host)['response_body']['data']
        category_big_types_list = []
        category_first_types_list = []
        # category_two_types_list = []
        for i in responce:
            category_big_types_list.append([i["cat_name"]])
            for a in i["sub_categories"]:
                category_first_types_list.append([i["cat_name"], a["cat_name"]])
            # for b in a["sub_categories"]:
            # 	category_two_types_list.append([i["cat_name"],a["cat_name"],b["cat_name"]])

        if type == 1:

            return category_big_types_list

        elif type == 2:

            return category_first_types_list

        else:
            print("类别输入有误")
            raise False






    @staticmethod
    def return_Sign(path):

        timestamp = int(time.time())
        # 签名计算方式：接口地址 + 密钥（523a1#$32@68a!5 + 时间戳
        data = path + "523a1#$32@68a!5" + str(timestamp)
        # md5值
        sign = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
        signdict = {
            'X-Inner-Service-Sign': sign,
            'X-Inner-Service-Timestamp': str(timestamp),
            'X-Inner-Service-Type': 'test-unit',
        }

        return signdict



    def return_request(self,method,path,tokens=None,hosts=None,data=None):

        header = base.return_Sign(path[0])
        header["Authorization"] = tokens
        header["User-Agent"] = user_agent


        if method == "get":

            if len(path) > 2:

                res = Request.get_request(url=hosts+ path[0] + path[1],headers=header,data=data)
                return res

            res = Request.get_request(url=hosts + path[0] , headers=header,data=data)
            return res

        elif method == "post":

            res = Request.post_request(url=hosts+path[0],headers=header,data=data)
            return res

        else:

            print("请输入请求方法")
            raise False












if __name__ == '__main__':

    print(base.return_product_types("https://api-service.chanmama.com",2))












