#A simple function to search an item in a list and return the position and number of repetitions of that single elemnt in the given list.


def buscar_un_elemento(lista, e):
    pos = -1  
    i = 0     
    for z in lista:  
        if z == e:   
            pos = i  # guardamos su posición
                
        i += 1       
    return pos

buscar_un_elemento([1,2,3,2,3,4],1)
buscar_un_elemento([1,2,3,2,3,4],2)
buscar_un_elemento([1,2,3,2,3,4],3)
buscar_un_elemento([1,2,3,2,3,4],5)

def buscar_n_elemento(lista,e):
  apariciones = -1
  i = 0
  for z in lista:
    if z == e:
      apariciones = i + 1
      i += 1
  return(apariciones)

buscar_n_elemento([1,2,3,2,3,4],1)
buscar_n_elemento([1,2,3,2,3,4],2)
buscar_n_elemento([1,2,3,2,3,4],3)
buscar_n_elemento([1,2,3,2,3,4],5)

#3.7
def maximo(lista):
  m = 0
  lista.sort(reverse = True)
  for e in lista:
    if e == lista[0]:
      m = e
      break
  return(m)

maximo([1,2,7,2,3,4])
maximo([1,2,3,4])
maximo([-5,4])
maximo([-5,-4])
