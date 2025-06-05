#TRABAJO PRACTICO ESTRUCTURAS COMPLEJAS

#1 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1200
precios_frutas["Pera"] = 1200

#2 
precios_frutas["Banana"]= 1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]= 2800

#3
lista= []
for key in precios_frutas: #python por defecto recorre las keys en un disccionario por medio de este for.
  lista.append(key)


#4
contactos = {}
i = 5

while i != 0:
    nombre = input("Ingrese nombre del contacto: ")
    while True:
        numero = input("Ingrese el número del contacto (10 números): ")
        if len(numero) == 10:
            break 
        else:
            print("Número incorrecto, intente de nuevo.")

    contactos[nombre] = int(numero)
    i -= 1
    print(f"Contacto guardado. Te quedan {i} intento(s).\n")



#5

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(frase)
conteo = {}
for palabra in frase:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1


#6

alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno.")
    notas = []
    for j in range(3): 
        nota = input("Ingrese la nota del alumno: ")
        notas.append(int(nota))
    alumnos[nombre] = tuple(notas)

#7 sets

parcial1 = {4, 7, 9, 10, 2, 5, 8}
parcial2 = {5, 8, 9, 2, 1, 7, 3, 10}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

#8
diccionario_productos = {"fideos": 10, "yerba": 5, "carne": 11, "azucar": 1}

opcion = input("Ingrese 1 para agregar producto. 2 para consultar stock del producto.")
if int(opcion) != 1 and int(opcion) != 2:
    print("Dato ingresado incorrecto. Gracias por usar el sistema.")
else:
    if int(opcion) == 1:
        producto_nuevo = input("Ingrese el nombre del producto que desea agregar: ").lower()
        stock_producto_nuevo = input("Ahora ingrese la cantidad de stock para el nuevo producto: ")
        diccionario_productos[producto_nuevo] = int(stock_producto_nuevo)
        print(f"Se agrego el producto {producto_nuevo} y tiene de stock: {diccionario_productos[producto_nuevo]}. Gracias por usar el sistema.")
    if int(opcion) == 2:
        consulta = input("Ingrese el producto que quiere consultar stock: ").lower()
        if consulta in diccionario_productos:
            print(f"El producto {consulta} tiene de stock: {diccionario_productos[consulta]}.")
            respuesta = input("Desea agregar stock?: SI/NO").lower()
            if respuesta == "si":
                nuevo_stock = input("Ingrese la cantidad de stock que desea sumar: ")
                diccionario_productos[consulta] += int(nuevo_stock)
                print(f"Se actualizo stock del producto {consulta} y ahora es stock de: {diccionario_productos[consulta]}. Gracias por usar el sistema.")

            else:
                print("Muchas gracias por usar el sistema.")
        else:
            respuesta1 = input("El producto no esta en inventario. Desea agregarlo? Si/No: ").lower()
            if respuesta1 == "si":
                producto_nuevo = input("Ingrese el nombre del producto que desea agregar: ").lower()
                stock_producto_nuevo = input("Ahora ingrese la cantidad de stock para el nuevo producto: ")
                diccionario_productos[producto_nuevo] = int(stock_producto_nuevo)


#9


class Agenda:
    def __init__(self):
        self.eventos = {}
    def agregar_evento(self, dia, hora, evento):
        self.eventos[(dia, hora)] = evento
    def consultar_evento(self, dia, hora):
        return self.eventos.get((dia, hora), "No hay evento programado en ese momento.")

agenda = Agenda()
agenda.agregar_evento("Lunes", "10:00", "Reunión con el equipo")
agenda.agregar_evento("Martes", "15:00", "Clase de yoga")

print(agenda.consultar_evento("Lunes", "10:00"))  
print(agenda.consultar_evento("Lunes", "11:00"))


#10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}


capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(capitales_paises)