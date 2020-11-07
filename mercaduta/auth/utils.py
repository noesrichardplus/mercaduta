import re


def verificar_email(email): 
    regex = "[^@]."
    no_empieza = re.match(regex,email)
    si_hay = re.search("@",email)
    if no_empieza and si_hay:
        email_divi = re.split("@",email)
        if email_divi[1] == "uta.edu.ec": 
            return True
        else: 
            return False
    else: 
        return False

def verificar_registro(nombre,apellido,passwd,repe_passwd): 
    regex_nombres = "[^\ ][a-zA-Z]"

    regex = "^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?.&])[A-Za-z\d@$!#%*?.&]{6,20}$"

    pat = re.compile(regex)
    
    nombre_valido = re.search(regex_nombres,nombre)
    apellido_valido = re.search(regex_nombres,apellido)
    passwd_valida = re.search(pat, passwd) 
    
    if nombre_valido and apellido_valido and passwd_valida: 
        if passwd == repe_passwd: 
            return True
        else: 
            return False
    else: 
        return False

print(verificar_registro("richard","carrion","123qwer.@","123qwer.@"))
