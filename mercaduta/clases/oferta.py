from mercaduta import db
import re
import MySQLdb
class Oferta: 

    def __init__(self):
        self.__titulo = "" 
        self.__precio = ""
        self.__categoria = "" 
        self.__condicion = "" 
        self.__descripcion = "" 
        self.__fecha = "" 
        self.__usuario = "" 

    def set_titulo(self, titulo): 
        self.__titulo = titulo
    
    def set_precio(self, precio ): 
        self.__precio = precio 

    def set_categoria(self, categoria): 
        self.__categoria = categoria

    def set_condicion(self, condicion): 
        self.__condicion = condicion

    def set_descripcion(self, descripcion): 
        self.__descripcion = descripcion
    
    def set_fecha(self): 
        self.__fecha = ""

    def set_usuario(self,usuario): 
        self.__usuario = usuario

    def get_titulo(self): 
        return self.__titulo

    def get_precio(self): 
        return self.__precio

    def get_categoria(self): 
        return self.__categoria

    def get_condicion(self): 
        return self.__condicion
    
    def get_descripcion(self): 
        return self.__descripcion

    def get_fecha(self): 
        return self.__fecha

    def get_usuario(self): 
        return self.__usuario

    def oferta_valida(self): 
        regex_precio = "\d*[\.]*\d{0,2}"
        precio_valido = re.search(regex_precio,self.__precio)
        if self.__titulo and precio_valido and self.__descripcion: 
            return True
        else: 
            return False

    def subir(self): 
        if self.oferta_valida(): 
            cur = db.connection.cursor()
            cur.execute(f'''INSERT INTO ofertas(titulo_oferta,precio_oferta,categoria_oferta,condicion_oferta,des_oferta,fecha_oferta,usuario_oferta)
                    VALUES  ('{self.__titulo}',{self.__precio},'{self.__categoria}',{self.__condicion},'{self.__descripcion}','{self.__fecha}','{self.__usuario}');''' )
            cur.connection.commit()  
            return True
        return False      

    def eliminar_oferta(self): 
        pass

    def listar_ofertas(self,categoria): 
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(f"SELECT * FROM ofertas WHERE categoria_oferta={categoria}")
        return cur.fetchall()

    def listar_todas_ofertas(self): 
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(f"SELECT * FROM ofertas")
        return cur.fetchall()

    def seleccionar_oferta(self, id_oferta): 
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(f"SELECT * FROM ofertas WHERE id_oferta={id_oferta}")
        return cur.fetchone()