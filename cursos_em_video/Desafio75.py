um = int(input("Informe uma valor: "));
dois = int(input("Informe o segundo valor: "));
tres = int(input("Informe o terceiro valor: "));
quatro = int(input("Informe o o quarto valor: "));
numeros = [um, dois, tres, quatro];
print(f"O valor 9 aparece {numeros.count(9)} vezes");
if(not(3 in numeros)):
    print("O valor 3 não foi digitado");
else:
    print(f"O valor 3 apareceu na {numeros.index(3) + 1}ª posição");
print("Os valores pares digitados foram: ", end = "");
for numero in numeros:
    if(numero%2 == 0):
        print(f"{numero} ", end = "");
print("")
