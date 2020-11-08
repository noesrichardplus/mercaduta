
from flask import Blueprint,render_template, session, url_for, redirect
from mercaduta.auth.utils import login_required
import mercaduta.db_query as db_query

mercado = Blueprint("mercado",__name__,template_folder='templates')


@mercado.route("/inicio")
@login_required
def inicio(): 
    return render_template("inicio.html")



@mercado.route("/mercado/<categoria>")
@login_required
def mostrar_productos(categoria): 
    productos = db_query.seleccionar_ofertas(categoria)
    return render_template("productos.html",productos=productos)

@mercado.route("/mercado/descripcion/<id_ofer>")
@login_required
def descripcion(id_ofer): 
    producto = db_query.seleccionar_oferta(id_ofer)
    return render_template("descripcion.html",producto = producto)


@mercado.route("/comunicate")
@login_required
def comunicate(): 
    return render_template("comunicate.html")



