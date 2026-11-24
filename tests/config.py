import os

BASE_URL = os.environ.get("MALL_BASE_URL", "http://localhost:8080")      
ADMIN_USER = os.environ.get("MALL_ADMIN_USER", "admin")
ADMIN_PASS = os.environ.get("MALL_ADMIN_PASS", "macro123")

DB_HOST = os.environ.get("MALL_DB_HOST", "127.0.0.1")
DB_PORT = int(os.environ.get("MALL_DB_PORT", "3307"))   
DB_USER = os.environ.get("MALL_DB_USER", "root")
DB_PASS = os.environ.get("MALL_DB_PASS", "root")
DB_NAME = os.environ.get("MALL_DB_NAME", "mall")        
TIMEOUT = float(os.environ.get("MALL_TIMEOUT", "10"))
PORTAL_URL = os.environ.get("MALL_PORTAL_URL", "http://localhost:8085")
MEMBER_USER = os.environ.get("MALL_MEMBER_USER", "test")
MEMBER_PASS = os.environ.get("MALL_MEMBER_PASS", "123456")