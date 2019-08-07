from random import randint;
from time import sleep;
def Sorteio(list):
    print("Sorteando 5 valores para a lista", end=" ", flush = True)
    for x in range(0, 5):
        list.append(randint(0, 1000));
        sleep(0.5);
        print(f"{list[x]}", end = " ", flush = True);

def SomaPar(list):
    print("Somando valores pares: ");
    soma = 0;
    for x in list:
        if(x%2 == 0):
            soma += x;
    sleep(0.5);
    print(f"{soma}");

###MAIN###
list = list();
Sorteio(list);
SomaPar(list);
