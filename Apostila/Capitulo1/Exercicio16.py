import math
r = float(input('Informe o raio do circulo; '))
area = math.pi*(r**2)
perimetro = 2*math.pi*r
diametro = 2*r
print('O circulo possui:\nPerimetro {:.2f}\nArea {:.2f}\nDiâmetro {:.2f}'.format(area, perimetro, diametro))
