lista = list();
while(True):
    numero = int(input("\33[mInforme um numero:\33[1;32m "));
    lista.append(numero);
    opt = str(input("\33[mDeseja continuar? [S/N]: \33[1;32m")).strip().upper();
    while((opt != "S") and (opt != "N")):
        opt = str(input("\33[mDeseja continuar? [S/N]: \33[1;32m")).strip().upper();
    if(opt == 'N'):
        break;
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)}\nA lista de forma decrescente é {lista}")
print("O valor 5 está na lista" if(5 in lista) else "O valor 5 não está na lista")
