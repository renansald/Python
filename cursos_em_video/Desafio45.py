from random import choice
jogadas = ["pedra", "papel", "tesoura"]
cpu = choice(jogadas)
print(cpu)
player = str(input("Infome sua jogada: ")).strip()
if(((player == 'pedra') and (cpu == 'papel')) or ((player == 'papel') and (cpu == 'tesoura')) or ((player == 'tesoura') and (cpu == 'pedra'))):
    print('\33[1;31mPERDEU\33[m')
else:
    print('\33[1;33m PARABÈNS VC VENCEU\33[m')
