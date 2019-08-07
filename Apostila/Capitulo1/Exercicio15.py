import math
lado1 = float(input("Informe o primeiro lado: "))
lado2 = float(input("Informe o segundo lado: "))
lado3 = float(input("Informe o terceiro lado: "))
aux = (lado1 + lado2+ lado3)/2
area = math.sqrt((aux*(aux-lado1)*(aux-lado2)*(aux-lado3)));
print("O triângulo possui a seguinte area {:.2f}".format(area))
