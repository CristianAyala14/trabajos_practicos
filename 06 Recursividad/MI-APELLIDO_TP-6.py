#TRABAJO PRACTICO N°6 - Cristian Ayala. 

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input("Ingrese un número: "))

# Mostrar factoriales desde 1 hasta n
for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("Ingrese la posición hasta la cual mostrar la serie de Fibonacci: "))

for i in range(n + 1):
    print(f"{i} = {fibonacci(i)}")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula n**m = n ∗ n**(m−1)
# Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


A = int(input("Base: "))
B = int(input("Exponente: "))
print(f"{A}^{B} = {potencia(A, B)}")



# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

# Ejemplo:
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1


def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número en base decimal: "))
binario = decimal_a_binario(numero)

print("Binario:", binario if binario else "0")






✅ 5) Palíndromo recursivo (sin [::-1])
python
Copiar
Editar
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejemplo de uso
texto = input("Ingrese una palabra: ").lower()
print("¿Es palíndromo?", es_palindromo(texto))
✅ 6) Suma de dígitos (sin strings)
python
Copiar
Editar
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# Ejemplo de uso
numero = int(input("Ingrese un número para sumar sus dígitos: "))
print("Suma de dígitos:", suma_digitos(numero))
✅ 7) Bloques de pirámide
python
Copiar
Editar
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Ejemplo de uso
niveles = int(input("Ingrese cantidad de bloques en la base: "))
print("Total de bloques necesarios:", contar_bloques(niveles))
✅ 8) Contar cuántas veces aparece un dígito
python
Copiar
Editar
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    actual = 1 if numero % 10 == digito else 0
    return actual + contar_digito(numero // 10, digito)

# Ejemplo de uso
num = int(input("Ingrese un número: "))
dig = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces.")