import re
from flask import redirect,url_for,session,current_app
from flask_mail import Message
from mercaduta import mail
from functools import wraps
import threading 

def verificar_email(email): 
    regex = "[^@]."
    no_empieza = re.match(regex,email)
    si_hay = re.search("@",email)
    if no_empieza and si_hay:
        email_divi = re.split("@",email)
        if email_divi[1] == "uta.edu.ec": 
            return True
        else: 
            return False
    else: 
        return False

def verificar_registro(nombre,apellido,passwd,repe_passwd): 
    regex_nombres = "[^\ ][a-zA-Z]"

    regex = "^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?.&])[A-Za-z\d@$!#%*?.&]{6,20}$"

    pat = re.compile(regex)
    
    nombre_valido = re.search(regex_nombres,nombre)
    apellido_valido = re.search(regex_nombres,apellido)
    passwd_valida = re.search(pat, passwd) 
    
    if nombre_valido and apellido_valido and passwd_valida: 
        if passwd == repe_passwd: 
            return True
        else: 
            return False
    else: 
        return False

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