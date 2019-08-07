lista = list();
for x in range(0, 5):
    numero = int(input("Informe um valor: "));
    if(len(lista) == 0):
        print("Valor adicionado na posição 0");
        lista.append(numero);
    else:
        for e, n in enumerate(lista):
            if(numero <= n):
                print(f"Valor adicionado na posição {e +1} da lista");
                lista.insert(e, numero);
                break
            elif(e == (len(lista) - 1)):
                print(f"Valor adicionado na posição final da lista");
                lista.append(numero);
                break;
    opt = str(input("Desejar sair da aplicação? [s/n]: ")).strip().upper()
    while((opt != 'S') and (opt != "N")):
        opt = srt(input("Desejar sair da aplicação? [s/n]: ")).strip().upper()
    if(opt == "S"):
        break;
print(f"Os valores digitados na ordem são {lista}");
