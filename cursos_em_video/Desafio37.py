base = int(input("Informe 1 para conversão para base 2\nInforme 2 para conversão para base 8\nInforme 3 para conversão para base 16: "))
numero = int(input("Informe o número: "))
if(base == 1):
    print('O número é: {}'.format(bin(numero)))
elif(base == 2):
    print('O número é: {}'.format(oct(numero)))
else:
    print('O número é: {}'.format(hex(numero)))
