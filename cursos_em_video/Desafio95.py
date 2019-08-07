from sys import exit
jogador = dict();
gols = list();
lista = list();
total = 0;
while(True):
    jogador['Nome'] = str(input("Informe o nome do Jogador: ")).strip();
    partidas = int(input("Informe o número de partidas: "));
    for x in range(0, partidas):
        gols.append(int(input(f"Informe o número de gols na {x+1} partida: ")));
    jogador['Gols'] = gols[:];
    jogador['Total de gols'] = sum(gols);
    gols.clear();
    lista.append(jogador.copy());
    opc = str(input("Deseja continuar?[S/N]: ")).strip().upper();
    while((opc != 'N') and (opc != 'S')):
        opc = str(input("Opção inválida. Deseja continuar?[S/N]: ")).strip().upper();
    if(opc == 'N'):
        break;
print("_"*30);
print("cod", end=" ");
for x in jogador.keys():
    print(f"{x:<15}", end="");
print("\n"+"_"*60);
for e, x in enumerate(lista):
    print(f"{e+1}  {x['Nome']:<15} {str(x['Gols']):<15} {x['Total de gols']:<15}");
while(True):
    cod = int(input("Informe o código do jogador que deseja ver as estátiscas: "));
    while(cod > len(lista) or (cod < 1)):
        if(cod == 999):
            exit()
        cod = int(input("Jogador não encontrado. Informe o código do jogador que deseja ver as estátiscas: "));
    print(f"Levantamento do jogador {lista[cod-1]['Nome']}:");
    for e, x in enumerate(lista[cod-1]['Gols']):
        print(f"    =>No jogo {e+1} fez {x} gols");
