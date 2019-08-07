x = float(input("Informe um valor de \"x\": "));
y = float(input("Informe um valor de \"y\": "));
if(x < 0):
    if(y < 0):
        print("3º quadrante");
    elif(y == 0):
        print("Entre o 2º e 3º quadrante")
    else:
        print("2º quadrante");
elif(x > 0):
    if(y > 0):
        print("1º quadrante");
    elif(y == 0):
        print("Entre o 1º e 4º quadrante")
    else:
        print("4º quadrante");
else:
    if(y > 0):
        print("Entre o 1º e o 2º quadrante");
    elif(y < 0):
        print("Entre o 3º e 4º quadrante");
    else:
        print("Origem");
