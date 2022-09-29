#Code created to explore and visualize a list of urban trees of the city of Bs As.

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

#Exploring the list

import csv
import arboles
def leer_parque(archivo, parque):
    f = open(archivo, "rt", encoding = "utf-8")
    filas = csv.reader(f)
    encabezados = next(filas)
    fila = next(filas)
    lista_parque = []
    for fila in filas:
        record = dict(zip(encabezados, fila))
        if record["espacio_ve"] == parque:
            arbol = {record["id_arbol"], record["nombre_com"]}
            lista_parque.append(arbol)
    return(lista_parque)

lista_arboles = leer_parque("../arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
lista_arboles.split()
#2.23
def especies(lista_arboles):
    especies = []
    lista = tuple(lista_arboles)
    lista2 = dict(lista)
    for i in lista2:
        lista_comun = lista2[str]
        especies = lista_comun
    return(especies)
especies(lista_arboles)

#ID and common names

import csv
def leer_parque(archivo, parque):
    f = open(archivo, "rt", encoding = "utf-8")
    filas = csv.reader(f)
    encabezados = next(filas)
    fila = next(filas)
    lista_parque = []
    for fila in filas:
        record = dict(zip(encabezados, fila))
        if record["espacio_ve"] == parque:
            arbol = record["id_arbol"], record["nombre_com"]
            lista_parque.append(arbol)
    return(lista_parque)

arboles = leer_parque("../arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
arboles
len(arboles)
