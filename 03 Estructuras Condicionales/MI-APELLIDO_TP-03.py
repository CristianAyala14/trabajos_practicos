# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario != 0 and edad_usuario > 18:
  print("Usted es mayor de edad.")
else:
  print("Usted no es mayor de edad.")


# 2)  Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”

nota_usuario = int(input("Ingrese su nota: "))
if nota_usuario  > 6:
  print("Usted ha aprobado.")
else:
  print("Usted ha desaprobado.")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

valor = int(input("Ingrese el valor: "))

if valor % 2 == 0: 
  print("Usted ingreso un numero par.")
else:
  print("Por favor, ingrese un numero par.")



# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario > 0 and edad_usuario < 12:
  print("Niño/a.")
elif edad_usuario >= 12 and edad_usuario < 18:
  print("Adolescente.")
elif edad_usuario >= 18 and edad_usuario < 30:
  print("Adulto/a joven.")
elif edad_usuario >= 30: 
  print("Adulto/a.")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.


contraseña = input("Ingrese su contraseña: ")

if 8 <= len(contraseña) <= 14:  
    print("Ha ingresado una contraseña correcta.")  
else:  
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")



# 6)  // CREO UN ENTORNO PARA ESTA CARPETA. ASI PODER INSTALAR STATISTICS


from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]
#el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if moda < mediana < media:
  print("Sesgo positivo (a la derecha)")
elif moda > mediana > media:
  print("Sesgo negativo (a la izquierda)")
else:
  print("Sin sesgo")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

texto = input("Ingrese el texto: ")

if texto[-1].lower() in "aeiou":
  texto += "!"

print(texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.


nombre = input("Ingresa tu nombre: ")

print("Elige una opción para transformar tu nombre:")
print("1. Mayúsculas")
print("2. Minúsculas")
print("3. Primera letra mayúscula")

opcion = input("Ingresa 1, 2 o 3: ")

if opcion == '1':
    nombre_transformado = nombre.upper() 
elif opcion == '2':
    nombre_transformado = nombre.lower() 
elif opcion == '3':
    nombre_transformado = nombre.title() 
else:
    nombre_transformado = "Opción no válida"

print(f"Resultado: {nombre_transformado}")



#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


magnitud = float(input("Ingresa la magnitud del terremoto según la escala de Richter: "))


if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"


print(f"La magnitud {magnitud} está clasificada como: {categoria}")

#10)


hemisferio = input("¿En qué hemisferio te encuentras? (N para Norte / S para Sur): ").strip().upper()


if hemisferio not in ('N', 'S'):
    print("Error: Debes ingresar 'N' para el hemisferio norte o 'S' para el hemisferio sur.")
else:
    mes = int(input("Ingresa el número del mes (1-12): "))
    dia = int(input("Ingresa el día del mes: "))

    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
        print("Error: Mes o día inválido.")
    else:
      if hemisferio == "N" and ((mes == 12 and dia >= 21) or mes == 1 or mes ==2 or (mes == 3 and dia <= 20)): 
        print("Usted se encuentra en Invierno.")
      elif hemisferio == "S" and ((mes == 12 and dia >= 21) or mes == 1 or mes ==2 or (mes == 3 and dia <= 20)):
        print("Usted se encuentra en Verano.")
      elif hemisferio == "N" and ((mes == 3 and dia >= 21) or mes == 4 or mes ==5 or (mes == 6 and dia <= 20)): 
        print("Usted se encuentra en Primavera.")
      elif hemisferio == "S" and ((mes == 3 and dia >= 21) or mes == 4 or mes ==5 or (mes == 6 and dia <= 20)): 
        print("Usted se encuentra en Otoño.")
      elif hemisferio == "N" and ((mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20)): 
        print("Usted se encuentra en Verano.")
      elif hemisferio == "S" and ((mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20)): 
        print("Usted se encuentra en Invierno.")
      elif hemisferio == "N" and ((mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20)): 
        print("Usted se encuentra en Otoño.")
      elif hemisferio == "S" and ((mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20)): 
        print("Usted se encuentra en Primavera.")


        