from flask import Blueprint,render_template, session, url_for, redirect,request
from mercaduta.auth.utils import login_required
import mercaduta.mercado.dbq as dbq

mercado = Blueprint("mercado",__name__,template_folder='templates',
                static_folder='static',static_url_path="/%s"%__name__)


@mercado.route("/")
@login_required
def inicio(): 
    return render_template("inicio.html")



@mercado.route("/mercado/<categoria>")
@login_required
def mostrar_productos(categoria): 
    productos = dbq.seleccionar_ofertas(categoria)
    return render_template("productos.html",productos=productos)

@mercado.route("/mercado/todos")
@login_required
def mostrar_todos_productos(): 
    productos = dbq.seleccionar_todas_ofertas()
    return render_template("productos.html",productos=productos)

@mercado.route("/mercado/descripcion/<id_oferta>")
@login_required
def descripcion(id_oferta): 
    producto = dbq.seleccionar_oferta(id_oferta)
    calificaciones = dbq.calificaciones_vendedor_por_oferta(id_oferta)
    return render_template("descripcion.html",producto = producto, calificaciones = calificaciones)


@mercado.route("/comunicate")
@login_required
def comunicate(): 
    return render_template("comunicate.html")


@mercado.route("/crear-oferta",methods = ["GET","POST"]) 
@login_required
def crear_oferta(): 
    if request.method == "POST": 
        titulo = request.form['titulo']
        precio = request.form['precio']
        categoria = request.form['categoria']
        condicion = request.form['condicion']
        descripcion = request.form['des']
        fecha = '2020-01-01'
        usuario = session['email']
        dbq.crear_oferta(titulo,precio,categoria,condicion,
                              descripcion,fecha,usuario)            
        return redirect(url_for('mercado.inicio'))
    return render_template("crear_oferta.html", categorias = dbq.get_categorias())


@mercado.route("/solicitudes") 
@login_required
def solicitudes():
    solicitudes = dbq.mostar_solicitudes(session['email'])
    info_solicitudes = dbq.info_usuario_solicitado(session['email'])
    return render_template("solicitudes.html", solicitudes = solicitudes, info_solicitudes = info_solicitudes)


@mercado.route("/solicitar-datos-<id_oferta>")
@login_required
def solicitar_datos(id_oferta): 
    if not dbq.existe_solicitud(session['email'],id_oferta): 
        dbq.ingresar_solicitud(session['email'],id_oferta)
        return render_template("solicitar_datos.html")
    return "Ya solicitaste estos datos" 

@mercado.route("/aceptar-solicitud-<id_solicitud>")
@login_required
def aceptar_solicitud(id_solicitud): 
    dbq.aceptar_solicitud(id_solicitud)
    return redirect(url_for('mercado.solicitudes'))

@mercado.route("/calificar-<vendedor>-<oferta>", methods = ['GET', 'POST'])
@login_required
def calificar_vendedor(vendedor,oferta): 
    if request.method == "POST" and not dbq.existe_calificacion(session['email'],vendedor,oferta): 
        dbq.calificar_vendedor(session['email'],vendedor,oferta,request.form['valor'],request.form['des'])
        return redirect(url_for('mercado.inicio'))
    return render_template('calificar.html',vendedor = vendedor, oferta = oferta)


@mercado.route("/eliminar-solicitud-<id_solicitud>")
@login_required
def eliminar_solicitud(id_solicitud): 
    dbq.eliminar_solicitud(id_solicitud)
    return redirect(url_for('mercado.solicitudes'))
