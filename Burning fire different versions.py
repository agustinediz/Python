def propagar_v1(lis):
    for i, f in enumerate(lis):
        if i - 1 >= 0:                
            if f==0 and lis[i-1]==1:
                lis[i] = 1
            
    return lis
                
    
def propagar_v2(lis):
    for i, f in enumerate(lis):
        if i - 1 >= 0:                
            if f==0 and lis[i-1]==1:
                lis[i] = 1
        if i + 1 < len(lis):
            if f==0 and lis[i+1]==1:
                lis[i] = 1            
    return lis    


def propagar_v3(lis):
    hice_cambio = True
    while hice_cambio:
        hice_cambio = False
        for i, f in enumerate(lis):
            if i - 1 >= 0:                
                if f==0 and lis[i-1]==1:
                    lis[i] = 1
                    hice_cambio = True

            if i + 1 < len(lis):
                if f==0 and lis[i+1]==1:
                    lis[i] = 1        
                    hice_cambio = True
    return lis    

def propagar_v4(lis):
    for i in range(len(lis)):
        if i - 1 >= 0:                
            if lis[i]==0 and lis[i-1]==1:
                lis[i] = 1
                
    for i in range(len(lis)-1,-1,-1):
        if i + 1 < len(lis):
            if lis[i]==0 and lis[i+1]==1:
                lis[i] = 1        

    return lis 
    
lista_1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 1, 0, 0]
