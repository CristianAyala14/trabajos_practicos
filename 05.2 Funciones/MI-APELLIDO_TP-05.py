# como definir funciones
def obtener_resto(num1, num2):
    # el resto de la division entre dos numeros
    return num1 - num2 *  (num1 // num2) #sin usar operador %

a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))

resto = obtener_resto()

print(f"El resto entre {a} y {b} es: {resto}")
