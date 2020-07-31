import os

from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME =  os.getenv("DB_SCEMA")
DB_TABLE = os.getenv("DB_TABLE")
DB_USER = os.getenv("DB_USER")
DB_PWD = os.getenv("DB_PWD")

