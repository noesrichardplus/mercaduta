from flask import Blueprint,render_template,request,session,redirect,url_for
from mercaduta.auth.utils import verify_passwd
import mercaduta.db_query as db_query 

usuario = Blueprint('usuario',__name__,template_folder='templates')

@usuario.route('/miperfil')
def mi_perfil():
    email = session['email']
    usuario = db_query.get_usuario(email)
    return render_template("miperfil.html",usuario = usuario)



@usuario.route('/misofertas')
def mis_ofertas(): 
    email = session['email']
    ofertas = db_query.get_ofertas(email)
    return render_template("misofertas.html",ofertas = ofertas)


@usuario.route("/passwd-change", methods = ['POST'])
def passwd_change(): 
    actual_passwd = request.form['actual_passwd'] 
    new_passwd = request.form['new_passwd'] 
    repe_passwd = request.form['repe_passwd'] 
    if db_query.check_passwd(actual_passwd,session['email']) and verify_passwd(new_passwd): 
        db_query.change_passwd(session['email'],new_passwd)
        return redirect(url_for('usuario.mi_perfil'))
    else: 
        return "No se pudo cambiar la contra" 
