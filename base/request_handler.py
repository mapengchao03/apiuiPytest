import requests


class RequestHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def request_response(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method,url, params=params, data=data, json=json, headers=headers,**kwargs)

    def close_session(self):
        """关闭session"""
        self.session.close()


if __name__ == '__main__':
    # 以下是测试代码
    # post请求接口
    url = 'https://tool.lu/uuid/ajax.html'
    data = {
        "num": 3
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.138 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://tool.lu/uuid/"
    }
    req = RequestHandler()
    login_res = req.request_response("post", url, data=data)
    print(login_res.status_code)
    print(login_res.encoding)
    print(login_res.content)