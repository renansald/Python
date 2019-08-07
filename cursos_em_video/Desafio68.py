import random
while(True):
    cpu = random.randint(0, 100000000000);
    playern = int(input("Escolha um número: "));
    playerPI = str(input("Escolha o seu lado[P/I]: ")).strip().upper();
    if((playerPI != 'P') and (playerPI != 'I')):
        print("Voce deve escolher P ou I refaça toda sua jogada");
        continue;
    if(((cpu + playern)%2 == 0) and (playerPI == "P")):
        print(f"Parabéns vc ganhou, os números eram {cpu} e {playern}");
    elif(((cpu + playern)%2 != 0) and (playerPI == "I")):
        print(f"Parabéns vc ganhou, os números eram {cpu} e {playern}");
    else:
        print(f"Você perdeu, os números eram {cpu} e {playern}");
        break;
