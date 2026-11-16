import requests
from config import BASE_URL


class ApiClient:
    def __init__(self, headers=None, timeout=10):
        self.base_url = BASE_URL
        self.headers = headers
        self.timeout = timeout

    def get(self, path, **kwargs):
        return requests.get(f"{self.base_url}{path}",
                            headers=self.headers,      # 填①:用对象里记住的哪个
                            timeout=self.timeout,      # 填②:同上
                            **kwargs)

    def post(self, path, **kwargs):
        return requests.post(f"{self.base_url}{path}",
                             headers=self.headers,
                             timeout=self.timeout,
                             **kwargs)