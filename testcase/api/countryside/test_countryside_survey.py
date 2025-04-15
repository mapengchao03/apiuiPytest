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
            try:
                result = res.status_code
                if expected_type == "status_code1":
                    assert result == expected_value
                elif expected_type == "status_code2":
                    assert result == expected_value
                else:
                    assert result == expected_value
            except Exception as e:
                # 第一logger.error是为了记录日志，
                # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
                logger.error(f"校验失败，错误信息:{str(e)}")
                raise e
            else:
                logger.info("校验成功")

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
            try:
                result = res.status_code
                if expected_type == "status_code1":
                    assert result == expected_value
                elif expected_type == "status_code2":
                    assert result == expected_value
                else:
                    assert result == expected_value
            except Exception as e:
                # 第一logger.error是为了记录日志，
                # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
                logger.error(f"校验失败，错误信息:{str(e)}")
                raise e
            else:
                logger.info("校验成功")