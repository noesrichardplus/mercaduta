
from flask import Flask 
from flask_mysqldb import MySQL
import mercaduta.config as config

db = MySQL() 

def create_app(): 
    app = Flask(__name__)
    app.secret_key = 'super secret key'
    app.config['MYSQL_HOST'] = config.HOST
    app.config['MYSQL_USER'] = config.USER
    app.config['MYSQL_PASSWORD'] = config.PASSWD
    app.config['MYSQL_DB'] = config.BD

    db.init_app(app)


    from .auth.rutas import auth
    app.register_blueprint(auth)

    from .mercado.rutas import mercado
    app.register_blueprint(mercado)

    from .usuario.rutas import usuario 
    app.register_blueprint(usuario)

    return app