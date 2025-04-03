# -*- coding:utf-8 -*-
from base.basepage import WebPage
from common.times import sleep

class JenkinsLogin(WebPage):

    # 元素定位器
    username_input = ("css", "#j_username")
    password_input = ("css", "#j_password")
    login_button = ("css", ".jenkins-button")


    def __init__(self,driver):
         super().__init__(driver)

    def input_username(self, content):
        self.is_send_keys(self.username_input, txt=content)
        sleep()

    def input_password(self, content):
        self.is_send_keys(self.password_input, txt=content)
        sleep()

    def click_login(self):
        """点击搜索"""
        self.is_click(self.login_button)
        sleep()
