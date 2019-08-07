peso = float(input("Informe o peso da pessoa: "));
altura = float(input("Informe a altura da pessoa: "));
imc = peso/(altura**2);
if((imc >= 20) and (imc < 25)):
    print("\33[1;32;40mPeso ideal\33[m");
elif((imc >= 25) and (imc < 30)):
    print("\33[1;33;40mSobre peso\33[m");
elif((imc >= 30) and (imc < 40)):
    print("\33[1;31;40mObesidade\33[m");
else:
    print("\33[7;31;40mObesidade mórbida\33[m");
