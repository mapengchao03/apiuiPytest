import os

# 项目根路径
root_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 日志路径
log_path = os.path.join(root_path, 'logs')
# 若不存在logs文件夹，则自动创建
if not os.path.exists(log_path):
    os.mkdir(log_path)
# allure报告中展示环境配置信息的文件路径
allure_environment_path = os.path.join(root_path, 'config', 'environment.properties')
# allure报告中展示执行器信息的文件路径
allure_executor_path = os.path.join(root_path, 'config', 'executor.json')
# allure报告中展示自定义分类信息的文件路径
allure_categories_path = os.path.join(root_path, 'config', 'categories.json')
# allure生成报告文件路径
allure_report = os.path.join(root_path, 'allure-report')
# allure生成结果文件路径
allure_results = os.path.join(root_path, 'allure-results')

# host
host = "https://www.baidu.com/"
# 邮件信息
EMAIL_INFO = {
    'username': '1084502012@qq.com',  # 切换成你自己的地址
    'password': 'QQ邮箱授权码',
    'smtp_host': 'smtp.qq.com',
    'smtp_port': 465
}
# 收件人
ADDRESSEE = [
    '1084502012@qq.com',
]

if __name__ == '__main__':
    print(root_path)