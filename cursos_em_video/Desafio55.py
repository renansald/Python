for x in range(0, 5):
    peso = float(input('Informe o peso da pessoa {}: '.format(x+1)))
    if(x == 0):
        maiorPeso = menorPeso = peso
    if(peso > maiorPeso):
        maiorPeso = peso
    if(peso < menorPeso):
        menorPeso = peso
print('O maior peso é {:.2f} e o menor peso é {:.2f}'.format(maiorPeso, menorPeso))
