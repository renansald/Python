numero = float(input('Informe o valor: '))
for i in range(0,11):
    print('{:02} x {:02.0f} = {:02.0f}'.format(i, numero, (i*numero)))
