# -*- coding:utf-8 -*-
import allure
from common.logger import logger
from config import config
from page_object.local_jenkins.jenkins_login import jenkins_login

@allure.feature("jenkins登录功能")
class TestJenkinsLogin:

    @allure.story("登录")
    @allure.title("jenkins登录正确用例")
    def test_001(self):
        """登录本地jenkins成功"""
        with allure.step("步骤1:打开本地jenkins网址"):
            jenkins_login.get_url(config.local_jenkins_host)
        with allure.step("步骤2:输入用户名"):
            jenkins_login.input_username("chenbaozi-jenkins")
        with allure.step("步骤3:输入密码"):
            jenkins_login.input_password("chenbaozi2305")
        with allure.step("步骤4:点击登录"):
            jenkins_login.click_login()
        with allure.step("步骤5:校验结果"):
            result = jenkins_login.get_title()
            try:
                assert result == "工作台 [Jenkins]"
            except Exception as e:
                # 第一logger.error是为了记录日志，
                # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
                logger.error(f"校验失败，错误信息:{repr(e)}")
                raise e
            else:
                logger.info("校验成功")
