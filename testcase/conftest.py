import pytest
from config import config
from common.read_data import read_data

# 获取全局的配置数据，如base_url, auth_url等
@pytest.fixture(scope="session")
def global_data():
    yaml_path = f"config/{config.run_env}_config.yaml"
    data =  read_data.read_yaml(yaml_path)
    return data