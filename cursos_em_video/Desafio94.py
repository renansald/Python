dic = dict();
pessoas = list();
media = 0;
while(True):
    dic['Nome'] = str(input("Informe o nome: ")).strip();
    dic['Sexo'] = str(input("Informe o sexo da pessoa [M/F]: ")).strip().upper();
    dic['Idade'] = int(input("informe a idade: "));
    pessoas.append(dic.copy());
    opc = str(input("Deseja continuar? [S/N]")).strip().upper();
    while((opc != 'N') and (opc != 'S')):
        opc = str(input("Opção inválida. Deseja continuar? [S/N]")).strip().upper();
    if(opc == 'N'):
        break;
print(f"Foram cadastrada {len(pessoas)} pessoas");
for x in pessoas:
    media += x['Idade'];
print(f"A média de idades do grupo é {media/len(pessoas)}\nAs mulheres do grupo são: ");
for x in pessoas:
    if(x['Sexo'] == 'F'):
        print(f"    =>{x['Nome']}");
print("As pessoas com idade acima da média são:");
for x in pessoas:
    if(x['Idade'] > (media/len(pessoas))):
        print(f"    =>{x['Nome']}")
