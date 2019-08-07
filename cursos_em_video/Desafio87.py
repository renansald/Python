matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Informe o numer da matriz[{linha}, {coluna}]: "));
somapares = colunatres = 0;
for l in range(0, 3):
    for c in range(0, 3):
        print(f"{matriz[l][c]}", end= " ");
        if(matriz[l][c]%2 == 0):
            somapares += matriz[l][c];
        if(c == 2):
            colunatres += matriz[l][c];
    print();
print(f"A soma de todos os valores pares é: {somapares}\nA soma dos valores da terceira coluna é {colunatres}\nO maior valor da segunda linha é {max(matriz[1])}");
