
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