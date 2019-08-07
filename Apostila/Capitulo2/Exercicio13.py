num1 = int(input("Informe o primeiro número: "));
num2 = int(input("Informe o segundo número: "));
while(((num1 < 0) or (num2 < 0) or (num1 > 10) or (num2>10))):
    print("\33[1;31;40mERRO os Números tem que está entre 0 e 10\n{:^30}Por favor entre com os novos números\33[m")
    num1 = int(input("Informe o primeiro número: "));
    num2 = int(input("Informe o segundo número: "));
if((num1 + num2) < 8):
    print(f"A média dos números é {(num1+num2)/2}");
elif((num1+num2) == 8):
    print(f"O produto dos números é {num1*num2}");
else:
    if(num1 >= num2):
        print(f"A divisão de {num1} e {num2} é {num1/num2}");
    else:
        print(f"A divisão de {num2} e {num1} é {num2/num1}");
