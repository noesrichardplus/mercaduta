import os 
import sys 
import urllib.parse as urlparse
from flask import Config

class HerokuDB_Config(Config): 
    urlparse.uses_netloc.append('mysql')
    url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])
    MYSQL_DB = url.path[1:]
    MYSQL_USER = url.username
    MYSQL_PASSWORD = url.password
    MYSQL_HOST = url.hostname
    MYSQL_PORT = url.port


class LocalDB_Config(Config): 
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "mercaduta"


class Mail_Config(Config): 
    MAIL_SERVER = "smtp.live.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True 
    MAIL_USE_SSL = False 
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_DEFAULT_SENDER = os.environ['MAIL_USERNAME']