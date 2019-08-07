from random import randint
from operator import itemgetter
jogador = {'jogador1': randint(1, 6), 'jogador2': randint(1,6), 'jogador3': randint(1, 6), 'jogador4': randint(1,6)}
podium = sorted(jogador.items(), key = itemgetter(1), reverse = True); #gera uma tuplua dentro de uma lista
for e, j in enumerate(podium):
    print(f"O {e+1}º lugar vai para {j[0]} com {j[1]}");
