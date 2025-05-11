import math

# 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(informacion_personal(nombre, apellido, edad, residencia))


# 4
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = int(input("Ingrese radio: "))

print(f"Area: {calcular_area_circulo(radio)}")
print(f"Perimetro: {calcular_perimetro_circulo(radio)}")



# 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese segundos: "))
print(f"Equivale a {segundos_a_horas(segundos)}")


# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

# 8. Calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# ------------------ Programa principal ------------------
if __name__ == "__main__":
    # 1
    imprimir_hola_mundo()

    # 2
    nombre = input("\nIngrese su nombre: ")
    print(saludar_usuario(nombre))

    # 3
    nombre = input("\nNombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    # 4
    radio = float(input("\nIngrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

    # 5
    segundos = int(input("\nIngrese una cantidad de segundos: "))
    print(f"Equivale a {segundos_a_horas(segundos):.2f} horas")

    # 6
    numero = int(input("\nIngrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    # 7
    a = float(input("\nIngrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    suma, resta, mult, div = operaciones_basicas(a, b)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")

    # 8
    peso = float(input("\nIngrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    print(f"Su IMC es: {calcular_imc(peso, altura)}")

    # 9
    celsius = float(input("\nIngrese la temperatura en Celsius: "))
    print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F")

    # 10
    n1 = float(input("\nPrimer número: "))
    n2 = float(input("Segundo número: "))
    n3 = float(input("Tercer número: "))
    print(f"El promedio es: {calcular_promedio(n1, n2, n3):.2f}")