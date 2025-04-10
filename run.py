# coding=utf-8
import pytest, os, shutil
from config import config

# if __name__ == '__main__':
#     pytest.main(["--alluredir=./allure-results", "--clean-alluredir"])
#     shutil.copy(config.allure_environment_path, config.allure_results) # 将环境配置信息文件copy到allure-results
#     shutil.copy(config.allure_executor_path, config.allure_results) # 将执行器信息文件copy到allure-results
#     shutil.copy(config.allure_categories_path, config.allure_results) # 将执自定义分类文件copy到allure-results
#     os.system(r"allure generate ./allure-results -o ./allure-report --clean") # report会清除历史数据
#     os.system(r"allure generate ./allure-results -o ./allure-report ") # report会保留历史数据
#     os.system(r"allure serve ./allure-report") # 如果需要在本地自动打开报告，请注释掉该行代码

if __name__ == '__main__':
    pytest.main(["--alluredir=./allure-results", "--clean-alluredir"])
    shutil.copy(config.allure_environment_path, config.allure_results) # 将环境配置信息文件copy到allure-results
    shutil.copy(config.allure_categories_path, config.allure_results)  # 将执自定义分类文件copy到allure-results
    os.system(r"allure generate ./allure-results -o ./allure-report --clean") # report会清除历史数据
