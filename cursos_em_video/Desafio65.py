opcao = 'S';
count = 0;
soma = 0;
while(opcao == 'S'):
    numero = int(input("Informe o valor: "))
    if (count == 0):
        menorValor = maiorValor = numero;
    if(numero < menorValor):
        menorValor = numero;
    elif(numero > maiorValor):
        maiorValor = numero;
    count += 1;
    soma += numero;
    opcao = str(input("Deseja continuar escrevendo valore?[S/N]")).upper()
print("O maior valor foi {};\nO menor valor foi {}.\nA Media dos valores Digitados foi {}".format(maiorValor, menorValor, soma/count))
