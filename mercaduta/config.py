import os 
import sys 
import urllib.parse as urlparse
from flask import Config

class HerokuDB_Config(Config):  
    def __init__(self): 
        urlparse.uses_netloc.append('mysql')
        self.url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])  
    @property
    def MYSQL_DATABASE_DB(self): 
        return self.url.path[1:]
    @property
    def MYSQL_DATABASE_USER(self): 
        return self.url.username
    @property
    def MYSQL_DATABASE_PASSWORD(self): 
        return self.url.password
    @property
    def MYSQL_DATABASE_HOST(self): 
        return self.url.hostname
    @property
    def MYSQL_DATABASE_PORT(self): 
        return self.url.port

     
    
'''
class LocalDB_Config(Config): 
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "mercaduta"
'''