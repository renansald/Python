from math import sqrt
a = float(input("Informe o valor de \'a\': "));
b = float(input("Informe o valor de \'b\': "));
c = float(input("Informe o calor de \'c\': "));
delta = (b**2) - (4*a*c);
if(delta > 0):
    print(f"As raízes são {((-b) + sqrt(delta))/(2*a)} e {((-b) - sqrt(delta))/(2*a)}");
elif(delta == 0):
    print(f"Só tem uma raíz que é: {(-b)/(2*a)}");
else:
    print("Número imaginário");
