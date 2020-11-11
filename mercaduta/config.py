import os 
import sys 
import urllib.parse as urlparse
from flask import Config
urlparse.uses_netloc.append('mysql')
url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])
class HerokuDB_Config(Config):     
    MYSQL_DATABASE_DB = url.path[1:]
    MYSQL_DATABASE_USER = url.username
    MYSQL_DATABASE_PASSWORD	 = url.password
    MYSQL_DATABASE_HOST = url.hostname
    MYSQL_DATABASE_PORT = url.port

'''
class LocalDB_Config(Config): 
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "mercaduta"
'''