import os

# 项目根路径
root_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 日志路径
log_path = os.path.join(root_path, 'logs')
# allure报告中展示环境配置信息的文件路径
allure_environment_path = os.path.join(root_path, 'allure_config', 'environment.properties')
# allure报告中展示执行器信息的文件路径
allure_executor_path = os.path.join(root_path, 'allure_config', 'executor.json')
# allure报告中展示自定义分类信息的文件路径
allure_categories_path = os.path.join(root_path, 'allure_config', 'categories.json')
# allure生成报告文件路径
allure_report = os.path.join(root_path, 'allure-report')
# allure生成结果文件路径
allure_results = os.path.join(root_path, 'allure-results')
# 当前运行环境
run_env = 'dev'
# run_env = 'test'
# run_env = 'uat'

if __name__ == '__main__':
    print(root_path)