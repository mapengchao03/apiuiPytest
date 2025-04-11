# -*- coding:utf-8 -*-
import pytest
import allure
from common.logger import logger
from config import config
from common.read_data import read_data
from page_object.baidu_demo.object_baidu_search import BaiduSearch


@allure.feature("测试TestOne类的功能")
class TestOne:

    @allure.story("加法运算")
    @allure.title("验证两个数相加的结果")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("测试加法描述")
    @allure.link("https://example.com/calculator", name="测试需求文档，请点击")
    def test_add(self):
        """测试加法"""
        with allure.step("步骤1：输入两个数字"):
            a, b = 2, 3
        with allure.step("步骤2：执行加法操作"):
            result = a + b
        with allure.step("步骤3：验证结果"):
            try:
                assert result == 5
            except Exception as e:
                # 第一logger.error是为了记录日志，
                # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
                logger.error(f"校验失败，错误信息:{repr(e)}")
                raise e
            else:
                logger.info("校验成功")
        allure.attach("操作日志", "成功完成加法测试", allure.attachment_type.TEXT)

    @allure.story("减法运算")
    @allure.title("验证两个数相减的结果")
    @allure.description("这是一个详细的测试描述，可以包含HTML内容<br><b>例如加粗文本</b>")
    def test_subtract(self):
        """测试减法"""
        a, b = 5, 3
        result = a - b
        try:
            assert result == 3
        except Exception as e:
            # 第一logger.error是为了记录日志，
            # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
            logger.error(f"校验失败，错误信息:{repr(e)}")
            raise e
        else:
            logger.info("校验成功")

    @allure.feature("高级功能")
    @allure.story("乘法运算")
    def test_multiply(self):
        with allure.step("步骤1:计算乘积"):
            try:
                assert 2 * 3 == 6
            except Exception as e:
                # 第一logger.error是为了记录日志，
                # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
                logger.error(f"校验失败，错误信息:{repr(e)}")
                raise e
            else:
                logger.info("校验成功")

    @allure.story("测试加法1")
    @allure.title("测试加法001用例标题")
    @allure.description("描述用例的功能")
    def test_add01(self):
        a, b = 2,2
        try:
            assert 4 == a + b
        except Exception as e:
            # 第一logger.error是为了记录日志，第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
            logger.error(f"校验失败，错误信息:{repr(e)}")
            raise e
        else:
            logger.info("校验成功")

    @pytest.mark.skip('无条件跳过的用例')
    @allure.story("测试加法2")
    @allure.title("测试加法002用例的标题")
    @allure.description("描述用例的功能")
    def test_add02(self):
        a, b = 2, 2
        try:
            assert 4 == a + b
        except Exception as e:
            # 第一logger.error是为了记录日志，
            # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
            logger.error(f"校验失败，错误信息:{repr(e)}")
            raise e
        else:
            logger.info("校验成功")

    @allure.story("测试加法3")
    @allure.title("测试加法003用例的标题")
    @allure.description("描述用例的功能")
    def test_add03(self):
        a, b = 2, 3
        try:
            assert 4 == a + b
        except Exception as e:
            # 第一logger.error是为了记录日志，
            # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
            logger.error(f"校验失败，错误信息:{repr(e)}")
            raise e
        else:
            logger.info("校验成功")

    @allure.story("测试参数化")
    @allure.description("描述用例的功能")
    @allure.title("测试参数化用例标题")
    @pytest.mark.parametrize('a', [111111, 222222, 333333, 444444, 555555])
    def test_param(self, a):
        try:
            assert a
        except Exception as e:
            # 第一logger.error是为了记录日志，
            # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
            logger.error(f"校验失败，错误信息:{repr(e)}")
            raise e
        else:
            logger.info("校验成功")

    @allure.story("测试参数化")
    @allure.title('测试读取csv并输出为字典列表格式数据')
    @pytest.mark.parametrize('data', read_data.read_csv("data/ui/baidu_demo/test_baidu_demo.csv"))
    def test_param01(self, data):
        if 'error' in data:
            pytest.fail(f"数据加载失败: {data['error']}")
        try:
            assert data
        except Exception as e:
            # 第一logger.error是为了记录日志，
            # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
            logger.error(f"校验失败，错误信息:{repr(e)}")
            raise e
        else:
            logger.info("校验成功")

    @allure.story("测试参数化")
    @allure.title('测试读取yaml并输出列表格式数据')
    @pytest.mark.parametrize('data', read_data.read_yaml("data/ui/baidu_demo/test_baidu_demo.yaml"))
    def test_param02(self, data):
        if 'error' in data:
            pytest.fail(f"数据加载失败: {data['error']}")
        try:
            assert data
        except Exception as e:
            # 第一logger.error是为了记录日志，
            # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
            logger.error(f"校验失败，错误信息:{repr(e)}")
            raise e
        else:
            logger.info("校验成功")

    @allure.story("测试参数化")
    @allure.title('测试读取json并输出数据')
    @pytest.mark.parametrize('data', read_data.read_json("data/ui/baidu_demo/test_baidu_demo.json"))
    def test_param03(self, data):
        if 'error' in data:
            pytest.fail(f"数据加载失败: {data['error']}")
        try:
            assert data
        except Exception as e:
            # 第一logger.error是为了记录日志，
            # 第二rasie e抛异常是为了让 pytest知道这条用例执行错误了
            logger.error(f"校验失败，错误信息:{repr(e)}")
            raise e
        else:
            logger.info("校验成功")

    @allure.story("搜索selenium结果用例")
    @allure.title("测试搜索selenium结果用例标题")
    @pytest.mark.parametrize('data', read_data.read_json("data/ui/baidu_demo/test_baidu_search.json"))
    def test_001(self, driver, data):
        if 'error' in data:
            pytest.fail(f"数据加载失败: {data['error']}")
        baidu_search = BaiduSearch(driver)
        base_url = config.baidu_demo_host
        search_input = data["search_input"]
        expected_type = data["expected_type"]
        expected_value = data["expected_value"]
        with allure.step("步骤1:打开百度网址"):
            baidu_search.get_url(base_url)
        with allure.step("步骤2:输入搜索内容"):
            baidu_search.input_search(search_input)
        with allure.step("步骤3:点击搜索按钮"):
            baidu_search.click_search()
        with allure.step("步骤4:获取标题"):
            result = baidu_search.get_title()
        with allure.step("步骤5:校验结果"):
            try:
                if expected_type == "selenium":
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

if __name__ == '__main__':
    pass
