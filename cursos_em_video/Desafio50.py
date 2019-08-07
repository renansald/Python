soma = int(0)
for x in range(0, 6):
    numero = int(input('Informe o {}º número: '.format(x+1)))
    if(numero%2 == 0):
        soma += numero
print("A soma é {}".format(soma))
