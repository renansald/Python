numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))
print('A media de {} {} {} é: {:*^30.2f} e quando inteiro {}'.format(numero1, numero2, numero3, ((numero1+numero2+numero3)/3), ((numero1+numero2+numero3)//3)))
