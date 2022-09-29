#Code created to calcule the cost of a truck loaded with different boxes of fruits.

import csv
import sys

def costo_camion(funcion_frutas):
    f = open('C:/.../camion.csv', 'rt')
    headers = next(f).split(',')
    costo_total = 0
    costo_fila = 0

    for line in f:
        row = line.split(',')
        costo_fila = int(row[1]) * float(row[2])
        costo_total = costo_total + costo_fila
        print('Costo acumulado:', costo_total)
    print('El costo total del camion es:', costo_total)
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'

costo = costo_camion(nombre_archivo)
