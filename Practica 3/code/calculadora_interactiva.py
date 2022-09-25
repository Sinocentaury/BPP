### MASTER DE PROGRAMACIÓN AVANZADA EN PYTHON
### ASIGNATURA. BUENAS PRÁCTICAS DE PROGRAMACIÓN CON PYTHON
### ACTIVIDAD LECCION 4. DEPURACIÓN Y REGLAS DE OPTIMIZACIÓN DE CÓDIGO
### AUTOR: JESÚS GUTIÉRREZ CONTRERAS

############################################################################################################################
#############################################   OPCION INTERACTIVA   #######################################################
############################################################################################################################

class Calculator:
    '''
    Calculator

    Atributos
    ---------
    num1:
        primer valor
    num2:
        segundo valor
    

    Métodos
    -------
    sumar:
        Suma los valores num1 y num2
    restar:
        Resta los valores num1 y num2
    multiplicar:
        Multiplica los valores num1 y num2
    dividir:
        Divide los valores num1 entre num2

    
    Ejemplos
    --------
    >>> import Calculator
    >>> cal = Calculator()
    >>> resultado_suma = cal.sumar(2,6)
    >>> print (resultado_suma)
    >>> resultado_dividir = cal.dividir(10,5)
    >>> print (resultado_dividir)
    '''

    def __init__(self, num1 = 0,num2 = 0) -> None:
        self.numero1 = num1
        self.numero2 = num2
    
    def sumar(self,num1,num2):
        '''
        Suma los valores nun1 y nun2
        '''
        try: 
            suma = num1 + num2
        except Exception as e:
            print (f"Ha introducido unos valores incorrectos, por favor vuelva a intentarlo\nDescripción del Error: {e}")
        else:
            return suma
    
    def restar (self,num1,num2):
        '''
        Resta los valores nun1 y nun2
        '''
        try: 
            resta = num1 - num2
            resta = self.numero1 - self.numero2
        except Exception as e:
            print (f"Ha introducido unos valores incorrectos, por favor vuelva a intentarlo\nDescripción del Error: {e}")
        else:
            return resta
    
    def multiplicar (self,num1, num2):
        '''
        Multiplica los valores nun1 y nun2
        '''
        try: 
            multiplicacion = num1 * num2
        except Exception as e:
            print (f"Ha introducido unos valores incorrectos, por favor vuelva a intentarlo\nDescripción del Error: {e}")
        else:
            return multiplicacion
    
    def dividir(self,num1, num2):
        '''
        Divide los valores nun1 entre nun2
        '''
        try: 
            division = num1 / num2
        except ZeroDivisionError:
            print (f"Ha intentado dividir por 'cero', por favor vuelva a intentarlo.")
            return False
        except Exception as e:
            print (f"Ha introducido unos valores incorrectos, por favor vuelva a intentarlo\nDescripción del Error: {e}")
        else:
            return division

def menuOpciones(num = 1):  #Mostrará un menú de opciones
    '''
    Mostrará un título y un menú de opciones para que el usuario elija lo que desea hacer
    '''
    if num == 0:    # Si es la primera vez mostramos todo el menú pero si no, no se mostrará más este mensaje de bienvenida
        print ("-------------------------------------------")
        print("  BIENVENID@ A LA CALCULADORA INTERACTIVA")
        print ("-------------------------------------------")

    
    print("QUÉ DESEA HACER:")
    print ("\t1. Sumar 2 números")
    print ("\t2. Restar 2 números")
    print ("\t3. Multiplicar 2 números")
    print ("\t4. Dividir 2 números")
    print ("\t5. Salir del Programa")
    
def eleccionUsuario():  # Recoge la eleción introducida por el usuario y la valida
    '''
    Comprueba si la opción que ha introducido el usuario es válida
    '''
    correcto = False
    while not correcto:
        opcion = input("Introduzca la opción deseada: ")
        correcto = comprobarValorOpcion(opcion)
        if not correcto:
            print("Ha introducido una opción errónea.")

    return int(opcion)

def comprobarValorOpcion (num): # Comprueba si la número que ha introducido el usuario es válido
    '''
    Comprueba si la opción que ha introducido el usuario es está en el rango permitido (opciones posibles)
    '''
    try:
        numero = int(num)   # Comprobamos si es un número
    except:
        return False
        
    else:
        if numero > 0 and numero <= 5:    # Comprobamos si el número está entre 1 y 5 que es el rango de opciones que puede elegir el usuario
            return True
        else:
            return False

def comprobarValorNumero (num): # Recoge el número introducido por el usuario y lo valida
    '''
    Comprueba si el valor introducido es un número
    '''
    try:
        numero = int(num)   # Comprobamos si es un número
    except:
        return False
        
    else:
        return True

def solicitudValor(opcion): # Solicita los números para operar y comprueba si son válidos
    '''
    Solicita 2 valores al usuario (num1 y num2) y comprueba si son válidos
    '''
    correcto = False
    
    #Solicitud del PRIMER NUMERO
    while not correcto: # Se le estará solicitando un valor mientras sea incorrecto
        numero1 = input("Introduzca el primer número: ")
        correcto = comprobarValorNumero(numero1)
        if not correcto:
            print("Ha introducido un valor no válido.")
        else:
            numero1 = int(numero1)

    correcto = False

    #Solicitud del SEGUNDO NUMERO
    while not correcto: # Se le estará solicitando un valor mientras sea incorrecto
        numero2 = input("Introduzca el segundo número: ")
        correcto = comprobarValorNumero(numero2)
        if opcion == 4 and numero2 == "0":    # Comprobamos que el usuario no quiera dividir por cero
            print("Ha introducido un valor no válido.")
            correcto = False
        elif not correcto:
            print("Ha introducido un valor no válido.")
        else:
            numero2 = int(numero2)

    return numero1, numero2

def operacionAritmetica (opcionUsuario,num1,num2):  #Realiza la operación matemática
    '''
    Realiza una operación aritmética en función de la opción elegida por el usuario y devuelve el resultado
    '''
    resultado = 0
    if opcionUsuario == 1:
        resultado = calculadora.sumar(num1,num2)
    elif opcionUsuario == 2:
       resultado = calculadora.restar(num1,num2)
    elif opcionUsuario == 3:
        resultado = calculadora.multiplicar(num1,num2)
    elif opcionUsuario == 4:
        resultado = calculadora.dividir(num1,num2)
        
    return resultado

calculadora = Calculator()
opcionUsuario = 0
primeraVez = 0    #Nos servirá para saber si el mensaje de bienvenida se ha mostrado ya, para no repetirlo

while opcionUsuario != 5:   #Si el usuario no ha elegido la opción de salir del programa se procederá a realizar la operación aritmética
    menuOpciones(primeraVez)
    
    opcionUsuario = eleccionUsuario()
    
    if opcionUsuario != 5:  # Si el usuario no ha elegido salir ejecutamos todo el algoritmo, si no, salimos del programa
        valores = solicitudValor(opcionUsuario)
        calculadora.numero1 = valores [0]
        calculadora.numero2 = valores [1]
        resultado = operacionAritmetica(opcionUsuario,calculadora.numero1, calculadora.numero2)
        print ("------------------------------------------------------------")
        print (f"\tEl resultado de la operación aritmética es: {resultado}")
        print ("------------------------------------------------------------\n")  

    primeraVez = 1    #Esta variable solo sirve para saber si es la primera vez que entramos en el bucle
    

# Si ha elegido la opción de salir, se mostrará un mensaje de despedida
print ("GRACIAS POR USAR LA CALCULADORA INTERACTIVA")
