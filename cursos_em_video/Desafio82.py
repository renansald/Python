lista = list();
listimpar = list();
listapar = list();
while(True):
    numero = int(input("Informe  número: "));
    #if(numero%2 == 0):
    lista.append(numero);
    '''    listapar.append(numero);
    else:
        listimpar.append(numero);
        lista.append(numero);'''
    opt = str(input("Deseja continuar? [S/N]")).strip().upper();
    while((opt != "S") and (opt != "N")):
        opt = str(input("Deseja continuar? [S/N]")).strip().upper();
    if(opt == "N"):
        break;
for e, n in enumerate(lista):
    if(n%2 == 0):
        listapar.append(lista[e]);
    else:
        listimpar.append(lista[e])
print(f"Lista com numero totais: {lista}\nLista com pares: {listapar}\nLista com impares: {listimpar}");
