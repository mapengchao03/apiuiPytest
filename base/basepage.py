# -*- coding:utf-8 -*-
"""
selenium基类
本文件存放了selenium基类的封装方法
"""
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from common.logger import logger
from common.times import sleep


class WebPage(object):

    """selenium基类"""
    def __init__(self):
        self.service = webdriver.ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60) # 设置页面加载超时时间
        self.driver.implicitly_wait(10) # 隐式等待时间

    @staticmethod
    def locator_mode(mode):
        # 元素定位的类型
        locator_modes = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'name': By.NAME,
            'id': By.ID,
            'class': By.CLASS_NAME,
            'link': By.LINK_TEXT
        }
        return locator_modes[mode]

    def get_url(self, url):
        """打开网址并验证"""
        try:
            self.driver.get(url)
            logger.info("打开网页：%s成功" % url)
        except Exception as e:
            logger.error("打开网页%s错误" % url, repr(e))

    def close_browser(self):
        """关闭浏览器"""
        try:
            self.driver.close()
            logger.info("已关闭当前活动窗口浏览器")
        except Exception as e:
            logger.error("关闭当前活动窗口浏览器异常", repr(e))

    def quit_browser(self):
        """关闭浏览器"""
        try:
            self.driver.quit()
            logger.info("已关闭当前实例浏览器")
        except Exception as e:
            logger.error("关闭当前实例浏览器异常", repr(e))

    def del_all_cookies(self):
        """关闭浏览器"""
        try:
            self.driver.delete_all_cookies()
            logger.info("已删除当前实例浏览器的所有cookies")
        except Exception as e:
            logger.error("删除当前实例浏览的所有cookies器异常", repr(e))

    def find_element(self, locator):
        """寻找单个元素"""
        mode = locator[0]
        element = locator[1]
        web_element = ''
        try:
            web_element = self.driver.find_element(WebPage.locator_mode(mode), element)
            logger.info("获取元素%s成功" % locator)
        except Exception as e:
            logger.error("获取元素%s错误" % locator, repr(e) )
        finally:
            return web_element

    def find_elements(self, locator):
        """查找多个相同的元素"""
        mode = locator[0]
        element = locator[1]
        web_elements = list()
        try:
            web_elements = self.driver.find_elements(WebPage.locator_mode(mode), element)
            logger.info("获取多元素%s成功" % locator)
        except Exception as e:
            logger.error("获取多元素%s错误" % locator, repr(e))
        finally:
            return web_elements

    def find_elements_num(self, locator, num):
        """获取指定的第num个元素"""
        find_elements_num = ''
        ele = self.find_elements(locator)
        try:
            find_elements_num = ele[num]
            logger.info("获取多元素%s的第%s个元素成功" % locator % num)
        except Exception as e:
            logger.error("获取多元素%s的第%s个元素错误" % locator % num, repr(e))
        finally:
            return find_elements_num

    def is_send_keys(self, locator, txt):
        """单个元素输入内容(输入前先清空)"""
        ele = self.find_element(locator)
        try:
            ele.clear()
            sleep()
            ele.send_keys(txt)
            logger.info("输入文本：{}成功".format(txt))
        except Exception as e:
            logger.error("输入文本：{}错误".format(txt), repr(e))

    def is_click(self, locator):
        """单个元素点击"""
        ele = self.find_element(locator)
        try:
            ele.click()
            sleep()
            logger.info("点击元素：{}成功".format(locator))
        except Exception as e:
            logger.error("点击元素：{}错误".format(locator), repr(e))

    def are_send_keys(self, locator, num, txt):
        """有多个元素第num个元素输入内容(输入前先清空)"""
        ele = self.find_elements_num(locator, num)
        try:
            ele.clear()
            sleep()
            ele.send_keys(txt)
            logger.info("输入文本：{}成功".format(txt))
        except Exception as e:
            logger.error("输入文本：{}错误".format(txt), repr(e))

    def are_click(self, locator, num):
        """多个元素第num个元素点击"""
        ele = self.find_elements_num(locator, num)
        try:
            ele.click()
            sleep()
            logger.info("点击元素：{}成功".format(locator))
        except Exception as e:
            logger.error("点击元素：{}错误".format(locator), repr(e))

    def element_text(self, locator):
        """获取当前单个元素的text"""
        element_text = ''
        ele = self.find_element(locator)
        try:
            element_text = ele.text
            logger.error("获取文本：{}成功".format(element_text))
        except Exception as e:
            logger.error("获取文本：{}错误".format(element_text), repr(e))
        finally:
            return element_text

    def elements_text(self, locator, num):
        """获取当前单个元素的text"""
        elements_text = ''
        ele = self.find_elements_num(locator, num)
        try:
            elements_text = ele.text
            logger.error("获取文本：{}成功".format(elements_text))
        except Exception as e:
            logger.error("获取文本：{}错误".format(elements_text), repr(e))
        finally:
            return elements_text

    def get_title(self):
        """获取网页标题"""
        title = ''
        try:
            title = self.driver.title
            logger.info("获取网页标题为--%s" % title)
        except Exception as e:
            logger.error("获取网页标题异常", repr(e))
        finally:
            return title

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()

    def switch_to_frame(self, locator):
        """切换iframe到指定页面"""
        ele = self.find_element(locator)
        self.driver.switch_to.frame(ele)

    def switch_to_default_frame(self):
        """切回到主文档页面或窗口"""
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        """切回到当前frame的父级frame"""
        self.driver.switch_to.parent_frame()


if __name__ == "__main__":
    pass
