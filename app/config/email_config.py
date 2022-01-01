from fastapi_mailman.config import ConnectionConfig
import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '../../env/.env')
load_dotenv(dotenv_path)
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
SERVER = os.environ.get("SERVER")
EMAILPORT = os.environ.get("EMAILPORT")

config = ConnectionConfig(
    MAIL_USERNAME = EMAIL,
    MAIL_PASSWORD = PASSWORD,
    MAIL_BACKEND =  'smtp',
    MAIL_SERVER =  SERVER,
    MAIL_PORT = EMAILPORT,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_DEFAULT_SENDER = EMAIL,
    )
