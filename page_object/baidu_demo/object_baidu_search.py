# -*- coding:utf-8 -*-
from common.times import sleep
from base.basepage import WebPage

class BaiduSearch(WebPage):

    # 元素定位器
    search_input = ("id", "kw")
    search_button = ("id", "su")
    candidate_input = ("css", ".bdsug-overflow")

    """搜索类"""
    def __init__(self,driver):
        super().__init__(driver)

    def input_search(self, content):
        """搜索框输入内容"""
        self.is_send_keys(self.search_input, txt=content)
        sleep()

    def click_search(self):
        """点击搜索"""
        self.is_click(self.search_button)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(self.candidate_input)]


