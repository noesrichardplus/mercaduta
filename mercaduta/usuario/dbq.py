from mercaduta import db
import MySQLdb


def change_passwd(email,passwd): 
    cur = db.connection.cursor()
    cur.execute(f'''UPDATE usuarios SET passwd = '{passwd}' WHERE email = '{email}';''' )
    cur.connection.commit()


def get_usuario(email): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"SELECT * FROM usuarios WHERE email = '{email}'")
    return cur.fetchone()

def get_ofertas(email): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"SELECT * FROM ofertas WHERE usuario_oferta = '{email}'")
    return cur.fetchall()


    
def check_passwd(passwd,email): 
    cur = db.connection.cursor()
    cur.execute(f"SELECT EXISTS( SELECT * FROM usuarios WHERE email = '{email}' AND passwd = '{passwd}' )")
    return cur.fetchone()[0]