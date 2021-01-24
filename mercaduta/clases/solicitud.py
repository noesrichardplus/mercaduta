
from mercaduta import db
import MySQLdb

class Solicitud: 

    def __init__(self):
        self.__email_solicitante = "" 
        self.__id_oferta = "" 
        self.__estado = "" 

    def set_email_solicitante(self,email): 
        self.__email_solicitante = email 

    def set_id_oferta(self,id_oferta): 
        self.__id_oferta = id_oferta

    def self_estado(self, estado): 
        self.__estado = estado

    def get_email_solicitante(self): 
        return self.__email_solicitante

    def get_id_oferta(self): 
        return self.__id_oferta

    def get_estado(self): 
        return self.__estado

    def listar_solicitudes(self): 
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(f'''SELECT solicitud.id_solicitud,solicitud.email_solicitante,ofertas.titulo_oferta, ofertas.usuario_oferta
                        FROM solicitud 
                        INNER JOIN ofertas ON solicitud.id_oferta = ofertas.id_oferta
                        WHERE ofertas.usuario_oferta = "{self.__email_solicitante}";''')
        return cur.fetchall() 


    def listar_solicitudes_enviadas(self): 
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(f'''SELECT solicitud.email_solicitante,ofertas.titulo_oferta, usuarios.email,usuarios.nombre,
                            usuarios.apellido,usuarios.celular,usuarios.contacto_alter
                    FROM solicitud 
                    INNER JOIN ofertas ON solicitud.id_oferta = ofertas.id_oferta
                    INNER JOIN usuarios  ON ofertas.usuario_oferta = usuarios.email
                    WHERE solicitud.email_solicitante = "{self.__email_solicitante}" AND solicitud.estado = true; ''')
        return cur.fetchall()

    def eliminar_solicitud(self, id_solicitud):
        cur = db.connection.cursor()
        cur.execute(f'''DELETE FROM solicitud WHERE id_solicitud = {id_solicitud};''' )
        cur.connection.commit() 

    def existe(self): 
        cur = db.connection.cursor()
        cur.execute(f"SELECT EXISTS( SELECT * FROM solicitud WHERE email_solicitante = '{self.__email_solicitante}' AND id_oferta = {self.__id_oferta}  )")
        return cur.fetchone()[0]

    def guardar(self): 
        cur = db.connection.cursor()
        cur.execute(f'''INSERT INTO solicitud(email_solicitante,id_oferta) VALUES("{self.__email_solicitante}",{self.__id_oferta});''' )
        cur.connection.commit()

    def aceptar(self,id_solicitud): 
        cur = db.connection.cursor()
        cur.execute(f'''UPDATE solicitud SET estado = true WHERE id_solicitud = {id_solicitud};''' )
        cur.connection.commit()