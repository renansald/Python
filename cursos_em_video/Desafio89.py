from time import sleep
diario = list();
temp = list();
notas = list();
while(True):
    temp.append(str(input("Infoemr o nome do aluno: ")).strip());
    notas.append(float(input("Informe a primeira nota do aluno: ")));
    notas.append(float(input("Informe a segunda nota do aluno: ")));
    temp.append(notas[:]);
    temp.append((notas[0] + notas[1])/2);
    notas.clear();
    diario.append(temp[:]);
    temp.clear();
    opt = str(input("Deseja continuar adicionando dados? [S/N]").strip().upper());
    while((opt != "S") and (opt != "N")):
        opt = str(input("Deseja continuar adicionando dados? [S/N]").strip().upper());
    if(opt == "N"):
        break;
print("_"*30);
print("Nº  Nome"+("."*6)+("Nota 1")+(" Nota 2 Média"))
for n, d in enumerate(diario):
    print(f"{n}   {d[0]:.<10}{d[1][0]:^6.1f} {d[1][1]:^6.1f} {d[2]:^5.1f}");
while(True):
    num = int(input("Informe o número do aluno desejado: "));
    if(num == 999):
        break;
    elif(num >= len(diario)):
        print("Aluno inválido:");
    else:
        print(f"As notas do aluno {diario[num][0]} são {diario[num][1][0]} e {diario[num][1][1]}");
sleep(2);
print("Bye");
