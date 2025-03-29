# -*- coding:utf-8 -*-
import pytest, re
import allure
from common.logger import logger
from common.read_data import read_data
from page_object.baidu_search import baidu_search


@allure.feature("计算器功能")
class TestCalculator:

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
            assert result == 5, "加法结果错误"
        allure.attach("操作日志", "成功完成加法测试", allure.attachment_type.TEXT)

    @allure.story("减法运算")
    @allure.title("验证两个数相减的结果")
    @allure.description("这是一个详细的测试描述，可以包含HTML内容<br><b>例如加粗文本</b>")
    def test_subtract(self):
        """测试减法"""
        a, b = 5, 3
        result = a - b
        assert result == 2, "减法结果错误"

    @allure.feature("高级功能")
    @allure.story("乘法运算")
    def test_multiply(self):
        with allure.step("计算乘积"):
            assert 2 * 3 == 6


@allure.feature("测试TestOne类的功能")
class TestOne:

    @allure.story("测试加法1")
    @allure.title("测试加法001用例标题")
    @allure.description("描述用例的功能")
    def test_add01(self):
        a, b = 2,2
        assert 4 == a + b
        print('add function is success')
        logger.info("这是info了")

    @pytest.mark.skip('无条件跳过的用例')
    @allure.story("测试加法2")
    @allure.title("测试加法002用例的标题")
    @allure.description("描述用例的功能")
    def test_add02(self):
        a, b = 2, 2
        assert 4 == a + b
        print('add function is success')
        logger.info("这是info了")

    @allure.story("测试参数化")
    @allure.description("描述用例的功能")
    @allure.title("测试参数化用例标题")
    @pytest.mark.parametrize('a', [111111, 222222, 333333, 444444, 555555])
    def test_param(self, a):
        print(a)
        logger.warning("这是warning了")

    @allure.story("测试参数化")
    @allure.title('测试读取csv并输出为字典格式数据')
    @pytest.mark.parametrize('a', read_data.read_csv_dict("data/ui/baidu_search.csv"))
    def test_param01(self, a):
        print(a)
        logger.critical("这是critical了")

    @allure.story("测试参数化")
    @allure.title('测试读取csv并输出列表格式数据')
    @pytest.mark.parametrize('a', read_data.read_csv_list("data/ui/baidu_search.csv"))
    def test_param02(self, a):
        print(a)
        logger.error("这是error了")

    @allure.story("搜索selenium结果用例")
    @allure.title("测试搜索selenium结果用例标题")
    def test_001(self):
        """搜索"""
        with allure.step("步骤1:打开百度网址"):
            baidu_search.get_url("https://www.baidu.com/")
        with allure.step("步骤2:输入搜索条件"):
            baidu_search.input_search("selenium")
        with allure.step("步骤3:点击搜索按钮"):
            baidu_search.click_search()
        with allure.step("步骤4:查询数据"):
            result = baidu_search.get_source
        with allure.step("步骤5:校验结果"):
            assert result
        with allure.step("步骤6:日志记录"):
            logger.info("OK")

    @allure.story("测试搜索候选项用例")
    @allure.title("测试搜索候选用例标题")
    def test_002(self):
        """测试搜索候选"""
        with allure.step("步骤1:打开百度网址"):
            baidu_search.get_url("https://www.baidu.com/")
        with allure.step("步骤2:输入搜索条件"):
            baidu_search.input_search("selenium")
        with allure.step("步骤3:获取搜索候选数据"):
            result = baidu_search.imagine
        with allure.step("步骤4:校验结果"):
            if "selenium" in result[0]:
                assert True
            else:
                assert False
        with allure.step("步骤5:日志记录"):
            logger.info("ok")


if __name__ == '__main__':
    pass
