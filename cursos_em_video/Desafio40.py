nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1+nota2)/2
if(media < 5.0):
    print("\33[1;31mREPROVADO\33[m")
elif((media >= 5.0) and (media <= 6.9)):
    print("\33[1;33mRECUPERAÇÃO\33[m")
else:
    print("\33[1;32mAPROVADO\33[m")
