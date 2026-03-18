import os
import mysql.connector

SECRET_KEY = os.urandom(24)

BASE_URL = os.environ.get('BASE_URL', 'http://127.0.0.1:8000')
SERVER_NAME = os.environ.get('SERVER_NAME', None)

# ✅ Railway ENV variables use
MYSQL_HOST = os.getenv("MYSQLHOST")
MYSQL_USER = os.getenv("MYSQLUSER")
MYSQL_PASSWORD = os.getenv("MYSQLPASSWORD")
MYSQL_DB = os.getenv("MYSQLDATABASE")
MYSQL_PORT = int(os.getenv("MYSQLPORT", 3306))

DB_CONFIG = {
    'host': MYSQL_HOST,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'database': MYSQL_DB,
    'port': MYSQL_PORT
}

def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        port=MYSQL_PORT
    )