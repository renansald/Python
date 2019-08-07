numero = int(input('Informe um número: '))
for x in range(1, numero+1):
    if((x < numero) and (x != 1) and (numero%x == 0)):
        print("O número {} não é primo".format(numero))
        break
    elif((x == numero)):
        print("O número {} é primo".format(numero))
