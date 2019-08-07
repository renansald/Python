from sys import exit
numero = list();
num = int(input("Informe um número: "));
while True:
    numero.append(num%10);
    num = num//10;
    if(num == 0):
        break;
for x in range(0, len(numero)):
    if(numero[x] != numero[len(numero)-(x+1)]):
        print("Não é um palindrome");
        exit();
print("O número é um palindrome")
