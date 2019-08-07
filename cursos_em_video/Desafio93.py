jogador = dict();
gols = list();
total = 0;
jogador['Nome'] = str(input("Informe o nome do Jogador: ")).strip();
partidas = int(input("Informe o número de partidas: "));
for x in range(0, partidas):
    gols.append(int(input(f"Informe o número de gols na {x+1} partida: ")));
    total += gols[x];
jogador['Gols'] = gols;
jogador['Total de gols'] = total;
print("_"*30);
print(f"O jogador {jogador['Nome']} jogou {partidas}.");
for e, g in enumerate(jogador['Gols']):
    print(f"    =>Na partida {e+1}, fez {g} gols;");
print(f"Foi um total de {jogador['Total de gols']} gols");
