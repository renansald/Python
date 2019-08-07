while(True):
    numero = int(input("Informe o valor da tabuada desejada: "))
    if(numero < 0):
        break;
    if(numero == 0):
        continue;
    print("------------------------------------------------")
    for x in range(0, 11):
        print(f'{numero} x {x} = {numero*x}')
    print("------------------------------------------------")
