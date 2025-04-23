#metodos para las listas / arrays

#LIST - RANGE
lista_range = list(range(1,10))
# [1,2,3,4,5,6,7,8,9]
lista_range = list(range(1,10,2))
# [1,3,5,7,9]

#SPLIT
hello_world_string = "Hello world!"
lista_separada = hello_world_string.split()
#[hello , world!]

#SLICING
lista = ["UTN", 2, 3.5, True]
posicion_1_lista = lista[0]
print(posicion_1_lista)
print(type(posicion_1_lista))
#UTN
#<class 'str'>


#SLICING PERO DE UNA SUBLISTA
print(posicion_1_lista[0:2]) # si quiero hasta el final de la lista, en el segundo parametro no pongo nada. / el parametro de fin no se incluye en el slicing.
#["UTN", 2]


#APPEND . se agrega al final de la lista.
notas = [9.1, 8.5, 7.3]
notas.append(9.2)
notas.append(False)
print(notas)
#[9.1, 8.5, 7.3, 9.2, False]

#REMOVE
notas.remove(9.2)
notas.remove(False)
print(notas)
#[9.1, 8.5, 7.3]


#ACTUALIZAR ELEMENTO DE UNA LISTA
notas[2] = "Hola mundo"
print(notas)
#[9.1, 8.5, "Hola mundo"]


#CONCATENAR
notas_2 = notas + ["UTN", True]
print(notas_2)
# [9.1, 8.5, 'Hola mundo', 'UTN', True]

#Lista anidada
lista_anidada = [1,1.3,["UTN", "MENDOZA "]]
print(lista_anidada[2]) #["UTN", "MENDOZA"]
print(lista_anidada[2][1]) # MENDOZA doble slicing


#podmos buscar un elemento en una lista por valor booleano
lista_anidada = [1,2,3]
print (1 in lista_anidada)
#True