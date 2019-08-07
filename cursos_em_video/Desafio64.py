soma = 0;
count = 0;
numero = int(input("Informe o numero: "))
while(numero != 999):
    count += 1;
    soma += numero;
    numero = (int(input("Informe um novo número: ")))
print("A Soma de todos os número digitados é {} e foram digitados {} números".format(soma, count))
