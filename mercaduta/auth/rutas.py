from flask import render_template, redirect, request, Blueprint, url_for, session
from flask_mail import Message
from mercaduta import mail
from mercaduta.auth.utils import *
from mercaduta.clases.usuario import Usuario
import mercaduta.auth.dbq as dbq
import random


auth = Blueprint('auth', __name__,template_folder='templates',
                static_folder='static',static_url_path="/%s"%__name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario()
        usuario.set_email(request.form['email_user'])
        usuario.set_passwd(request.form['passwd_user'])
        if usuario.valido():
            session['email'] = usuario.get_email()
            return redirect(url_for('mercado.inicio'))
        return render_template('login.html')

    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nuevo_usuario = Usuario()
        nuevo_usuario.set_email(request.form['email'])
        nuevo_usuario.set_nombre(request.form['nombre'])
        nuevo_usuario.set_apellido(request.form['apellido'])
        nuevo_usuario.set_passwd(request.form['contra'])
        repe_passwd = request.form['repe_contra']

        if not nuevo_usuario.existe():
            if (nuevo_usuario.validar_email() and 
                nuevo_usuario.validar_atributos(repe_passwd)):
                '''
                session['signup_email'] = nuevo_usuario.get_email()
                session['signup_passwd'] = nuevo_usuario.get_passwd()
                session['signup_nombre'] = nuevo_usuario.get_nombre()
                session['signup_apellido'] = nuevo_usuario.get_apellido()
                '''
                return redirect(url_for('auth.signup_verification', nuevo_usuario = nuevo_usuario))
            else:
                return "Las contras no se repiten bien o no cumplen con las normas"
        else:
            return "El email esta mal"

    return render_template('signup.html')


@auth.route("/logout")
def logout(): 
    session.clear() 
    return redirect(url_for("auth.login"))

@auth.route("/signup-verification-<nuevo_usuario>", methods= ['GET','POST'])
def signup_verification(nuevo_usuario): 
    if request.method == "POST": 
        if request.form['verification_code'] == str(session['code']): 
            nuevo_usuario.registrar_usuario()
            '''
            dbq.registrar_usuario(session['signup_email'],session['signup_passwd'],
                                session['signup_nombre'],session['signup_apellido'])
                                '''
            return redirect(url_for("auth.logout"))
        else: 
            return render_template("signup_verification.html",email = session['signup_email'])
    session['code'] = random.randint(1000,10000)
    enviar_email(session['signup_email'],session['code'])
    return render_template("signup_verification.html",email = session['signup_email'])
    