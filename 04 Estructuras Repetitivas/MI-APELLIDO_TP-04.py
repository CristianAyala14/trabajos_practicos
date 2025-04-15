#TRABAJO PRACTICO N°4 - Cristian Ayala. 



#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for c in range(0, 101):
    print(c)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num_User = input("Ingrese un numero entero: ")
cantidad_Digitos = len(num_User)
print("La cantidad de digitos es: ", cantidad_Digitos)


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

inicio = min(valor1, valor2) + 1
fin = max(valor1, valor2)

for c in range(inicio + 1, fin):
    suma = 0
    suma += c

print("La suma de los numeros entre ", valor1, " y ", valor2, " es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

total = 0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    total += numero
    if numero == 0:
        break

print("La suma total es:", total)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_Aleatorio = random.randint(0, 9)
intentos = 0

while True:
    num_User = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1

    if num_User == num_Aleatorio:
        print("¡Correcto! Adivinaste en", intentos, "intentos.")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")




#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for c in range(0, 101, 2):
    print(c)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.


num_User = int(input("Ingrese un numero entero positivo: "))
suma = 0
for c in range(0, num_User + 1):
    suma += c

print("La suma de los numeros entre 0 y ", num_User, " es: ", suma)


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0


for c in range(100): 
    num = int(input(f"Ingrese el número {c + 1}: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1


print("\nResultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

import statistics

numeros = []

for c in range(100):  
    num = int(input(f"Ingrese el número {c + 1}: "))
    numeros.append(num) 

media = statistics.mean(numeros)
print(f"La media de los números ingresados es: {media}")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número: ")

numero_invertido = numero[::-1]
print(f"El número invertido es: {numero_invertido}")