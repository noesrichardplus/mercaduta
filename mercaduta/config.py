import os 
import sys 
import urllib.parse as urlparse
from flask import Config

class HerokuDB_Config(Config): 
    urlparse.uses_netloc.append('mysql')
    url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])
    BD = url.path[1:]
    USER = url.username
    PASSWD = url.password
    HOST = url.hostname
    PORT = url.port

'''
class LocalDB_Config(Config): 
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "mercaduta"
'''