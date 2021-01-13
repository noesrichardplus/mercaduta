from mercaduta import db
import MySQLdb

def seleccionar_ofertas(categoria): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"SELECT * FROM ofertas WHERE categoria_oferta={categoria}")
    return cur.fetchall()


def seleccionar_oferta(id_oferta): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"SELECT * FROM ofertas WHERE id_oferta={id_oferta}")
    return cur.fetchone()

def crear_oferta(titulo,precio,categoria,condicion,descripcion,fecha,usuario): 
    cur = db.connection.cursor()
    cur.execute(f'''INSERT INTO ofertas(titulo_oferta,precio_oferta,categoria_oferta,condicion_oferta,des_oferta,fecha_oferta,usuario_oferta)
                    VALUES  ('{titulo}',{precio},'{categoria}',{condicion},'{descripcion}','{fecha}','{usuario}');''' )
    cur.connection.commit()                    

def mostar_solicitudes(email): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f'''SELECT solicitud.id_solicitud,solicitud.email_solicitante,ofertas.titulo_oferta, ofertas.usuario_oferta
                    FROM solicitud 
                    INNER JOIN ofertas ON solicitud.id_oferta = ofertas.id_oferta
                    WHERE ofertas.usuario_oferta = "{email}";''')
    return cur.fetchall() 

def ingresar_solicitud(email, id_oferta):
    cur = db.connection.cursor()
    cur.execute(f'''INSERT INTO solicitud(email_solicitante,id_oferta) VALUES("{email}",{id_oferta});''' )
    cur.connection.commit()


def aceptar_solicitud(id_solicitud): 
    cur = db.connection.cursor()
    cur.execute(f'''UPDATE solicitud SET estado = true WHERE id_solicitud = {id_solicitud};''' )
    cur.connection.commit()

def info_usuario_solicitado(email): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f'''SELECT solicitud.email_solicitante,ofertas.titulo_oferta, usuarios.email,usuarios.nombre,
                            usuarios.apellido,usuarios.celular,usuarios.contacto_alter
                    FROM solicitud 
                    INNER JOIN ofertas ON solicitud.id_oferta = ofertas.id_oferta
                    INNER JOIN usuarios  ON ofertas.usuario_oferta = usuarios.email
                    WHERE solicitud.email_solicitante = "{email}" AND solicitud.estado = true; ''')
    return cur.fetchall()


def existe_solicitud(email,id_oferta): 
    cur = db.connection.cursor()
    cur.execute(f"SELECT EXISTS( SELECT * FROM solicitud WHERE email_solicitante = '{email}' AND id_oferta = {id_oferta}  )")
    return cur.fetchone()[0]

def get_categorias(): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f'''SELECT * FROM categoria''')
    return cur.fetchall() 


def calificar_vendedor(comprador,vendedor,oferta,valor,descripcion): 
    cur = db.connection.cursor()
    cur.execute(f'''INSERT INTO calificacion(comprador_calificacion, vendedor_calificacion,oferta_calificacion,valor_calificacion,des_calificacion) 
                    VALUES ('{comprador}','{vendedor}','{oferta}','{valor}','{descripcion}')''' )
    cur.connection.commit()

def existe_calificacion(comprador,vendedor,oferta): 
    cur = db.connection.cursor()
    cur.execute(f"SELECT EXISTS( SELECT EXISTS( SELECT * FROM calificacion WHERE comprador_calificacion = '{comprador}' AND vendedor_calificacion = '{vendedor}' AND oferta_calificacion = '{oferta}' ))")
    return cur.fetchone()[0]

def calificaciones_vendedor_por_oferta(id_oferta): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    vendedor = cur.execute(f''' SELECT usuario_oferta FROM ofertas WHERE id_oferta={id_oferta}''')[0]['usuario_oferta']
    cur.execute(f''' SELECT valor_calificacion,des_calificacion FROM calificacion WHERE vendedor_calificacion = '{vendedor}' ''')
    return cur.fetchall()