#Code to emulate the behaviour of lighted matches in a row. The function works as each match turn on an adjacent new match or ligthed match but it doesnt to an 
#already used match.
#Coded the situation as 0(new), 1 (lighted) and -1 (used).

def propagar(lista):
    lista_nueva = []
    i = 0
    for e in lista:
        if e == 1:
            i = i +1 
            lista_nueva = lista.insert(i, 1)
        elif e == 0:
            i = i + 1
            lista_nueva = lista.insert(i, 1)
    return(lista_nueva)
