from random import randint;
numeros = [randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000)];
print("Os valores sorteados foram:", end = " ")
for x in range(0, len(numeros)):
    '''if(x == 0):
        maior = menor = numeros[x];
    if(maior < numeros[x]):
        maior = numeros[x];
    if(menor > numeros[x]):
        menor = numeros[x];'''
    print(f"{numeros[x]}", end = " ");
print(f"\nO menor numero sorteado foi {min(numeros)}\nO maior numero sorteado foi {max(numeros)}");
