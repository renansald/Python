inferior = int(input("Informe o menor valor do inervalo: "));
superior = int(input("Informe o maior valor do intervalo: "));
num = int(input("Informe um valor: "));
if((num >= inferior) and (num <= superior)):
    print("O valor digitado está dentro do intervalo");
else:
    print("O valor está fora do intervalo");
