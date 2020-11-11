import os 
import sys 
import urllib.parse as urlparse
from flask import Config
urlparse.uses_netloc.append('mysql')
url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])
class HerokuDB_Config(Config):     
    MYSQL_DB = url.path[1:]
    MYSQL_USER = url.username
    MYSQL_PASSWORD = url.password
    MYSQL_HOST = url.hostname
    MYSQL_PORT = url.port

'''
class LocalDB_Config(Config): 
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "mercaduta"
'''