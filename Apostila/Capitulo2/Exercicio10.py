opc = str(input("Menu:\nDigite + para soma\nDigite - para subtração\nDigite * para multiplicação\nDigite / para divisão\nInforme a opção desejada: ")).strip();
while((opc != '+') and (opc != '=') and (opc != '*') and (opc != '/')):
    opc = str(input("\33[1;31;40mERRO:Operação não encontrada\33[m\nMenu:\nDigite + para soma\nDigite - para subtração\nDigite * para multiplicação\nDigite / para divisão\nInforme a opção desejada: "));
num1 = float(input("Informe o primeiro valor: "));
num2 = float(input('Informe o segundo valor: '));
if(opc == "+"):
    print(f"{num1} + {num2} = {num1+num2}");
elif(opc == '-'):
    print(f"{num1} - {num2} = {num1-num2}");
elif(opc == '/'):
    print(f"{num1} / {num2} = {num1/num2}");
else:
    print(f"{num1} * {num2} = {num1*num2}");
