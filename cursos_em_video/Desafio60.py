numero1 =  numero2 = int(input("Informe o número: "))
fatorial = 1
while(numero2 != 0):
    fatorial = fatorial * numero2
    numero2 -= 1
print("{}! é {}".format(numero1, fatorial))
