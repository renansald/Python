nota1 = float(input("Informe a primeira nota: "));
nota2 = float(input("Informe a segunda nota: "));
nota3 = float(input("Informe a terceira nota: "));
media = (nota1+nota2+nota3)/3;
if(media < 4):
    print("\33[7;31;40mREPROVADO\33[m");
elif(4 <= media < 5):
    print("\33[1;31;40mRECUPERAÇÃO\33[m");
elif(5 <= media < 6):
    print("\33[1;33;40mPROVA EXTRA\33[m");
else:
    print("\33[1;32;40mAPROVADO\33[m");
