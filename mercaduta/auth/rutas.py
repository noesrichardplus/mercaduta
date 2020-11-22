from flask import render_template, redirect, request, Blueprint, url_for, session
from flask_mail import Message
from mercaduta import mail
from mercaduta.auth.utils import *
import mercaduta.auth.dbq as dbq
import random


auth = Blueprint('auth', __name__,template_folder='templates',
                static_folder='static',static_url_path="/%s"%__name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email_user']
        passwd = request.form['passwd_user']
        es_cuenta = dbq.verificar_cuenta(email, passwd)
        if es_cuenta:
            session['email'] = email
            return redirect(url_for('mercado.inicio'))
        return render_template('login.html')

    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        passwd = request.form['contra']
        repe_passwd = request.form['repe_contra']
        if not dbq.existe_usuario(email):
            if (verificar_email(email) and 
                verificar_registro(nombre, apellido, passwd, repe_passwd)):
                session['signup_email'] = email
                session['signup_passwd'] = passwd
                session['signup_nombre'] = nombre
                session['signup_apellido'] = apellido
                return redirect(url_for('auth.signup_verification'))
            else:
                return "Las contras no se repiten bien o no cumplen con las normas"
        else:
            return "El email esta mal"

    return render_template('signup.html')


@auth.route("/logout")
def logout(): 
    session.clear() 
    return redirect(url_for("auth.login"))

@auth.route("/signup-verification", methods= ['GET','POST'])
def signup_verification(): 
    if request.method == "POST": 
        if request.form['verification_code'] == str(session['code']): 
            dbq.registrar_usuario(session['signup_email'],session['signup_passwd'],
                                session['signup_nombre'],session['signup_apellido'])
            return redirect(url_for("auth.logout"))
        else: 
            return render_template("signup_verification.html",email = session['signup_email'])
    session['code'] = random.randint(1000,10000)
    enviar_email(session['signup_email'],session['code'])
    return render_template("signup_verification.html",email = session['signup_email'])
    