import os
import mysql.connector

# Flask Configuration
SECRET_KEY = os.urandom(24)

# Base URL Configuration (for production deployment)
# Change this when deploying to production
BASE_URL = os.environ.get('BASE_URL', 'http://127.0.0.1:8000')
SERVER_NAME = os.environ.get('SERVER_NAME', None)  # e.g., 'yourdomain.com'

# MySQL Configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Dattu@1234'
MYSQL_DB = 'rohidas_footwear'

# Database Config Dictionary
DB_CONFIG = {
    'host': MYSQL_HOST,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'database': MYSQL_DB
}

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
