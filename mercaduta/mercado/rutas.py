
from flask import Blueprint,render_template, session, url_for, redirect,request
from mercaduta.auth.utils import login_required
import mercaduta.db_query as db_query

mercado = Blueprint("mercado",__name__,template_folder='templates')


@mercado.route("/")
@login_required
def inicio(): 
    return render_template("inicio.html")



@mercado.route("/mercado/<categoria>")
@login_required
def mostrar_productos(categoria): 
    productos = db_query.seleccionar_ofertas(categoria)
    return render_template("productos.html",productos=productos)

@mercado.route("/mercado/descripcion/<id_oferta>")
@login_required
def descripcion(id_oferta): 
    producto = db_query.seleccionar_oferta(id_oferta)
    return render_template("descripcion.html",producto = producto)


@mercado.route("/comunicate")
@login_required
def comunicate(): 
    return render_template("comunicate.html")


@mercado.route("/crear-oferta",methods = ["GET","POST"]) 
def crear_oferta(): 
    if request.method == "POST": 
        titulo = request.form['titulo']
        precio = request.form['precio']
        categoria = request.form['categoria']
        condicion = request.form['condicion']
        if condicion == "Nuevo": 
            condcion = True
        else: 
            condcion = False
        descripcion = request.form['des']
        fecha = '2020-01-01'
        usuario = session['email']
        db_query.crear_oferta(titulo,precio,categoria,condicion,descripcion,fecha,usuario)            
        return redirect(url_for('mercado.inicio'))
    return render_template("crear_oferta.html")