import pytest
from common.logger import logger
from base.baseapi import BaseApi
from config import config


@pytest.fixture(scope="session")
def api_client():
    base_api = BaseApi(config.countryside_host)
    _res = base_api.post(config.auth_url, json=config.auth_json, verify=False)
    auth = _res.json()['data']['accessToken']
    base_api.add_auth_header(auth)
    yield base_api
    base_api.session.close()