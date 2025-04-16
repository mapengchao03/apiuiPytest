# -*- coding:utf-8 -*-
import allure, pytest
from common.logger import logger
from common.read_data import read_data

@allure.feature("countryside问卷功能")
class TestCountrysideSurvey:

    @allure.story("全部问卷-读取json文件")
    @allure.title("全部问卷查询")
    @pytest.mark.parametrize('data', read_data.read_json("data/api/countryside/test_countryside_survey.json"))
    def test_001(self, api_client, global_data, data):
        if 'error' in data:
            pytest.fail(f"数据加载失败: {data['error']}")
        expected_type = data["expected_type"]
        expected_value = data["expected_value"]
        with allure.step("步骤1:查询"):
            res = api_client.get(global_data['api']['survey_url'], data=data, verify=False)
        with allure.step("步骤5:校验结果"):
            actual_result = res.status_code
            if expected_type == "assert_equal":
                api_client.assert_equal(actual_result, expected_value)

    @allure.story("全部问卷-读取yaml文件")
    @allure.title("全部问卷查询")
    @pytest.mark.parametrize('data', read_data.read_yaml("data/api/countryside/test_countryside_survey.yaml"))
    def test_002(self, api_client, global_data, data):
        if 'error' in data:
            pytest.fail(f"数据加载失败: {data['error']}")
        expected_type = data["expected_type"]
        expected_value = data["expected_value"]
        with allure.step("步骤1:查询"):
            res = api_client.get(global_data['api']['survey_url'], data=data, verify=False)
        with allure.step("步骤5:校验结果"):
            actual_result = res.status_code
            if expected_type == "assert_equal":
                api_client.assert_equal(actual_result, expected_value)