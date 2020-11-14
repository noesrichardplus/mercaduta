
from flask import Flask 
from flask_mysqldb import MySQL
from flask_mail import Mail
from mercaduta.config import LocalDB_Config,HerokuDB_Config,Mail_Config

db = MySQL() 
mail = Mail()

def create_app(): 
    app = Flask(__name__)
    app.secret_key = 'super secret key'

    #Configura la app en base a la configuracion que le pasamos como objeto
    app.config.from_object(HerokuDB_Config)
    app.config.from_object(Mail_Config)

    db.init_app(app)
    mail.init_app(app)

    

    from .auth.rutas import auth
    app.register_blueprint(auth)

    from .mercado.rutas import mercado
    app.register_blueprint(mercado)

    from .usuario.rutas import usuario 
    app.register_blueprint(usuario)

    return app