pessoas = list();
dados = list();
while(True):
    dados.append(str(input("Informe o nome da pessoa: ")).strip());
    dados.append(float(input("Informe o peso da pessoa: ")));
    pessoas.append(dados[:]);
    dados.clear()
    opt = str(input("Deseja continuar? [S/N]")).strip().upper();
    while((opt != "S") and (opt != "N")):
        opt = str(input("Deseja continuar? [S/N]")).strip().upper();
    if(opt == 'N'):
        break;
for e, p in enumerate(pessoas):
    if(e == 0):
        menorpeso = maiorpeso = p[1];
    else:
        if(menorpeso > p[1]):
            menorpeso = p[1];
        elif(maiorpeso < p[1]):
            maiorpeso = p[1];
print(f"Foram cadastradas {len(pessoas)}.\n O maior peso foi de {maiorpeso:.1f}. Peso de ", end="");
for p in pessoas:
    if (p[1] == maiorpeso):
        print(f"{p[0]}", end=" ");
print(f"\nO menor peso foi {menorpeso:.1f}. Peso de", end=" ");
for p in pessoas:
    if(p[1] == menorpeso):
        print(f"{p[0]}", end =" ");
print("")
