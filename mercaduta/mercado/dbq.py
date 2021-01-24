from mercaduta import db
import MySQLdb








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
    cur.execute(f"SELECT EXISTS( SELECT * FROM calificacion WHERE comprador_calificacion = '{comprador}' AND vendedor_calificacion = '{vendedor}' AND oferta_calificacion = '{oferta}' )")
    return cur.fetchone()[0]

def calificaciones_vendedor_por_oferta(id_oferta): 
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f''' SELECT usuario_oferta FROM ofertas WHERE id_oferta={id_oferta}''')
    vendedor = cur.fetchall()[0]['usuario_oferta']
    cur.execute(f''' SELECT valor_calificacion,des_calificacion FROM calificacion WHERE vendedor_calificacion = '{vendedor}' ''')
    return cur.fetchall()

