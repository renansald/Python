numero = [[], []];
for x in range(0, 7):
    num = int(input("Informe um número: "));
    if(num%2 == 0):
        numero[0].append(num);
    else:
        numero[1].append(num);
numero[0].sort();
numero[1].sort();
print(f"Os números pares foram {numero[0]}\nOs números inmpáres foram {numero[1]}")
