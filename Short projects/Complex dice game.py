#Code created to emulate the behaviour of a dice game. 
#The objective of the game is to achieve the highest score, according to the assessment established for each possible move in the game, called category. 
#Each roll consists of the throwing of the five dice, and depending on the numbers that come out, a category can be chosen
#If a satisfactory category is not achieved on the first roll, the useful dice can be set aside and the others taken and rolled again; In this second roll, the most convenient ones can be set aside again and put together with those that were already set aside, and then the rest will be rolled for the third and last time, thus ending the roll. 
#If a category was achieved in a single shot, this is called a "shot served" (this will only apply to larger games; see below). This can only happen on the first of the three shots on each turn 3. The score is established in relation to the category obtained with the combination of the 5 dice. 

def tirar():
    import random
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return(tirada)

lista = tirar()
def es_generala(lista):
    for i in lista:
        if i == lista[1] and i == lista[2] and i == lista[3] and i == lista[4]:
            a = print(True)
            break
        else:
            a = print(False)
    return(a)    
            
   

es_generala(lista))

N = 1000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
