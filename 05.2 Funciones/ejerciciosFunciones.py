
#EJERCICIO 1: Informar si el numero es primo

# Definicion de funciones // agregamos al ejercicio anterior  rango min y max pero con rangos por defecto. en este caso infinitos negativos y positivo.
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}"))
    while n < min or n > max:
        n = int(input(f"Error. {mensaje}"))
        return n
    
# Programa principal
num = leer_entero_validado("Ingrese un numero natural: ", 1)
print (f"Seguimos adelante con el numero {num}")


# si es primo o no
def obtener_resto(num1, num2):
    # el resto de la division entre dos numeros
    return num1 - num2 *  (num1 // num2) #sin usar operador %

def es_multiplo(x, y):
    return obtener_resto(x, y) == 0

def es_primo(numero):
    cont = 2
    while cont < numero and not es_multiplo(numero, cont):
        cont += 1
    return cont == numero


def informar_si_numero_es_primo(numero):
    if es_primo(numero): 
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")



# ------------------------------------------------------------------------
# EJERCICIO 2: Ingresar cualquier numero positivo y que diga si es perfecot o no (aca vemos la modularizacion de funciones)

#def de funciones

# valido el numero entre 1 y mas infinito.
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}"))
    while n < min or n > max:
        n = int(input(f"Error. {mensaje}"))
        return n
    
def obtener_resto(num1, num2):
    # el resto de la division entre dos numeros
    return num1 - num2 *  (num1 // num2) #sin usar operador %

def es_multiplo(x, y):
    return obtener_resto(x, y) == 0


def sumatoria_divisores_propios(numero):
    for i in range(1, numero // 2 + 1):
        if es_multiplo(numero, i):
            suma += i

    
def es_perfecto(numero):
    return sumatoria_divisores_propios(numero) == numero
    
def informar_si_numero_es_perfecto(numero):
    if es_perfecto(numero): 
        print(f"El numero {numero} es perfecto")
    else:
        print(f"El numero {numero} no es perfecto")




#Programa principal
num = leer_entero_validado("Ingrese un numero natural", 1)
informar_si_numero_es_perfecto(num)

# ------------------------------------------------------------------------
