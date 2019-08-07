from random import randint
lista = list();
temp = list();
jogos = int(input("Informe o numero de jogos desejados: "));
for x in range(0, jogos):
    for y in range(0, 6):
        num = randint(0, 61);
        while(num in temp):
            num = randint(0, 61);
        temp.append(num);
    lista.append(temp[:]);
    temp.clear();
for e, l in enumerate(lista):
    print(f"Jogo {e+1}: {l}");
