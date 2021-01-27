
from mercaduta import db
import re

class Usuario: 
    def __init__(self): 
        self.__email = ""
        self.__passwd = ""
        self.__nombre= ""
        self.__apellido = ""
        self.__contacto_alter = ""
        self.__celular = ""

    def set_email(self,email): 
        self.__email = email
    
    def get_email(self): 
        return self.__email 

    def set_passwd(self,passwd): 
        self.__passwd = passwd 

    def get_passwd(self): 
        return self.__passwd

    def set_nombre(self,nombre): 
        self.__nombre = nombre

    def get_nombre(self): 
        return self.__nombre 

    def set_apellido(self,apellido): 
        self.__apellido = apellido

    def get_apellido(self): 
        return self.__apellido 

    def set_contacto_alter(self,contacto): 
        self.__contacto_alter = contacto

    def set_celular(self,celular): 
        self.__celular = celular  


    def valido(self): 
        cur = db.connection.cursor()
        cur.execute(f"SELECT EXISTS( SELECT * FROM usuarios WHERE email = '{self.__email}' AND passwd = '{self.__passwd}')")
        return cur.fetchone()[0]

    def existe(self): 
        cur = db.connection.cursor()
        cur.execute(f"SELECT EXISTS( SELECT * FROM usuarios WHERE email = '{self.__email}' )")
        return cur.fetchone()[0]

    def validar_email(self): 
        regex = "[^@]."
        no_empieza = re.match(regex,self.__email)
        si_hay = re.search("@",self.__email)
        if no_empieza and si_hay:
            email_divi = re.split("@",self.__email)
            if email_divi[1] == "uta.edu.ec": 
                return True
            else: 
                return False
        else: 
            return False

    def validar_atributos(self,repe_passwd): 
        regex_nombres = "[^\ ][a-zA-Z]"
        nombre_valido = re.search(regex_nombres,self.__nombre)
        apellido_valido = re.search(regex_nombres,self.__apellido)
        if nombre_valido and apellido_valido and self.validar_passwd(): 
            if self.__passwd == repe_passwd: 
                return True
            else: 
                return False
        else: 
            return False

    def validar_passwd(self): 
        regex = ".{8,}"
        pat = re.compile(regex)
        return re.search(pat, self.__passwd) 

    def registrar_usuario(self):
        cur = db.connection.cursor()
        cur.execute(f"INSERT INTO usuarios(email, passwd, nombre, apellido) VALUES ('{self.__email}','{self.__passwd}','{self.__nombre}','{self.__apellido}')")
        db.connection.commit()

    def validar_nombre(self): 
        regex_nombres = "[^\ ][a-zA-Z]"
        nombre_valido = re.search(regex_nombres,self.__nombre)
        if nombre_valido: 
            return True
        else: 
            return False
        
    def validar_apellido(self): 
        regex_nombres = "[^\ ][a-zA-Z]"
        apellido_valido = re.search(regex_nombres,self.__apellido)
        if apellido_valido: 
            return True
        else: 
            return False

    def validar_celular(self): 
        regex_celular = "^(\d{10})"
        celular_valido = re.search(regex_celular,self.__celular)
        if celular_valido: 
            return True
        else: 
            return False

    def actualizar_nombre(self): 
        if self.validar_nombre(): 
            cur = db.connection.cursor()
            cur.execute(f'''UPDATE usuarios SET nombre = '{self.__nombre}' WHERE email = '{self.__email}';''' )
            cur.connection.commit()
    def actualizar_apellido(self): 
        if self.validar_apellido(): 
            cur = db.connection.cursor()
            cur.execute(f'''UPDATE usuarios SET apellido = '{self.__apellido}' WHERE email = '{self.__email}';''' )
            cur.connection.commit()

    def actualizar_celular(self): 
        if self.validar_celular(): 
            cur = db.connection.cursor()
            cur.execute(f'''UPDATE usuarios SET celular = '{self.__celular}' WHERE email = '{self.__email}';''' )
            cur.connection.commit()

    def actualizar_contacto_alter(self): 
        cur = db.connection.cursor()
        cur.execute(f'''UPDATE usuarios SET contacto_alter = '{self.__contacto_alter}' WHERE email = '{self.__email}';''' )
        cur.connection.commit()

        