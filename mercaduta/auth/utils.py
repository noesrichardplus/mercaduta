import re
from flask import redirect,url_for,session,current_app
from flask_mail import Message
from mercaduta import mail
from functools import wraps
import threading 


def verify_passwd(passwd): 
    regex = "^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?.&])[A-Za-z\d@$!#%*?.&]{6,20}$"
    pat = re.compile(regex)
    return re.search(pat, passwd) 

def enviar_email_async(app,msg): 
    with app.app_context(): 
        mail.send(msg)

def enviar_email(to,code): 
    app = current_app._get_current_object()
    msg = Message("Codigo de verificacion mercadUTA",recipients=[to])
    msg.body = f"El codigo para verificar tu cuenta es: {code}" 
    hilo = threading.Thread(target=enviar_email_async, args=[app,msg])
    hilo.start()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function