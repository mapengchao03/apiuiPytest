# -*- coding:utf-8 -*-
import allure
from common.logger import logger
from config import config
from common.read_data import read_data
from page_object.local_jenkins.object_jenkins_login import JenkinsLogin

@allure.feature("jenkins登录功能")
class TestJenkinsLogin:

    @allure.story("登录")
    @allure.title("jenkins登录正确用例")
    def test_001(self, driver):
        """登录本地jenkins成功"""
        jenkins_login = JenkinsLogin(driver)
        data = read_data.read_json("data/ui/local_jenkins/test_jenkins_login.json")
        username = data["test_001"]["用户名"]
        password = data["test_001"]["密码"]
        assert_title_txt = data["test_001"]["校验标题内容"]
        with allure.step("步骤1:打开本地jenkins网址"):
            jenkins_login.get_url(config.local_jenkins_host)
        with allure.step("步骤2:输入用户名"):
            jenkins_login.input_username(username)
        with allure.step("步骤3:输入密码"):
            jenkins_login.input_password(password)
        with allure.step("步骤4:点击登录"):
            jenkins_login.click_login()
        with allure.step("步骤5:校验结果"):
            result = jenkins_login.get_title()
            try:
                assert assert_title_txt == result
            except Exception as e:
                # 第一logger.error是为了记录日志，
                # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
                logger.error(f"校验失败，错误信息:{repr(e)}")
                raise e
            else:
                logger.info("校验成功")
