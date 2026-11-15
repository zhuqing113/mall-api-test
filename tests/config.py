import os

BASE_URL = os.environ.get("MALL_BASE_URL", "http://localhost:8080")      # 填①:你 conftest 里现在 BASE 的值
ADMIN_USER = os.environ.get("MALL_ADMIN_USER", "admin")
ADMIN_PASS = os.environ.get("MALL_ADMIN_PASS", "macro123")

DB_HOST = os.environ.get("MALL_DB_HOST", "127.0.0.1")
DB_PORT = int(os.environ.get("MALL_DB_PORT", "3307"))   # 填②:宿主机端口
DB_USER = os.environ.get("MALL_DB_USER", "root")
DB_PASS = os.environ.get("MALL_DB_PASS", "rot")        # 填③:来自 docker-compose
DB_NAME = os.environ.get("MALL_DB_NAME", "mall")