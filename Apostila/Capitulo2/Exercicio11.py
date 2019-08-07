lado1 = int(input("Informe o primeiro lado: "));
lado2 = int(input("Informe o segundo lado: "));
lado3 = int(input("Informe o terciro lado: "));
if(((lado1+lado2) < lado3) or ((lado1+lado3)<lado2) or ((lado2+lado3) < lado1)):
    print("\33[1;31;40mInfelizmente não é um triângulo\33[m");
else:
    if(lado1 == lado2 == lado3):
        print("Forma um triângulo equilátero");
    elif((lado1 == lado2 != lado3) or (lado1 == lado3 != lado2) or (lado2 == lado3 != lado1)):
        print("Forma um triângulo isóceles");
    else:
        print("Forma um triângulo escaaleno");
