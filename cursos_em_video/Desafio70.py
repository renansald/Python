produBarato = "";
menosque1000 = totalGasto = 0;
produto = str(input("Informe o nome do produto: "));
preco = float(input("Informe o preço do produto: "));
if(preco < 1000):
    menosque1000 += 1;
totalGasto += preco;
produBarato = produto;
produtoBarato = preco;
while(True):
    opcao = str(input("Deseja continuar cadastrando[S/N]: ")).strip().upper()
    if(opcao == 'S' or opcao == 'N'):
        break;
if(opcao == "S"):
    while(True):
        produto = str(input("Informe o nome do produto: "));
        preco = float(input("Informe o preço do produto: "));
        if(preco < 1000):
            menosque1000 += 1;
        if(produtoBarato > preco):
            produBarato = produto;
            produtoBarato = preco;
        totalGasto += preco;
        while(True):
            opcao = str(input("Deseja continuar cadastrando[S/N]: ")).strip().upper()
            if(opcao == 'S' or opcao == 'N'):
                break;
        if(opcao == 'N'):
            break;
print(f"O produto mias barato foi {produBarato}\n{menosque1000} itens custaram menos de R$ 1000\nO total da compra foi {totalGasto:.2f}")
