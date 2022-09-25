def multiplica_numeros(a,b):
    resultado = a*b
    return resultado

def numero_primo(numero):
    resultado = True
    for i in range(2,numero):
        if numero%i == 0:
            resultado = False
    return resultado
            
def longitud_palabra(palabra):
    # La palabra elegida es "python" que tiene una longitud de 6
    resultado = len(palabra)
    return resultado

def comprueba_arroba_email(email):
    resultado = email.find("@")
    return resultado

def comprobar_DNI(dni):
    # El dni elegido es 52922687. La letra de este DNI es "D"
    letra='TRWAGMYFPDXBNJZSQVHLCKE'
    resultado = letra[dni%23]
    return resultado