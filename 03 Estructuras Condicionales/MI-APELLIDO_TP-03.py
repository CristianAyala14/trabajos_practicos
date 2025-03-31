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