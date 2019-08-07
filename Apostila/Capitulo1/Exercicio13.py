from math import sqrt
base = float(input("Informe a base do triângulo: "))
altura = float(input("Informe a altura do triângulo: "))
hipotenusa = sqrt((base**2) + (altura**2))
print("O triângulo de base {:.2f} e altura {:.2f} tem como área {:.2f} e perimetro {:.2f}".format(base, altura, ((base*altura)/2), (base+altura+hipotenusa)))
