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
        except requests.RequestException as e:
            logger.error("Request failed: %s", str(e))
            raise RuntimeError(f"API request error: {str(e)}") from e

        # 日志记录响应信息
        logger.info(f"接口Response响应结果: [{resp.status_code}] {resp.reason}")
        return resp

    def get(self, endpoint: str, **kwargs):
        return self._request('GET', endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request('POST', endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._request('PUT', endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request('DELETE', endpoint, **kwargs)

    def assert_status_code(
            self,
            response: requests.Response,
            expected_code: int
    ):
        """验证状态码"""
        assert response.status_code == expected_code

    def add_auth_header(self, token: str):
        """添加鉴权头 (示例)"""
        self.session.headers.update({'Authorization': f'Bearer {token}'})

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
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8", "Authorization":"123456"
    }
    base_api = BaseApi(url)
    login_res = base_api.post("/system/auth/authorize/hunan", json=json, headers=headers, verify=False)
    auth = login_res.json()['data']['accessToken']
    base_api.add_auth_header(auth)
    login_res1 = base_api.get("/survey/survey/getSurveyList", data=data, verify=False)