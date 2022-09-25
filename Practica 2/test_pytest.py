### MASTER DE PROGRAMACIÓN AVANZADA EN PYTHON
### ASIGNATURA. BUENAS PRÁCTICAS CON PYTHON
### ACTIVIDAD LECCION 2. DESARROLLO DE CÓDIGO GUIADO POR PRUEBAS
### AUTOR: JESÚS GUTIÉRREZ CONTRERAS
#############################################################################################

import pytest

def test_multiplica_numeros():
    a = 8
    b = 5
    resultado = 40
    assert a*b == resultado

def test_numero_primo():
    resultado = True
    numero = 7
    for i in range(2,numero):
        if numero%i == 0:
            resultado = False
    assert resultado == True
            
def test_longitud_palabra():
    palabra = "python"
    resultado = 6
    assert len(palabra) == resultado

def test_comprueba_arroba_email():
    email = "email@gmail.com"
    resultado = -1
    assert email.find("@") != resultado

def test_comprobar_DNI():
    dni =52922687
    resultado = "D"
    letra='TRWAGMYFPDXBNJZSQVHLCKE'
    assert letra[dni%23] == resultado
