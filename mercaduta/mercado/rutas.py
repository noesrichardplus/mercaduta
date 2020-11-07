
from flask import Blueprint,render_template, session, url_for, redirect

import mercaduta.db_query as db_query

mercado = Blueprint("mercado",__name__,template_folder='templates')


@mercado.route("/inicio")
def inicio(): 
    if 'email' in session: 
        return render_template("inicio.html")
    return redirect('/')


@mercado.route("/mercado/<categoria>")
def mostrar_productos(categoria): 
    productos = db_query.seleccionar_ofertas(categoria)
    return render_template("productos.html",productos=productos)

@mercado.route("/mercado/descripcion/<id_ofer>")
def descripcion(id_ofer): 
    producto = db_query.seleccionar_oferta(id_ofer)
    return render_template("descripcion.html",producto = producto)


@mercado.route("/comunicate")
def comunicate(): 
    return render_template("comunicate.html")



