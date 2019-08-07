from time import sleep
def MaiorValor(*valor):
    """
    :param valor: recebe n valores
    :return: void
    """
    print("Analisando valores...");
    if(len(valor) > 0):
        maior = valor[0]
        print(f"{valor[0]}", end=" ", flush = True);
        sleep(0.5);
        for x in range(1, len(valor)):
            print(f"{valor[x]}", end= " ", flush = True);
            sleep(0.5);
            if(valor[x] > maior):
                maior = valor[x];
        print();
    else:
        maior = 0;
    print(f"Foram passados {len(valor)} e o maior deles é {maior}");

###Main###
help(MaiorValor);
MaiorValor(2, 9, 4, 5, 7, 1);
MaiorValor(4, 7, 0);
MaiorValor(1, 2);
MaiorValor(6);
MaiorValor();
