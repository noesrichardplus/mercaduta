from flask import Blueprint,render_template,request,session,redirect,url_for
from mercaduta.auth.utils import verify_passwd
import mercaduta.usuario.dbq as dbq

usuario = Blueprint('usuario',__name__,template_folder='templates')

@usuario.route('/miperfil')
def mi_perfil():
    email = session['email']
    usuario = dbq.get_usuario(email)
    return render_template("miperfil.html",usuario = usuario)



@usuario.route('/misofertas')
def mis_ofertas(): 
    email = session['email']
    ofertas = dbq.get_ofertas(email)
    return render_template("misofertas.html",ofertas = ofertas)


@usuario.route("/passwd-change", methods = ['POST'])
def passwd_change(): 
    actual_passwd = request.form['actual_passwd'] 
    new_passwd = request.form['new_passwd'] 
    repe_passwd = request.form['repe_passwd'] 
    if dbq.check_passwd(actual_passwd,session['email']) and verify_passwd(new_passwd): 
        dbq.change_passwd(session['email'],new_passwd)
        return redirect(url_for('usuario.mi_perfil'))
    else: 
        return "No se pudo cambiar la contra" 


@usuario.route("/eliminar-oferta-<id_oferta>")
def eliminar_oferta(id_oferta): 
    dbq.eliminar_oferta(id_oferta)
    return redirect(url_for('mercado.inicio'))