from math import sin, cos, tan, radians
angulo = float(input("Informe o angulo: "))
print('O seno de {} e: {}\nO cosseno de {} é:{}\nA tangente de {} é: {}'.format(radians(angulo), sin(radians(angulo)), angulo, cos(radians(angulo)), angulo, tan(radians(angulo))))
