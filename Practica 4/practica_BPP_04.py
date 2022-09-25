### MASTER DE PROGRAMACIÓN AVANZADA EN PYTHON
### ASIGNATURA. BUENAS PRÁCTICAS DE PROGRAMACIÓN CON PYTHON
### ACTIVIDAD LECCION 4. DEPURACIÓN Y REGLAS DE OPTIMIZACIÓN DE CÓDIGO
### AUTOR: JESÚS GUTIÉRREZ CONTRERAS


#################################### APARTADO 1. LISTAS DE COMPRESION ###################################
import pdb
pdb.set_trace()

lista = [[2,4,1],[1,2,3,4,5,6,7,8],[100,250,43]]

# Metodo Tradicional
maximos_tradicional = []
for i in lista:
    maximos_tradicional.append (max(i))
print (maximos_tradicional)


# Metodo Listas de Compresión
maximos_compresion = [max(i) for i in lista]
print (maximos_compresion)


################################### APARTADO 2. FUNCIÓN FILTER ###################################
def es_primo(n):
    primo = True
    for i in range (2,n):
        if n%i == 0:
            primo = False
    return primo

lista2 = [3,4,8,5,5,22,13]

lista_primos = list(filter(es_primo,lista2))
print (lista_primos)
