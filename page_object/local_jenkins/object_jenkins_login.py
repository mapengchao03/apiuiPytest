# -*- coding:utf-8 -*-
from base.basepage import WebPage
from common.times import sleep
from common.util import util_data
from common.read_data import read_data

class JenkinsLogin(WebPage):

    def input_username(self, content):
        self.is_send_keys(util_data.split_data(login_yaml['用户名输入框']), txt=content)
        sleep()

    def input_password(self, content):
        self.is_send_keys(util_data.split_data(login_yaml['密码输入框']), txt=content)
        sleep()

    def click_login(self):
        """点击搜索"""
        self.is_click(util_data.split_data(login_yaml['登录按钮']))
        sleep()

login_yaml = read_data.read_yaml("data/ui/local_jenkins/object_jenkins_login.yaml")
jenkins_login = JenkinsLogin()