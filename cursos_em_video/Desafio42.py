reta1 = float(input("Informe a primeira reta: "))
reta2 = float(input("Informe a segunda reta: "))
reta3 = float(input("Informe a terceira reta: "))
aux = (reta1 + reta2 + reta3)/2
if((reta1 <= 0) or (reta2 <= 0) or (reta3 <= 0) or (aux-reta1 <= 0) or (aux-reta2 <= 0) or (aux-reta3 <= 0)):
    print("Não é possível criar um triângulo")
else:
    print("É possível criar um triângulo", end = ',')
    if((reta1 == reta2) and (reta1 == reta3) and (reta2 == reta3)):
        print(' Equilátero')
    elif((reta1 == reta2) or (reta1 == reta3) or (reta2 == reta3)):
        print(' Isósceles')
    else:
        print(' Escaleno')
