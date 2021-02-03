#Code created to explore a list of urban trees of the city of BS AS.

import csv
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding= 'utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows) 
        indices = [headers.index(colum) for colum in headers]
        row = next(rows)
        record = { colum : row[index] for colum, index in zip(headers, indices) }
        arboleda =[record for row in rows]
    return arboleda

arboleda = leer_arboles("C:/.../arbolado-en-espacios-verdes.csv")
arboleda


arboleda = leer_arboles('C:/.../arbolado-en-espacios-verdes.csv')
especie = "Jacarandá" 
H = [float(arbol["altura_tot"]) for arbol in arboleda if arbol["nombre_com"] == especie]
H

#New list with tuples
#Containing height and diameter of each "Jacaranda" in the list.

arboleda = leer_arboles("C:/.../arbolado-en-espacios-verdes.csv")
especie = "Jacarandá"
H = [float(arbol["altura_tot"]) for arbol in arboleda if arbol["nombre_com"] == especie]
D = [float(arbol["diametro"]) for arbol in arboleda if arbol["nombre_com"] == especie]
a = zip(H,D)
nueva_lista = tuple(a)
nueva_lista
