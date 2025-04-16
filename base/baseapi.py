import requests
from typing import Optional, Dict, Any, Union
from common.logger import logger

class BaseApi:
    def __init__(
            self,
            base_url: str,
            timeout: int = 10,
            default_headers: Optional[Dict] = None
    ):
        if default_headers is None:
            default_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8"}
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(default_headers or {})

    def _request(
            self,
            method: str,
            endpoint: str,
            params: Optional[Dict] = None,
            json: Optional[Dict] = None,
            data: Optional[Union[Dict, str]] = None,
            headers: Optional[Dict] = None,
            **kwargs
    ):
        """统一请求入口"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = headers or {}

        # 合并会话级 headers 和本次请求 headers
        merged_headers = {**self.session.headers, **headers}

        # 日志记录请求信息
        logger.info(f'Request：method={method.upper()}, url={url},params={params},'
                    f'data={data},json={json},headers={merged_headers}'
                    )

        try:
            resp = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json,
                data=data,
                headers=merged_headers,
                timeout=self.timeout,
                **kwargs
            )
            status_code = resp.status_code
            rep_reason = resp.reason
            # 如果状态码不是200，抛出异常
            if status_code != 200:
                logger.error(f"Request failed: status code {status_code}, reason {rep_reason}")
                raise Exception(f"Request failed: status code {status_code}, reason {rep_reason}")
        except requests.RequestException as e:
            logger.error("Request failed: %s", str(e))
            raise e

        # 日志记录响应信息
        logger.info(f"接口Response响应结果: [{status_code}] {rep_reason}")
        return resp

    def get(self, endpoint: str, **kwargs):
        return self._request('GET', endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request('POST', endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._request('PUT', endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request('DELETE', endpoint, **kwargs)

    def add_auth_header(self, token: str):
        """添加鉴权头 (示例)"""
        self.session.headers.update({'Authorization': f'Bearer {token}'})

    # 断言相等,兼容各种类型数据(字符串，整型，字典，列表)
    @staticmethod
    def assert_equal(actual_result, expected_value):
        try:
            assert actual_result == expected_value,f"实际结果{actual_result}不等于预期结果{expected_value}"
            logger.info(f"实际结果{actual_result}等于预期结果{expected_value}")
        except Exception as e:
            logger.error(f"断言失败，错误信息{str(e)}" )
            raise e

    # 断言不相等
    @staticmethod
    def assert_not_equal(actual_result, expected_value):
        try:
            assert actual_result != expected_value,f"实际结果{actual_result}等于预期结果{expected_value}"
            logger.info(f"实际结果{actual_result}不等于预期结果{expected_value}")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言大于
    @staticmethod
    def assert_greater(actual_result, expected_value):
        try:
            assert actual_result > expected_value,f"实际结果{actual_result}小于或等于预期结果{expected_value}"
            logger.info(f"实际结果{actual_result}大于预期结果{expected_value}")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言小于
    @staticmethod
    def assert_less(actual_result, expected_value):
        try:
            assert actual_result < expected_value,f"实际结果{actual_result}大于或等于预期结果{expected_value}"
            logger.info(f"实际结果{actual_result}小于预期结果{expected_value}")
        except Exception as e:
                logger.error(f"断言失败,错误信息{str(e)}" )
                raise e

    # 断言布尔值true
    @staticmethod
    def assert_true(actual_result):
        try:
            assert actual_result is True,f"实际结果{actual_result}为False"
            logger.info(f"实际结果{actual_result}为True")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言布尔值false
    @staticmethod
    def assert_false(actual_result):
        try:
            assert actual_result is False,f"实际结果{actual_result}为True"
            logger.info(f"实际结果{actual_result}为False")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言包含
    @staticmethod
    def assert_in(actual_result, expected_value):
        try:
            assert expected_value in actual_result,f"预期结果{expected_value}不在实际结果{actual_result}中"
            logger.info(f"预期结果{expected_value}在实际结果{actual_result}中")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言不包含
    @staticmethod
    def assert_not_in(actual_result, expected_value):
        try:
            assert expected_value not in actual_result,f"预期结果{expected_value}在实际结果{actual_result}中"
            logger.info(f"预期结果{expected_value}不在实际结果{actual_result}中")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言是None
    @staticmethod
    def assert_is_none(actual_result):
        try:
            assert actual_result is None,f"实际结果{actual_result}不为None"
            logger.info(f"实际结果{actual_result}为None")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言不是None
    @staticmethod
    def assert_is_not_none(actual_result):
        try:
            assert actual_result is not None,f"实际结果{actual_result}为None"
            logger.info(f"实际结果{actual_result}不为None")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言空字符串
    @staticmethod
    def assert_empty_string(actual_result):
        try:
            assert actual_result == '',f"实际结果{actual_result}不为空字符串"
            logger.info(f"实际结果{actual_result}为空字符串")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言长度相等
    @staticmethod
    def assert_length_equal(actual_result, expected_value):
        try:
            assert len(actual_result) == expected_value,f"实际结果{actual_result}的长度不等于预期结果{expected_value}"
            logger.info(f"实际结果{actual_result}的长度等于预期结果{expected_value}")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言长度不相等
    @staticmethod
    def assert_length_not_equal(actual_result, expected_value):
        try:
            assert len(actual_result) != expected_value,f"实际结果{actual_result}的长度等于预期结果{expected_value}"
            logger.info(f"实际结果{actual_result}的长度不等于预期结果{expected_value}")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言长度大于
    @staticmethod
    def assert_length_greater(actual_result, expected_value):
        try:
            assert len(actual_result) > expected_value,f"实际结果{actual_result}的长度小于或等于预期结果{expected_value}"
            logger.info(f"实际结果{actual_result}的长度大于预期结果{expected_value}")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言长度小于
    @staticmethod
    def assert_length_less(actual_result, expected_value):
        try:
            assert len(actual_result) < expected_value,f"实际结果{actual_result}的长度大于或等于预期结果{expected_value}"
            logger.info(f"实际结果{actual_result}的长度小于预期结果{expected_value}")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言类型相等
    @staticmethod
    def assert_type_equal(actual_result, expected_value):
        try:
            assert type(actual_result) == expected_value,f"实际结果{actual_result}的类型不等于预期结果{expected_value}"
            logger.info(f"实际结果{actual_result}的类型等于预期结果{expected_value}")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言类型不相等
    @staticmethod
    def assert_type_not_equal(actual_result, expected_value):
        try:
            assert type(actual_result) != expected_value,f"实际结果{actual_result}的类型等于预期结果{expected_value}"
            logger.info(f"实际结果{actual_result}的类型不等于预期结果{expected_value}")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言存在某个键
    @staticmethod
    def assert_key_in(actual_result, expected_value):
        try:
            assert expected_value in actual_result.keys(),f"预期结果{expected_value}不在实际结果{actual_result}的键中"
            logger.info(f"预期结果{expected_value}在实际结果{actual_result}的键中")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言不存在某个键
    @staticmethod
    def assert_key_not_in(actual_result, expected_value):
        try:
            assert expected_value not in actual_result.keys(),f"预期结果{expected_value}在实际结果{actual_result}的键中"
            logger.info(f"预期结果{expected_value}不在实际结果{actual_result}的键中")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言存在某个值
    @staticmethod
    def assert_value_in(actual_result, expected_value):
        try:
            assert expected_value in actual_result.values(),f"预期结果{expected_value}不在实际结果{actual_result}的值中"
            logger.info(f"预期结果{expected_value}在实际结果{actual_result}的值中")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言不存在某个值
    @staticmethod
    def assert_value_not_in(actual_result, expected_value):
        try:
            assert expected_value not in actual_result.values(),f"预期结果{expected_value}在实际结果{actual_result}的值中"
            logger.info(f"预期结果{expected_value}不在实际结果{actual_result}的值中")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

    # 断言集合完全相等
    @staticmethod
    def assert_set_equal(actual_result, expected_value):
        try:
            assert set(actual_result) == set(expected_value),f"预期结果{expected_value}在实际结果{actual_result}的值中"
            logger.info(f"实际结果{actual_result}的集合等于预期结果{expected_value}")
        except Exception as e:
            logger.error(f"断言失败,错误信息{str(e)}" )
            raise e

if __name__ == '__main__':
    # 以下是测试代码
    # post请求接口
    url = 'https://203.83.237.82:30763/hnweb/api/proxy/'
    json = {
        "tokenCode":"c6zY8PJCO4+lD3RMWcuZS2lE/cT8JmrbZbbeEDxTSNZGEEZl5bEViYXXcaqAmsRDeEih6njMJfZFTgmsJbQ6N7FaCZgejZtxyxVjEEaev//xgh4ylRHERSC8Mkk545j2J+8zH0Q1TyTfd+OdpDKxTcJ2lxJrB1sGpQKEQivRp/4nAZcnsnYDkXl36H1+0D09GOgKR3nm3Ji8IH5GRhAIq9I3XZKNy9gpzVFmSA0skiLRCWAQYP8zuq+lN3ZEW9miW72REk31nZjVqUjnspwzcBnonFQ1ySJlNsfilRDDJs8mIcRXcU1SPJAXkKyjv4hy9MrHkm96mwn0uJOBIlpOCY3giQ1satS0CEItN31G9ysn3uBfkX2jawqAfmKwb2tkp+PqaphU99c5ppHhmLdaDtfHFV4ube5CMNDUfH2mXt+yHPU3TWqa8HAv+ZIhNRbomihvjtmsMa3j0FwbIAS2pCE/bToZXpq3QfOT/Jh6jaW65OztEc+X5xY7Kp5hPeRm"
    }
    data = {
        "pageNum": 1,"pageSize": 20,"publishCode":'',"surveyName":'',"surveyType": [0, 2],
        "orderByColumn": "createTime","isAsc": "desc","regionCode":''
    }
    base_api = BaseApi(url)
    login_res = base_api.post("/system/auth/authorize/hunan", json=json, verify=False)
    auth = login_res.json()['data']['accessToken']
    base_api.add_auth_header(auth)
    login_res1 = base_api.get("/survey/survey/getSurveyList", data=data, verify=False)