import os 
import sys 
import urllib.parse as urlparse

urlparse.uses_netloc.append('mysql')

url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])

BD = url.path[1:]
USER = url.username
PASSWD = url.password
HOST = url.hostname
PORT = url.port
