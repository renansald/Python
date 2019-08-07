frase = str(input("Informe a frase desejada: ")).strip()
test = frase.upper().split()
test = ''.join(test)
for x in range(0, (len(test)-1)):
    if(test[x] != test[(len(test) -1)-x]):
        print("A frase {} não é um palíndromo".format(frase))
        break
    elif(x == len(test)-2):
        print('A frase {} é um palindromo'.format(frase))
