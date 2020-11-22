
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



