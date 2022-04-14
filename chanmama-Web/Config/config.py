# -*- coding: utf-8 -*-
# @Time    : 2019/8/19
# @Author  : chenlinjie
# @File    : Config.py

from configparser import ConfigParser
import os


class Config:
    # sections:
    section_debug = "debug"
    section_release = "release"
    section_mail = "Mail"
    section_graph = "graph"
    # [debug\release] options
    de_re_name = "loginName"
    de_re_pwd = "password"
    de_re_url = "login_url"
    de_re_id = "compId"
    de_re_ios = "isIOS"
    # [Mail] options
    mail_host = 'host'
    mail_port = 'port'
    mail_from = "msg_from"
    mail_receiver = "msg_to"
    mail_pwd = "password"
    mail_subject = "subject"
    mail_content = "text_content"

    # [graph] options
    graph_url = 'url'



    # 项目目录路径 ../Python-auto
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        # config.ini配置文件路径
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        # print(self.conf_path)
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")
        self.config.read(self.conf_path,encoding='utf-8')

        self.url_debug = self.get_conf(Config.section_debug,Config.de_re_url)
        self.url_release = self.get_conf(Config.section_release,Config.de_re_url)
        self.compId_debug = self.get_conf(Config.section_debug,Config.de_re_id)
        self.compId_release = self.get_conf(Config.section_release,Config.de_re_id)
        self.isIOS_debug = self.get_conf(Config.section_debug,Config.de_re_ios)
        self.isIOS_release = self.get_conf(Config.section_release,Config.de_re_ios)
        self.loginName_debug = self.get_conf(Config.section_debug,Config.de_re_name)
        self.loginName_release = self.get_conf(Config.section_release,Config.de_re_name)
        self.password_debug = self.get_conf(Config.section_debug,Config.de_re_pwd)
        self.password_release = self.get_conf(Config.section_release,Config.de_re_pwd)
        self.sender_mail = self.get_conf(Config.section_mail,Config.mail_from)
        self.receiver_mail = self.get_conf(Config.section_mail,Config.mail_receiver)
        self.password_mail = self.get_conf(Config.section_mail,Config.mail_pwd)
        self.subject_mail = self.get_conf(Config.section_mail,Config.mail_subject)
        self.content_mail = self.get_conf(Config.section_mail,Config.mail_content)
        self.host_mail = self.get_conf(Config.section_mail, Config.mail_host)
        self.port_mail = self.get_conf(Config.section_mail, Config.mail_port)
        self.graph_url = self.get_conf(Config.section_graph, Config.graph_url)


    def get_conf(self, section, option):
        """
        配置文件读取
        :param section: 配置节点，即[section]
        :param option: 对应节点里选项
        :return:
        """
        return self.config.get(section,option)

    def set_conf(self, section, option, value):
        """
        修改或创建节点里的选项
        :param section: 配置节点，即[section]
        :param option: 对应节点里选项
        :param value: 对应的值
        :return:
        """
        if not self.config.has_section(section):
            self.add_section(section)

        self.config.set(section, option, value)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_section(self, section):
        """
        添加配置节点
        :param section: 节点名称
        :return:
        """
        self.config.add_section(section)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def del_section(self, section):
        """
        删除节点
        :param section: 节点名称
        :return:
        """
        self.config.remove_section(section)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def del_option(self, section, option):
        """
        删除节点里选项（元素）
        :param section: 节点名称
        :param option:  节点里的选项
        :return:
        """
        self.config.remove_option(section, option)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)


if __name__ == '__main__':

    a = Config()
    # a.add_section('test111')
    # a.set_conf('test111', 'name2', 'zhangsan2')
    # a.del_section('test111')
    # a.del_option('test111', 'name')