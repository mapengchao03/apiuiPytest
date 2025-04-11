# -*- coding:utf-8 -*-
import allure
import pytest
from common.logger import logger
from config import config
from common.read_data import read_data
from page_object.local_jenkins.object_jenkins_login import JenkinsLogin

@allure.feature("jenkins登录功能")
class TestJenkinsLogin:

    @allure.story("登录")
    @allure.title("jenkins登录正确用例")
    @pytest.mark.parametrize('data', read_data.read_json("data/ui/local_jenkins/test_jenkins_login.json"))
    def test_001(self, driver, data):
        if 'error' in data:
            pytest.fail(f"数据加载失败: {data['error']}")
        """登录本地jenkins成功"""
        jenkins_login = JenkinsLogin(driver)
        username = data["username"]
        password = data["password"]
        expected_type = data["expected_type"]
        expected_value = data["expected_value"]
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
                if expected_type == "jenkins":
                    assert expected_value == result
                elif expected_type == "test":
                    assert expected_value == result
                else:
                    assert expected_value == result
            except Exception as e:
                # 第一logger.error是为了记录日志，
                # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
                logger.error(f"校验失败，错误信息:{repr(e)}")
                raise e
            else:
                logger.info("校验成功")
