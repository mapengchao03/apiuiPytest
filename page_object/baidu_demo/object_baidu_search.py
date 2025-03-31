# -*- coding:utf-8 -*-
from base.basepage import WebPage
from common.times import sleep
from common.util import util
from common.read_data import read_data


class BaiduSearch(WebPage):

    """搜索类"""
    def input_search(self, content):
        """搜索框输入内容"""
        self.is_send_keys(util.split_data(search_yaml['搜索框']), txt=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(util.split_data(search_yaml['候选']))]

    def click_search(self):
        """点击搜索"""
        self.is_click(util.split_data(search_yaml['搜索按钮']))


search_yaml = read_data.read_yaml("data/ui/baidu_demo/object_baidu_search.yaml")
baidu_search = BaiduSearch()

if __name__ == '__main__':
    print(util.split_data(search_yaml['搜索框']))
