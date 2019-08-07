peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))
imc = (peso/(altura**2))
if(imc < 18.5):
    print("Abaixo do peso")
elif((imc >= 18.5) and (imc < 25)):
    print("Peso ideal")
elif((imc >= 25) and (imc < 30)):
    print('Sobrepeso')
elif((imc >= 30) and (imc < 40)):
    print("Obesidade")
else:
    print("Obesidade Mórbida")
