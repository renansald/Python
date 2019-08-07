from random import randint
numero = randint(0, 5);
print('{}'.format(numero))
numero2 = int(input('Escolha um numero: '))
if numero == numero2:
    print('parabens vc acertou', end ='>>>>')
else:
    print("vc errou")
