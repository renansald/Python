matriz = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]];
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].insert(coluna, str(input(f"Informe o valor da matrix[{linha}, {coluna}]: ")));
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"{matriz[linha][coluna]:^4}", end=" ");
    print(" ");
