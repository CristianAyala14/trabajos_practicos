#RECURSIVIDAD
#EJ 1:
def sum_list(lst):
  if len(lst)==0:
    return 0
  else:
    return lst[0] + sum_list(lst[1:])

lista = [1,2,3,4,5]
if __name__=="__main__":
  print(f"el valor total de la lista es {sum_list(lista)}")
  
#EJ 2: 
def repetir_frase(num,frase):
  if num >=1:
    print(frase)
    repetir_frase(num-1, frase)

if __name__=="__main__": #cuando usemos esta funcion repetir_frase en otro archivo, tambien el otro archivo ejecutara las llamadas a la funcion aqui, por eso ponemos esta sentencia.
  repetir_frase(3, "Hola mundo") 


#EJ 3:
def suma_recursiva(num):
  if num == 0:
    return 0
  else:
    return num + suma_recursiva(num-1)
  

#EJ 4
#funcion de fibonacci: serie de numeros que parte de dos bases iniciales: 0 y 1. Y luego cada numero en la serie es el resultado de la suma de los dis ultimos numeros.
#pos0 = 0 
#pos1 = 1
#pos2 = pos0+pos1 =0+1=1
#pos3 = pos1+pos2 =1+1=2
#pos4 = pos2+pos3 =1+2=3
#pos5 = pos3+pos4 =3+2=5

#osea decimos: posN = posN-1 + posN -2

def fibonacci_recursiva(posicion):
  if posicion == 0:
    return 0
  elif posicion == 1:
    return 1
  else:
    return fibonacci_recursiva(posicion-1) + fibonacci_recursiva(posicion-2)
  

#EJ 5
def es_primo(numero):
  if numero <= 1:
    return False
  
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False
  return True

def sum_n_primos(num):
  if num==1:
    return 0
  elif es_primo(num):
    return num + sum_n_primos(num-1)
  else:
    return sum_n_primos(num-1)
