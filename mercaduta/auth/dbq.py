
from mercaduta import db
import MySQLdb

def registrar_usuario(email,passwd,nombre,apellido):
    cur = db.connection.cursor()
    cur.execute(f"INSERT INTO usuarios(email, passwd, nombre, apellido) VALUES ('{email}','{passwd}','{nombre}','{apellido}')")
    db.connection.commit()



