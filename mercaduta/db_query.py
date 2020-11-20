
from mercaduta import db
import MySQLdb
def verificar_cuenta(email,passwd): 
    cur = db.connection.cursor()
    cur.execute(f"SELECT EXISTS( SELECT * FROM usuarios WHERE email = '{email}' AND passwd = '{passwd}')")
    return cur.fetchone()[0]


def registrar_usuario(email,passwd,nombre,apellido):
    cur = db.connection.cursor()
    cur.execute(f"INSERT INTO usuarios(email, passwd, nombre, apellido) VALUES ('{email}','{passwd}','{nombre}','{apellido}')")
    db.connection.commit()

def existe_usuario(email): 
    cur = db.connection.cursor()
    cur.execute(f"SELECT EXISTS( SELECT * FROM usuarios WHERE email = '{email}' )")
    return cur.fetchone()[0]

def seleccionar_ofertas(categoria): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"SELECT * FROM ofertas WHERE categoria_oferta='{categoria}'")
    return cur.fetchall()


def seleccionar_oferta(id_oferta): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"SELECT * FROM ofertas WHERE id_oferta={id_oferta}")
    return cur.fetchone()


def get_usuario(email): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"SELECT * FROM usuarios WHERE email = '{email}'")
    return cur.fetchone()

def get_ofertas(email): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"SELECT * FROM ofertas WHERE usuario_oferta = '{email}'")
    return cur.fetchall()

def crear_oferta(titulo,precio,categoria,condicion,descripcion,fecha,usuario): 
    cur = db.connection.cursor()
    cur.execute(f'''INSERT INTO ofertas(titulo_oferta,precio_oferta,categoria_oferta,condicion_oferta,des_oferta,fecha_oferta,usuario_oferta)
                    VALUES  ('{titulo}',{precio},'{categoria}',{condicion},'{descripcion}','{fecha}','{usuario}');''' )
    cur.connection.commit()                    

def mostar_solicitudes(email): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f'''SELECT solicitud.email_solicitante,ofertas.titulo_oferta, ofertas.usuario_oferta
                    FROM solicitud 
                    INNER JOIN ofertas ON solicitud.id_oferta = ofertas.id_oferta
                    WHERE ofertas.usuario_oferta = "{email}";''')
    return cur.fetchall() 

def ingresar_solicitud(email, id_oferta):
    cur = db.connection.cursor()
    cur.execute(f'''INSERT INTO solicitud(email_solicitante,id_oferta) VALUES("{email}",{id_oferta});''' )
    cur.connection.commit()


def aceptar_solicitud(id_solicitud): 
    pass