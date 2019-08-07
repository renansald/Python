count = soma = 0;
while(True):
    numero = float(input("Informe o valor: "))
    if(numero == 999):
        break;
    count += 1;
    soma += numero
print(f'Foram digitados {count} números e a soma dos números é {soma:.2f}')
