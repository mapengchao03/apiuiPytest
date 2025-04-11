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

# host--UI
baidu_demo_host = "https://www.baidu.com/"
local_jenkins_host = "http://localhost:8081/"
# host--API
countryside_host = 'https://203.83.237.82:30763/hnweb/api/proxy/'
# auth--URL/json
auth_url = '/system/auth/authorize/hunan'
auth_json = {
        "tokenCode":"c6zY8PJCO4+lD3RMWcuZS2lE/cT8JmrbZbbeEDxTSNZGEEZl5bEViYXXcaqAmsRDeEih6njMJfZFTgmsJbQ6N7FaCZgejZtxy"
                    "xVjEEaev//xgh4ylRHERSC8Mkk545j2J+8zH0Q1TyTfd+OdpDKxTcJ2lxJrB1sGpQKEQivRp/4nAZcnsnYDkXl36H1+0D09GOg"
                    "KR3nm3Ji8IH5GRhAIq9I3XZKNy9gpzVFmSA0skiLRCWAQYP8zuq+lN3ZEW9miW72REk31nZjVqUjnspwzcBnonFQ1ySJlNsfil"
                    "RDDJs8mIcRXcU1SPJAXkKyjv4hy9MrHkm96mwn0uJOBIlpOCY3giQ1satS0CEItN31G9ysn3uBfkX2jawqAfmKwb2tkp+Pqaph"
                    "U99c5ppHhmLdaDtfHFV4ube5CMNDUfH2mXt+yHPU3TWqa8HAv+ZIhNRbomihvjtmsMa3j0FwbIAS2pCE/bToZXpq3QfOT/Jh6"
                    "jaW65OztEc+X5xY7Kp5hPeRm"
    }

# 数据库信息

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