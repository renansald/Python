numeros = list();
for x in range(0, 5):
    numeros.append(int(input(f"Informe o valor {x+1}: ")));
print("-"*30);
print(f"O maior valor foi {max(numeros)} e sua(s) posição(ções) é(são) ", end="");
for n, v in enumerate(numeros):
    if v == max(numeros):
        print(f"{n+1}...", end="");
print(f"\nO menor valor foi {min(numeros)} e sua(s) posição(ções) é(são) ", end="");
for n, v in enumerate(numeros):
    if v == min(numeros):
        print(f"{n+1}...", end="");
