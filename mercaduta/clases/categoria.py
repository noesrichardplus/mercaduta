from mercaduta import db
import MySQLdb

class Categoria: 
    
    def __init__(self):
        self.__nombre = "" 
        self.__descripcion = "" 

    def set_nombre(self, nombre): 
        self.__nombre = nombre
    
    def set_descripcion(self,descripcion): 
        self.__descripcion = descripcion

    
    def listar_categorias(self): 
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(f'''SELECT * FROM categoria''')
        return cur.fetchall()