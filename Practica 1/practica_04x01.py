### MASTER DE PROGRAMACIÓN AVANZADA EN PYTHON
### ASIGNATURA. BUENAS PRÁCTICAS CON PYTHON
### ACTIVIDAD LECCION 1. CONTROL DE ERRORES, PRUEBAS Y VALIDACIÓN DE DATOS
### AUTOR: JESÚS GUTIÉRREZ CONTRERAS
########################################################################################################

import csv
from statistics import median
import pandas as pd
import matplotlib.pyplot as plt


########################################################################################################
# APARTADO 1 DE LA PRACTICA: IMPLEMENTAR UN PROGRAMA QUE LEA EL CONTENIDO DEL FICHERO Y REALICE CÁLCULOS
########################################################################################################

def indice_min(lista):
    indice = 0
    valor = 0
    for i in range(12):
        if lista[i] < valor:
            valor = lista[i]
            indice = i
    return indice

def indice_max(lista):
    indice = 0
    valor = 0
    for i in range(12):
        if lista[i] >= valor:
            valor = lista[i]
            indice = i
    return indice

df = pd.read_csv("finanzas2020[1].csv",sep="\t")
df_meses = pd.DataFrame(df.columns.values).transpose()

gastos = [0,0,0,0,0,0,0,0,0,0,0,0]
ingresos = [0,0,0,0,0,0,0,0,0,0,0,0]
ahorro = []

# Separamos los gastos y los ingresos de cada mes en dos listas diferentes para poder calcular después los datos que nos piden
for mes in range(12):

    for i in df.iloc[mes]:
        if type(i)!= int:
            i = int(i)
            if i < 0:
                gastos[mes] += i
            else:
                ingresos[mes]+= i  
    
    
df_ingresos = pd.DataFrame(ingresos).transpose()
df_gastos = pd.DataFrame(gastos).transpose()

# Calculamos el resultado de cada mes (ingresos + (- gastos))
ahorro = list(map(lambda x,y: x+y, ingresos, gastos))

df_resultado = pd.concat([df_meses,df_ingresos,df_gastos,pd.DataFrame([ahorro])],axis=0)
df_resultado.index = ["Mes","Ingresos","Gastos","Ahorros"]

index_min = indice_min(gastos)   #Calculamos el indice del valor mínimo
index_max = indice_max(ahorro)   #Calculamos el indice del valor máximo

mes_gasto = df.columns.values[index_min]    #A partir del indice anterior se averigua el mes al que corresponde
mes_ahorro = df.columns.values[index_max]  #A partir del indice anterior se averigua el mes al que corresponde

print (f"MES QUE MÁS SE HA GASTADO: {mes_gasto} CON UN TOTAL DE {gastos[index_min]}€")
print (f"MES QUE MÁS SE HA AHORRADO: {mes_ahorro} CON UN TOTAL DE {ahorro[index_max]}€")
print (f"LA MEDIA DE GASTOS DEL AÑO HA SIDO: {median(gastos)}€")
print (f"EL GASTO TOTAL DEL AÑO HA SIDO: {sum(gastos)}€")
print (f"EL TOTAL DE INGRESOS DEL AÑO HA SIDO: {sum(ingresos)}€")

print (df_resultado)

# Generamos un gráfico con la evolución de los ingresos a lo largo del año
plt.bar(df_resultado.iloc[0], df_resultado.iloc[3])
plt.show()

########################################################################################################
# APARTADO 2 DE LA PRACTICA: IMPLEMENTAR UN PROGRAMA QUE LEA EL CONTENIDO DEL FICHERO Y REALICE CÁLCULOS
########################################################################################################

class Error_tamaño (Exception):
    pass

class Error_contenido_mes (Exception):
    pass


def indice_min(lista):  # Calcularemos el indice del valor mínimo dentro de la lista
    indice = 0
    valor = 0
    for i in range(12):
        if lista[i] < valor:
            valor = lista[i]
            indice = i
    return indice

def indice_max(lista):  # Calcularemos el indice del valor máximo dentro de la lista
    indice = 0
    valor = 0
    for i in range(12):
        if lista[i] >= valor:
            valor = lista[i]
            indice = i
    return indice


def comprobar_contenido_mes(data):  # Comprobaremos si cada columna del mes tiene datos o no
    longitud = data.shape
    
    for i in range(longitud[1]):
        mes = data.columns.values[i]
        columna = data[mes]
        tamaño = len(columna)
        if tamaño < 1:   # Si no hay datos se lanzará una excepción
            print ("No hay datos")
            raise Error_contenido_mes

gastos = [0,0,0,0,0,0,0,0,0,0,0,0]
ingresos = [0,0,0,0,0,0,0,0,0,0,0,0]
ahorro = []

# Intentamos abrir el archivo
try:
    df = pd.read_csv("finanzas2020[1].csv",sep="\t")
    df_meses = pd.DataFrame(df.columns.values).transpose()
    
    tamaño = df.shape   #Calculamos el tamaño de la matriz

    if tamaño[1] != 12: #Si no tiene 12 columnas (12 meses) lanzará una excepcion
        raise Error_tamaño

    comprobar_contenido_mes(df) # Comprobaremos si cada columna del mes tiene datos o no


    # Separamos los gastos y los ingresos de cada mes en dos listas diferentes para poder calcular después los datos que nos piden
    for mes in range(12):
        for i in df.iloc[mes]:
            if type(i)!= int:
                i = int(i)  #Si los valores de la matriz no son enteros el programa intentará convertirlos. Si no puede lanzará una excepcion
                if i < 0:
                    gastos [mes] += i
                else:
                    ingresos [mes] += i  

    df_ingresos = pd.DataFrame(ingresos).transpose()
    df_gastos = pd.DataFrame(gastos).transpose()

    # Calculamos el resultado de cada mes (ingresos + (- gastos))
    ahorro = list(map(lambda x,y: x+y, ingresos, gastos))

    df_resultado = pd.concat([df_meses,df_ingresos,df_gastos,pd.DataFrame([ahorro])],axis=0)
    df_resultado.index = ["Mes","Ingresos","Gastos","Ahorros"]

    index_min = indice_min(gastos)   #Calculamos el indice del valor mínimo
    index_max = indice_max(ahorro)   #Calculamos el indice del valor máximo

    mes_gasto = df.columns.values[index_min]    #A partir del indice anterior se averigua el mes al que corresponde
    mes_ahorro = df.columns.values[index_max]  #A partir del indice anterior se averigua el mes al que corresponde

    print (f"MES QUE MÁS SE HA GASTADO: {mes_gasto} CON UN TOTAL DE {gastos[index_min]}€")
    print (f"MES QUE MÁS SE HA AHORRADO: {mes_ahorro} CON UN TOTAL DE {ahorro[index_max]}€")
    print (f"LA MEDIA DE GASTOS DEL AÑO HA SIDO: {median(gastos)}€")
    print (f"EL GASTO TOTAL DEL AÑO HA SIDO: {sum(gastos)}€")
    print (f"EL TOTAL DE INGRESOS DEL AÑO HA SIDO: {sum(ingresos)}€")


except OSError:
    print ("El archivo no se encuentra")
        
except Error_tamaño:
    print ("No hay 12 meses en el archivo")

except Error_contenido_mes:
    print ("1 o más meses no tienen datos")

except TypeError:
    print ("Los valores leidos no son del tipo apropiado. Compruebe el tipo de datos del archivo")

except ZeroDivisionError:
    print ("Se ha intentado dividir un valor por cero")

except Exception as e:
    print ("Lo sentimos pero ha ocurrido un error al intentar abrir el archivo. Comprueve que existe dicho archivo")