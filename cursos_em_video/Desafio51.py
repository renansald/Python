a1 = float(input("Informe o seu a indice 1: "))
r = float(input('Informe a sua razão: '))
for x in range(1, 11):
    print('{}'.format(a1*(r**(x-1))))
