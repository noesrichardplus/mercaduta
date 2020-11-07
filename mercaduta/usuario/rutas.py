from flask import Blueprint,render_template,request

import mercaduta.db_query as db_query 

usuario = Blueprint('usuario',__name__,template_folder='templates')

@usuario.route('/miperfil')
def mi_perfil():
    email = 'rcarrion3406@uta.edu.ec' 
    usuario = db_query.get_usuario(email)
    return render_template("miperfil.html",usuario = usuario)



@usuario.route('/misofertas')
def mis_ofertas(): 
    email = 'rcarrion3406@uta.edu.ec'
    ofertas = db_query.get_ofertas(email)
    return render_template("misofertas.html",ofertas = ofertas)
