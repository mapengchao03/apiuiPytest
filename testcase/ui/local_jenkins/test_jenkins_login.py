# -*- coding:utf-8 -*-
import allure, pytest
from common.logger import logger
from common.read_data import read_data
from page_object.local_jenkins.object_jenkins_login import JenkinsLogin

@allure.feature("jenkins登录功能")
class TestJenkinsLogin:

    @allure.story("登录-读取json文件")
    @allure.title("jenkins登录用例")
    @pytest.mark.parametrize('data', read_data.read_json("data/ui/local_jenkins/test_jenkins_login.json"))
    def test_001(self, driver,global_data, data):
        if 'error' in data:
            pytest.fail(f"数据加载失败: {data['error']}")
        """登录本地jenkins成功"""
        jenkins_login = JenkinsLogin(driver)
        username = data["username"]
        password = data["password"]
        expected_type = data["expected_type"]
        expected_value = data["expected_value"]
        with allure.step("步骤1:打开本地jenkins网址"):
            jenkins_login.get_url(global_data['ui']["jenkins_url"])
        with allure.step("步骤2:输入用户名"):
            jenkins_login.input_username(username)
        with allure.step("步骤3:输入密码"):
            jenkins_login.input_password(password)
        with allure.step("步骤4:点击登录"):
            jenkins_login.click_login()
        with allure.step("步骤5:校验结果"):
            actual_result = jenkins_login.get_title()
            if expected_type == "assert_equal":
                jenkins_login.assert_equal(actual_result, expected_value)

    @allure.story("登录-读取yaml文件")
    @allure.title("jenkins登录用例")
    @pytest.mark.parametrize('data', read_data.read_yaml("data/ui/local_jenkins/test_jenkins_login.yaml"))
    def test_002(self, driver,global_data, data):
        if 'error' in data:
            pytest.fail(f"数据加载失败: {data['error']}")
        """登录本地jenkins成功"""
        jenkins_login = JenkinsLogin(driver)
        username = data["username"]
        password = data["password"]
        expected_type = data["expected_type"]
        expected_value = data["expected_value"]
        with allure.step("步骤1:打开本地jenkins网址"):
            jenkins_login.get_url(global_data['ui']["jenkins_url"])
        with allure.step("步骤2:输入用户名"):
            jenkins_login.input_username(username)
        with allure.step("步骤3:输入密码"):
            jenkins_login.input_password(password)
        with allure.step("步骤4:点击登录"):
            jenkins_login.click_login()
        with allure.step("步骤5:校验结果"):
            actual_result = jenkins_login.get_title()
            if expected_type == "assert_equal":
                jenkins_login.assert_equal(actual_result, expected_value)