from flask import Blueprint,render_template,request,session

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
