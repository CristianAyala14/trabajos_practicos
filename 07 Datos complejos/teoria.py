#Datos abstractos, complejos: NTipos de datos que nos describen su comportamiento pero no como funcionan internaemente
#beneficios: modularidad, reutilizacion, facilidad y mantenimiento.
#caracteristicas: 
# abstraccion: ocultan la implementacion interna.  }
# encapsulacion: protegen los datos evitando acceso externo no autorizado.
# independencia: se pueden representar de diferentes maneras sin afectar su uso.
#Ejemplos: Listas, pilas, colas, conjuntos, diccionarios, arboles, grafos.

#lista []

# 📌 Creación y uso de una lista en Python
mi_lista = ["🍎", "🍌", "🍇"]
mi_lista.append("🥑")  # Agregar un elemento
print(mi_lista)  # Salida: ['🍎', '🍌', '🍇', '🥑']

#Pila (stack) first in last out (LIFO)
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        return self.elementos.pop() if self.elementos else "La pila está vacía"

pila = Pila()
pila.apilar("📚 Libro 1")
pila.apilar("📚 Libro 2")
print(pila.desapilar())  # Salida esperada: 📚 Libro 2


#Cola (Queue) first in first out (FIFO)

from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        return self.elementos.popleft() if self.elementos else "La cola está vacía"

# 🚀 Probemos nuestra cola
cola = Cola()
cola.encolar("🎟️ Ticket 1")
cola.encolar("🎟️ Ticket 2")
print(cola.desencolar())  # Salida esperada: 🎟️ Ticket 1

# 📌 Creación y uso de un diccionario en Python
mi_diccionario = {"nombre": "Alice", "edad": 25, "profesion": "Ingeniera"}
print(mi_diccionario["nombre"])  # Salida: Alice