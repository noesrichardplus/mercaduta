from flask import render_template, redirect, request, Blueprint, url_for, session


from mercaduta.auth.utils import *
import mercaduta.db_query as db_query


auth = Blueprint('auth', __name__,template_folder='templates',static_folder='static',static_url_path="/%s"%__name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email_user']
        passwd = request.form['passwd_user']
        es_cuenta = db_query.verificar_cuenta(email, passwd)
        if es_cuenta:
            session['email'] = email
            return redirect(url_for('mercado.inicio'))
        return render_template('login.html')

    return render_template('login.html')


@auth.route('/regis', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        email = request.form['email']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        passwd = request.form['contra']
        repe_passwd = request.form['repe_contra']
        if verificar_email(email):
            if verificar_registro(nombre, apellido, passwd, repe_passwd):
                db_query.registrar_usuario(email, passwd, nombre, apellido)
            else:
                return "Las contras no se repiten bien"
        else:
            return "El email esta mal"

    return render_template('registro.html')


@auth.route("/logout")
def logout(): 
    session.clear() 
    return redirect(url_for("auth.login"))