from mercaduta import db
import MySQLdb

class Calificacion: 

    def __init__(self):
        self.__comprador = "" 
        self.__vendedor = "" 
        self.__oferta = "" 
        self.__valor = "" 
        self.__descripcion = "" 

    def set_comprador(self, comprador ): 
        self.__comprador = comprador

    def set_vendedor(self, vendedor): 
        self.set_vendedor = vendedor 

    def set_oferta(self, oferta): 
        self.__oferta = oferta

    def set_valor(self, valor): 
        self.__valor = valor 

    def set_descripcion(self, descripcion): 
        self.__descripcion = descripcion
    
    def existe(self): 
        cur = db.connection.cursor()
        cur.execute(f"SELECT EXISTS( SELECT * FROM calificacion WHERE comprador_calificacion = '{self.__comprador}' AND vendedor_calificacion = '{self.__vendedor}' AND oferta_calificacion = '{self.__oferta}' )")
        return cur.fetchone()[0] 

    def guardar(self): 
        cur = db.connection.cursor()
        cur.execute(f'''INSERT INTO calificacion(comprador_calificacion, vendedor_calificacion,oferta_calificacion,valor_calificacion,des_calificacion) 
                        VALUES ('{self.__comprador}','{self.__vendedor}','{self.__oferta}','{self.__valor}','{self.__descripcion}')''' )
        cur.connection.commit()

    def segun_vendedor(self,id_oferta): 
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(f''' SELECT usuario_oferta FROM ofertas WHERE id_oferta={id_oferta}''')
        vendedor = cur.fetchall()[0]['usuario_oferta']
        cur.execute(f''' SELECT valor_calificacion,des_calificacion FROM calificacion WHERE vendedor_calificacion = '{vendedor}' ''')
        return cur.fetchall()