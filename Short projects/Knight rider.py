#Code aimed to emulate the propagation of lights used in the intro of the 1982 series knight rider ("auto fantástico").

def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l): #para cada elemento en l
        if e==1 and i<n-1: #si el elemento es igual a 1 y estoy dentro del rango de l
            if l[i+1]==0: #si el elemento siguiente es o
                l[i+1] = 1 #le asigno el valor 1 al elemento siguiente
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1] #propagar a derecha pero empezando por el último elemento
#%
def propagar(l):
    ld=propagar_a_derecha(l)
    lp = propagar_a_izquierda(ld)
    return lp
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Propagando...")
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
