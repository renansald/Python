itens = ["Lápis", 1.40, "Caneta", 20.00, "Borracha", 0.60];
print("_"*30);
print(f"{'Preços': ^30}");
print("-"*30);
for x in range(0, len(itens), 2):
    print(f"{itens[x]:.<20}R$ {itens[x+1]:.2f}");
