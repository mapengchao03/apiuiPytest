import pytest
from config import config
from common.read_data import read_data

# 获取全局配置的yaml数据，如base_url, auth_url等，并将其作为全局变量，供测试用例使用
# yaml路径为config/(dev/test/uat)_config.yaml
@pytest.fixture(scope="session")
def global_data():
    yaml_path = f"config/{config.run_env}_config.yaml"
    data =  read_data.read_yaml(yaml_path)
    return data