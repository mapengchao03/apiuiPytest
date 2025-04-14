import pytest
from base.baseapi import BaseApi

# 获取全局的api_client对象并添加auth到headers中，用于调用接口
@pytest.fixture(scope="session")
def api_client(global_data):
    base_api = BaseApi(global_data['api']['base_url'])
    _res = base_api.post(global_data['api']['auth_url'], json=global_data['api']['auth_json'], verify=False)
    auth = _res.json()['data']['accessToken']
    base_api.add_auth_header(auth)
    yield base_api
    base_api.session.close()
