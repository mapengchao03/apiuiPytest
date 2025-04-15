# -*- coding:utf-8 -*-
import pytest, os, shutil
from config import config

# 设置allure环境信息、自定义分类、执行器信息和历史报告
def allure_setting():
    # 将环境配置信息文件copy到allure-results
    shutil.copy(config.allure_environment_path, config.allure_results)
    # 将执自定义分类文件copy到allure-results
    shutil.copy(config.allure_categories_path, config.allure_results)
    # 将执行器信息文件copy到allure-results
    shutil.copy(config.allure_executor_path, config.allure_results)
    # 如果allure-results/history存在，则删除history文件夹
    if os.path.exists(config.allure_results_history_path):
        shutil.rmtree(config.allure_results_history_path)
    # 将历史报告copy到历史结果文件中，这样每次执行后，allure-results/history都会有新的历史报告数据
    shutil.copytree(config.allure_report_history_path, config.allure_results_history_path)

if __name__ == '__main__':
    pytest.main(["--alluredir=./allure-results", "--clean-alluredir"])
    allure_setting()
    # report会清除历史数据，所以需要手动执行allure generate命令生成报告
    os.system(r"allure generate ./allure-results -o ./allure-report --clean")
    # 如果需要在本地自动打开报告，请注释掉该行代码
    # os.system(r"allure serve ./allure-report")
